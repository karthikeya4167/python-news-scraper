# 📰 Hacker News Web Scraper

![Python](https://img.shields.io/badge/Python-3.13-blue)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.14-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

A lightweight, automated web scraper built to extract the latest top articles from Hacker News and save them into a clean, structured CSV format for data analysis. Built as part of a 20-Day Python Challenge.

## 🚀 Features
* **Automated Extraction:** Instantly pulls the newest headlines and URLs from the Hacker News front page.
* **Anti-Bot Bypass:** Utilizes custom `User-Agent` headers to simulate real browser traffic and prevent server blocks.
* **Data Parsing:** Cleanly navigates the DOM tree to separate messy HTML tags from the target text.
* **Structured Export:** Automatically formats and exports the extracted data into a universally readable `.csv` file.

## 💻 Tech Stack
**Core Language:**
* Python 3

**Libraries & Modules:**
* `requests` (HTTP Networking & GET requests)
* `beautifulsoup4` (HTML/XML DOM Parsing)
* `csv` (Built-in data export)

## 🛠️ Installation & Setup

Follow these steps to run the scraper locally on your machine.

**1. Clone the Repository**
```bash
git clone [https://github.com/karthikeya4167/python-news-scraper.git](https://github.com/karthikeya4167/python-news-scraper.git)
cd python-news-scraper
```

**2. Install Dependencies**
Ensure you have Python installed, then run:
```bash
pip install requests beautifulsoup4
```

**3. Run the Scraper**
Execute the script from your terminal:
```bash
python news_scraper.py
```

**4. View the Data**
Once the script finishes running, check the folder for a newly generated `tech_news.csv` file!

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

👤 Author

Karthik

GitHub: @karthikeya4167
