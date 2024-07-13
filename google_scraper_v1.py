import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, WebDriverException
from urllib.parse import urlparse
import time
import re
import os


def google_search(query, num_results, driver):
    # Perform a Google search with the specified query and number of results
    driver.get(f"https://www.google.com/search?q={query}&num={num_results}")
    WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div.yuRUbf a')))
    time.sleep(5)  # Allow more time for all results to load

    links = driver.find_elements(By.CSS_SELECTOR, 'div.yuRUbf a')
    urls = [link.get_attribute("href") for link in links if link.get_attribute("href") and 'http' in link.get_attribute("href")]
    urls = [url for url in urls if 'translate.google.com' not in url]  # Exclude Google Translate links

    unique_domains = set()
    unique_urls = []
    for url in urls:
        domain = urlparse(url).netloc
        if domain not in unique_domains:
            unique_domains.add(domain)
            unique_urls.append(url)

    return unique_urls[:num_results]


def get_page_title(url, driver):
    # Get the title of the specified URL
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        return f"Page load error: {http_err.response.status_code}"
    except requests.exceptions.RequestException as req_err:
        return f"Page load error: {req_err}"

    try:
        driver.set_page_load_timeout(15)
        driver.get(url)
        WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.TAG_NAME, 'title')))
        return driver.title
    except TimeoutException:
        return "Page load error (timeout)"
    except WebDriverException as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    # Input from the user
    query = input("Enter your search query: ")
    num_results = int(input("Enter the number of results you want: "))
    driver_path = os.path.join(os.getcwd(), 'chromedriver.exe')

    # Set up Chrome options for headless mode
    options = ChromeOptions()
    options.headless = True
    service = ChromeService(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        urls = google_search(query, num_results, driver)

        print(f'Found {len(urls)} URLs:')
        for url in urls:
            print(url)

        data = []
        for url in urls:
            title = get_page_title(url, driver)
            data.append({'Title': title, 'URL': url})
            print(f'Title: {title}, URL: {url}')

        # Create DataFrame and save to Excel
        df = pd.DataFrame(data)

        # Format the file name
        query_safe = re.sub(r'\W+', '_', query)  # Replace all non-alphanumeric characters with "_"
        file_name = f'{query_safe}_search_results.xlsx'

        # Check if file exists and remove it if necessary
        if os.path.exists(file_name):
            os.remove(file_name)

        df.to_excel(file_name, index=False)
        print(f'Results have been saved to "{file_name}".')

    finally:
        driver.quit()


if __name__ == '__main__':
    main()
