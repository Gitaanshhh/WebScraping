# Web Scraping Examples

A collection of web scraping scripts using BeautifulSoup and Selenium in Python.

## Contents

- **`beautifulSoup.py`** - Basic HTML parsing with BeautifulSoup using local HTML file
- **`Selenium.py`** - Selenium WebDriver setup and basic usage
- **`LiveSite/sol.py`** - Live website scraping example (Alibaba sourcing data)
- **`index.html`** - Sample HTML file for testing BeautifulSoup

## Requirements

```bash
pip install beautifulsoup4 lxml requests selenium pandas
```

**Chrome Driver:** Download from [Chrome for Developers](https://developer.chrome.com/docs/chromedriver/downloads) (version 138.0.7204.94 or compatible with your Chrome version)

## Usage

1. **BeautifulSoup (Local HTML):**
   ```bash
   python beautifulSoup.py
   ```

2. **Selenium (Google):**
   ```bash
   python Selenium.py
   ```

3. **Live Site Scraping:**
   ```bash
   python LiveSite/sol.py
   ```

## Setup

- Ensure Chrome Driver is in your PATH or update the path in scripts
- Install required packages using pip
- Run scripts individually based on your needs

---
*Basic web scraping examples for learning purposes*
