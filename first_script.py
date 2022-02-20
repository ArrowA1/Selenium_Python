# This is the very first script i wrote using Selenium
# It opens up a site, clicks on a dummy download button
# and waits till the download operation is completed

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# specify PATH for Selenium
os.environ['PATH'] += r"C:/Code/Selenium_Python/Drivers"

# start the browser
driver = webdriver.Edge()

# open the webpage
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

# wait for atmost 3 sec or until the target element loads
driver.implicitly_wait(8)   # is applied to every future element searches

# search for the required element
download_button = driver.find_element_by_id("downloadButton")
# element = driver.find_element(by = id, Value = "downloadButton")
download_button.click()

# Explicit wait to wait till download is completed
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "progress-label"),  # Element filtration
        "Complete!" # expected text
    )
)

# time.sleep(15)