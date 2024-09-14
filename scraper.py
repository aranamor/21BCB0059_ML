import requests
from bs4 import BeautifulSoup
import threading
import time


def scrape_news():
    while True:
        url = 'https://news.google.com/topstories'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/58.0.3029.110 Safari/537.3'}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Check for HTTP request errors
            soup = BeautifulSoup(response.content, 'html.parser')

            articles = soup.select('h3 a')  # Google News uses <h3> for titles
            if articles:
                print("Scraping News Articles:")
                for article in articles[:5]:  # Limit to top 5 articles
                    title = article.get_text()
                    link = "https://news.google.com" + article['href'][1:]  # Google News links are relative
                    print(f"Title: {title}, Link: {link}")
            else:
                print("No articles found. The page structure may have changed.")

        except Exception as e:
            print(f"Error occurred while scraping: {e}")

        time.sleep(900)  # Scrapping every 15 mins


def start_scraper_thread():
    scraper_thread = threading.Thread(target=scrape_news)
    scraper_thread.daemon = True
    scraper_thread.start()


if __name__ == "__main__":
    start_scraper_thread()

# https://stackoverflow.com/questions/56106040/unable-to-scrape-google-news-heading-via-their-class
# Referred to this thread for this code
