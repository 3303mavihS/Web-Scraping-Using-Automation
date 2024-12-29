# Selenium Trending Topics Scraper

This project is a Python-based web scraping tool designed to scrape trending topics from X.com (formerly Twitter) using Selenium and store the data in a MongoDB database.

---

## Features

- Uses Selenium WebDriver to scrape trending topics.
- Supports proxy configuration for anonymity.
- Stores scraped data in MongoDB.

---

## Todo List

### **Setup & Environment**

1. [x] Install necessary Python libraries:
   - Selenium
   - Pymongo
   - Requests
   - Flask
2. [x] Configure environment variables:
   - `PROXY_USERNAME`
   - `PROXY_PASSWORD`
   - `PROXY_HOST`
   - `PROXY_PORT`
   - `MONGO_URI`
3. [x] Ensure `chromedriver` is installed and available in the system path and executable.

### **Selenium Integration**

4. [x] Setup Selenium WebDriver with:
   - Headless mode.
   - Proxy settings.
5. [x] Test and verify that the proxy works with Selenium.
6. [x] Ensure `WebDriverWait` and appropriate CSS selectors are used for dynamic content loading.

### **Scraping Logic**

7. [ ] Update CSS selectors for the trending topics on X.com:
   - Verify selectors manually using browser dev tools.
   - Add fallback selectors for robustness.
8. [x] Handle cases where no data is returned or blocked by X.com’s anti-bot measures.
9. [ ] Ensure proper error handling during scraping.
10. [ ] Implement logic to extract exactly **5 trending topics** and handle incomplete data gracefully.

### **Database Integration**

11. [x] Configure MongoDB connection using environment variables.
12. [x] Create a collection named `trends` in the `trending_topics` database.
13. [x] Store the scraped data with fields:
    - `nameoftrend1`, `nameoftrend2`, etc.
    - `date_time`
    - `ip_address`

### **Testing**

16. [x] Test scraping functionality on:
    - Proxied network.
    - Direct network without a proxy.
17. [ ] Validate the data stored in MongoDB.
18. [ ] Ensure the script gracefully handles edge cases:
    - No internet connection.
    - Proxy errors.
    - Website structure changes.
19. [ ] Verify the script collects trends reliably over multiple runs.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/3303mavihS/Web-Scraping-Using-Automation.git
   cd your-repo-name
   ```
