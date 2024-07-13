# Google Search Results Scraper

Google Search Results Scraper is a Python-based tool that uses Selenium to automate Google searches and scrape the titles and URLs of the search results. The results are saved in an Excel file for easy access and analysis. This tool can be particularly useful for data collection, competitive analysis, or SEO research.

## Key Features

- **Automated Google Searches:** Perform Google searches programmatically.
- **Scraping Titles and URLs:** Extract titles and URLs from the search results.
- **Error Handling:** Gracefully handle page load errors, such as 404 or 500 status codes.
- **Duplicate Domain Filtering:** Avoid duplicate domains in the search results.
- **Headless Browser:** Use headless mode for running Chrome, making the tool suitable for server environments.
- **Customizable Output:** Save the results in an Excel file with a name based on the search query.

## Technologies Used

- **Python:** The core programming language used for the project.
- **Selenium:** For automating browser interactions.
- **pandas:** For handling data and exporting it to Excel.
- **requests:** For handling HTTP requests.
- **openpyxl:** For writing data to Excel files.

## Getting Started

### Prerequisites

- Python 3.x
- Google Chrome installed on your machine

### Requirements

- Selenium
- pandas
- requests
- Chrome WebDriver

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ValentynKrasnokutskyi/GoogleSearchResultsScraper.git
    cd GoogleSearchResultsScraper
    ```

2. Set up a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. Run the script:
    ```sh
    python google_scraper_v1.py
    ```

2. Enter your search query and the number of results when prompted.

### Example

When you run the script, you will be prompted to enter your search query and the number of results you want to scrape. The results will be saved in an Excel file with a name based on your search query, such as `buy_a_car_search_results.xlsx`.

### Troubleshooting

- If you encounter issues with ChromeDriver, ensure you have downloaded the correct version that matches your installed version of Google Chrome. Download the latest version from [this link](https://developer.chrome.com/docs/chromedriver/downloads).

## Contributions

Contributions are welcome! Whether it's bug fixes, feature additions, or documentation improvements, feel free to fork the repository and create a pull request. Please ensure that your changes align with the project's goals and maintain the existing coding standards.
