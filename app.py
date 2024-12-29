from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.parse
import pymongo
import datetime
import os
from flask import Flask, render_template, jsonify
import socket
import certifi
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set the SSL certificate file to the one from certifi
os.environ['SSL_CERT_FILE'] = certifi.where()

# MongoDB Setup
MONGO_URI = os.getenv('MONGO_URI')  # Fetch MongoDB URI from .env file
client = pymongo.MongoClient(MONGO_URI)
db = client["x_com_trends"]  # Database name
collection = db["trends"]  # Collection name

# Flask Setup
app = Flask(__name__)

# Proxy settings
proxy_username = os.getenv('PROXY_USERNAME')
proxy_password = os.getenv('PROXY_PASSWORD')
proxy_host = os.getenv('PROXY_HOST')
proxy_port = os.getenv('PROXY_PORT')

# URL encode the proxy username and password
encoded_username = urllib.parse.quote(proxy_username)
encoded_password = urllib.parse.quote(proxy_password)

# Define the full proxy URL
PROXY = f"http://{encoded_username}:{encoded_password}@{proxy_host}:{proxy_port}"

# Function to setup driver with proxy
def setup_driver():
    options = webdriver.ChromeOptions()

    # Use the proxy server argument
    # options.add_argument(f'--proxy-server={PROXY}')

    # Chrome options for debugging and ensuring proper proxy usage
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # Optional: Disable headless mode for debugging
    options.headless = False

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Login to X.com
def login_to_x(driver):
    email = os.getenv('EMAIL')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    
    driver.get("https://x.com/i/flow/login")
    wait = WebDriverWait(driver, 10)

    input_email = wait.until(EC.presence_of_element_located((By.NAME, "text")))
    input_email.clear()
    input_email.send_keys(email)
    sleep(3)

    button_1 = driver.find_elements(By.CSS_SELECTOR, "button div span span")
    if button_1:
        button_1[1].click()
    sleep(3)

    input_verification = wait.until(EC.presence_of_element_located((By.NAME, "text")))
    input_verification.clear()
    input_verification.send_keys(username)
    sleep(3)

    button_2 = driver.find_element(By.CSS_SELECTOR, "button div span span")
    button_2.click()
    sleep(3)

    input_password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    input_password.clear()
    input_password.send_keys(password)
    sleep(3)

    button_3 = driver.find_element(By.CSS_SELECTOR, "button div span span")
    button_3.click()
    sleep(5)

    driver.get("https://x.com/home")

    try:
        section_found = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'section[aria-labelledby="accessible-list-0"]'))
        )
        return True
    except:
        return False

# Scraping function
def scrape_news(driver):
    news_data = {}

    try:
        section_found = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'section[aria-labelledby="accessible-list-0"]'))
        )

        div_elements = section_found.find_elements(By.CSS_SELECTOR, 'div.css-146c3p1.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-b88u0q')

        if div_elements:
            for index, div in enumerate(div_elements):
                try:
                    span = div.find_element(By.CSS_SELECTOR, 'span.css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3')
                    news_text = span.text
                    if news_text:
                        trend_name = f"nameoftrend{index + 1}"
                        news_data[trend_name] = news_text
                except Exception as e:
                    print(f"Error while extracting news from a div: {e}")

        else:
            print("No div elements found in the section.")
    except Exception as e:
        print(f"Error during scraping: {type(e).__name__}: {e}")

    # Add timestamp and IP address
    news_data["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    news_data["ip_address"] = socket.gethostbyname(socket.gethostname())  # Get the local machine IP
    return news_data

# Function to store the news in MongoDB
def store_news_in_db(news_data):
    try:
        collection.insert_one(news_data)
        print("News stored in MongoDB.")
    except Exception as e:
        print(f"Error storing news in MongoDB: {e}")

# Flask route to trigger the scraping process
@app.route('/scrape_news', methods=['GET'])
def scrape_and_display():
    driver = setup_driver()

    try:
        if login_to_x(driver):
            news_data = scrape_news(driver)
            store_news_in_db(news_data)

            # Display the news in the HTML page
            return render_template('results.html', news_data=news_data)
        else:
            return "Login failed. Please try again later."
    finally:
        driver.quit()

# Flask route to display stored trends from MongoDB
@app.route('/')
def index():
    # Fetch the latest trends from MongoDB
    trends = collection.find().sort([("_id", -1)]).limit(1)  # Sort by _id in descending order and limit to 1 result
    latest_trends = list(trends)  # Convert the cursor to a list

    if latest_trends:
        latest_trend = latest_trends[0]  # Get the first (and only) record from the list
        return render_template('index.html', trends=latest_trend)
    else:
        return render_template('index.html', trends=None)

if __name__ == "__main__":
    app.run(debug=True)
