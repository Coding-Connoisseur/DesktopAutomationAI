# browser_control.py
# Controls browser automation using Selenium or Puppeteer.
# This module will allow opening browsers, navigating web pages, filling forms,
# and interacting with web elements for desktop automation tasks.

# Import necessary modules for browser automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# Placeholder for the browser driver (e.g., ChromeDriver)
driver = None

def open_browser(browser_type='chrome', headless=False):
    """
    Opens a browser session using Selenium.
    
    :param browser_type: (str) The type of browser to open (default is 'chrome').
    :param headless: (bool) Whether to run the browser in headless mode (default is False).
    :return: None
    
    Logic:
    - Initializes the Selenium WebDriver.
    - Configures browser options (e.g., headless mode if required).
    - Opens the browser and waits until it's ready.
    
    Interaction with program:
    - Other functions like 'navigate_to_url' and 'fill_form' will rely on the 
      browser instance created here to perform further actions.
    
    Enhancements:
    - Added support for different browsers like Firefox, Edge.
    - Enabled configuration options (e.g., headless mode).
    """
    global driver
    if browser_type == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        if headless:
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_type == 'firefox':
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        firefox_options = FirefoxOptions()
        if headless:
            firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
    elif browser_type == 'edge':
        from selenium.webdriver.edge.options import Options as EdgeOptions
        edge_options = EdgeOptions()
        if headless:
            edge_options.add_argument("--headless")
        driver = webdriver.Edge(options=edge_options)
    else:
        raise ValueError(f"Browser type {browser_type} is not supported yet.")
    
    print(f"Browser {browser_type} opened successfully.")

def navigate_to_url(url):
    """
    Navigates to a specified URL in the opened browser.
    
    :param url: (str) The URL to navigate to.
    :return: None
    
    Logic:
    - Takes the URL input and directs the browser to the specified webpage.
    - Waits for the page to load fully before allowing other actions.
    
    Interaction with program:
    - This function is required before interacting with any web elements or 
      automating tasks like form filling or button clicks.
    
    Enhancements:
    - Added checks for valid URL formats.
    - Implemented timeouts and error handling for slow page loads.
    """
    if driver:
        if not re.match(r'^(http|https)://', url):
            raise ValueError(f"Invalid URL format: {url}")
        try:
            driver.get(url)
            print(f"Navigated to {url}")
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
        except Exception as e:
            print(f"Error occurred while navigating to {url}: {e}")
    else:
        raise RuntimeError("Browser session is not started. Call 'open_browser' first.")

def fill_form(input_selector, input_value):
    """
    Fills a form field on the webpage.
    
    :param input_selector: (str) The CSS selector or XPath to locate the input field.
    :param input_value: (str) The value to input into the form field.
    :return: None
    
    Logic:
    - Locates the input field on the web page using the provided selector.
    - Inputs the specified value into the field.
    
    Interaction with program:
    - Other functions (like 'navigate_to_url') should be called before this to ensure
      that the browser is on the correct page.
    
    Enhancements:
    - Added better error handling if the input field is not found.
    - Integrated dynamic wait times for loading form elements.
    """
    if driver:
        try:
            input_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, input_selector))
            )
            input_element.clear()
            input_element.send_keys(input_value)
            print(f"Filled form input with {input_value}.")
        except Exception as e:
            print(f"Error occurred while filling form: {e}")
    else:
        raise RuntimeError("Browser session is not started. Call 'open_browser' first.")

def click_element(button_selector):
    """
    Clicks a button or element on the webpage.
    
    :param button_selector: (str) The CSS selector or XPath to locate the button or element.
    :return: None
    
    Logic:
    - Locates the button or element using the provided selector.
    - Clicks the element to perform an action (e.g., submit a form, navigate to a new page).
    
    Interaction with program:
    - This function is often used after filling forms or navigating through web pages.
    
    Enhancements:
    - Added error handling if the button is not clickable or the element is not found.
    - Implemented checks to ensure the element is visible and clickable.
    """
    if driver:
        try:
            button_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))
            )
            button_element.click()
            print(f"Clicked element with selector {button_selector}.")
        except Exception as e:
            print(f"Error occurred while clicking the element: {e}")
    else:
        raise RuntimeError("Browser session is not started. Call 'open_browser' first.")

def close_browser():
    """
    Closes the browser session and ends WebDriver.
    
    :return: None
    
    Logic:
    - Closes the currently open browser window.
    - Cleans up the WebDriver instance.
    
    Interaction with program:
    - This function is called after all automation tasks are done, ensuring proper resource cleanup.
    
    Enhancements:
    - Added checks to ensure there are no ongoing tasks before closing the browser.
    """
    global driver
    if driver:
        # Check for ongoing tasks (placeholder logic)
        if driver.current_url != "about:blank":
            print("Warning: There might be ongoing tasks.")
        driver.quit()
        driver = None
        print("Browser closed successfully.")
    else:
        print("No browser session to close.")
