import requests
from bs4 import BeautifulSoup
import csv

URL = "https://news.ycombinator.com/"
CSV_FILE = "tech_news.csv"

def get_html(url):
    """
    Fetches the raw HTML content from the URL.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        response = requests.get(url, headers=headers)
        
        response.raise_for_status() 
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parse_news(html_content):
    """
    Parses the HTML and extracts headlines and links.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    news_data = []

    story_spans = soup.find_all("span", class_="titleline")

    for span in story_spans:
        link_tag = span.find("a")
        
        if link_tag:
            title = link_tag.get_text()
            link = link_tag.get("href")
            
            news_data.append({"Title": title, "Link": link})
            
    return news_data

def save_to_csv(data, filename):
    """
    Saves the list of dictionaries to a CSV file.
    """
    if not data:
        print("No data to save.")
        return

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Link"])
        
        writer.writeheader()
        
        writer.writerows(data)
        
    print(f"Successfully saved {len(data)} articles to {filename}")

if __name__ == "__main__":
    print(f"Scraping {URL}...")
    
    html = get_html(URL)
    
    if html:
        articles = parse_news(html)
        if articles:
            print("\nPreview of extracted data:")
            for item in articles[:3]: 
                print(f"- {item['Title']}")
            
            save_to_csv(articles, CSV_FILE)
        else:
            print("No articles found. The website structure might have changed.")