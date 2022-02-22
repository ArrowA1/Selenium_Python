# A simple script to fill keys into an input field in a webpage
# And click on a button using css selectors


import os   # to use environ to set PATH for Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys   # to use keyboard keys such as Shift/Enter

# Specify PATH for Selenium
os.environ['PATH'] += r"C:/Code/Selenium_Python/Drivers"

# Launch the browser
driver = webdriver.Edge()

# load the webpage
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(5)

# in case of sudden pop-ups
try:
    # locate the "no button" and click on it
    no_button = driver.find_element_by_class_name("at-cm-no-button")
    no_button.click()
    print("\nA pop-up window was just closed. Success\n")

except:
    print("\nNo element with this class name was found. Skipping....\n")

# get the input fields
sum1 = driver.find_element_by_id("sum1")
sum2 = driver.find_element_by_id("sum2")

# send values/keys in input fields
sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)  # sum1.send_keys(15)
sum2.send_keys(Keys.NUMPAD2, Keys.NUMPAD5)  # sum1.send_keys(25)

# find and click on the "get total" button using class name   DOES NOT WORK
try:
    # locate the "get total" button and click on it
    total_button = driver.find_element_by_class_name("btn-default")
    total_button.click()

except:
    print("No element with this class name was found. Skipping....")

# find and click on the "get total" button using css selector  WORKS!!!!
total_button = driver.find_element_by_css_selector("button[onclick='return total()']")
total_button.click()

# get the total value from the page
value = driver.find_element_by_id("displayvalue")
print(value.text)
