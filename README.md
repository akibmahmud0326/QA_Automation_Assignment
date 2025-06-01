# 🛒 Amazon Automation Bot using Selenium

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen)
![Chrome](https://img.shields.io/badge/Browser-Chrome-yellow)

---

## 📌 Overview

This project is a simple web automation script using **Selenium** that opens [Amazon.com](https://www.amazon.com), waits for 5 seconds, and prints out:

- The webpage **title**
- The **current URL**
- The **browser name**

It uses `webdriver-manager` to automatically manage ChromeDriver installation, so you don't need to download it manually.

---

## 🚀 Features

- ✅ Launches Amazon.com automatically  
- 🕒 Waits 5 seconds for the page to load  
- 🧾 Prints title, URL, and browser name  
- 🔧 No manual ChromeDriver setup required  

---

## 🧰 Technologies Used

- Python 3.10+
- Selenium
- Webdriver Manager
- Google Chrome

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/amazon-automation.git
cd amazon-automation
```

### 2. Install dependencies

```bash
pip install selenium webdriver-manager
```

---

## ▶️ Usage

Simply run the script:

```bash
python main.py
```

Expected Output:

```
Amazon.com. Spend less. Smile more.
https://www.amazon.com/
chrome
```

---

## 🧪 Sample Code

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com")
time.sleep(5)

print(driver.title)
print(driver.current_url)
print(driver.name)
```

---

## 🙋‍♂️ Author

**Akib Mahmud**

- GitHub: [@akibmahmud0326](https://github.com/your-username)
- Email: akibmahmudabcd@gmail.com

---

## 🌐 Connect

If you find this useful, please ⭐ the repo and share!

