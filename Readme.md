# Trending Topics Scraper

This project is a Python-based web scraping tool designed to extract trending topics from **X.com** (formerly Twitter). The scraped data is stored in a **MongoDB database** for further use or analysis. The project uses **Selenium** for web scraping and supports the use of proxies for anonymity.

---

## What Does This Project Do?

1. Scrapes the top 5 trending topics from **X.com**.
2. Stores the extracted data into a **MongoDB database**.
3. Logs all activities and errors for better debugging and tracking.
4. Uses a proxy for scraping to avoid IP bans or restrictions.

---

## Tools and Libraries Used

### **Libraries**

- **Selenium**: For web scraping dynamic web pages.
- **Pymongo**: For interacting with the MongoDB database.
- **Flask**: Web framework to build a simple web app.
- **Requests**: For making HTTP requests (e.g., fetching public IP address).
- **Logging**: For generating debug logs.

### **Tools**

- **ChromeDriver**: To run Selenium for scraping.
- **MongoDB Atlas**: Cloud-based NoSQL database for storing data.
- **ProxyMesh**: Proxy service to avoid being blocked by X.com.

---

## Prerequisites

Before running the project, make sure you have the following installed:

1. **Python 3.8+**
2. **Google Chrome** (latest version)
3. **ChromeDriver** (compatible with your Chrome version)
4. **MongoDB Atlas** (or local MongoDB installation)

---

## Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/3303mavihS/Web-Scraping-Using-Automation.git
cd Web-Scraping-Using-Automation
```

### Step 2: Configure Environment Variables

```bash
MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/test
EMAIL=your_email@example.com
USERNAME=your_x_username
PASSWORD=your_x_password
PROXY_USERNAME=your_proxy_username
PROXY_PASSWORD=your_proxy_password
PROXY_HOST=your_proxy_host
PROXY_PORT=your_proxy_port
```

### Step 3: Download ChromeWebDriver and the libraries mentioned above

Visit the ChromeDriver Downloads page.
Download the version matching your installed Google Chrome version.
Place the chromedriver executable in /usr/local/bin (for macOS/Linux) or add its path to your system's environment variables (for Windows).

### Step 4: Running the Web App

```bash
python3 app.py
```

Visit http://127.0.0.1:5000/ in your browser to see the scraped data.

Troubleshooting
ChromeDriver Issues: Make sure the version of ChromeDriver matches your installed Chrome browser version. If there is a mismatch, download the correct version from ChromeDriver Downloads.
MongoDB Connection Issues: Ensure your MongoDB URI in the .env file is correct and your MongoDB instance (either local or Atlas) is running.
Contributing
Feel free to fork the repository, make improvements, and submit pull requests. Contributions are always welcome!

### Demonstration

<video controls>
  <source src="demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
