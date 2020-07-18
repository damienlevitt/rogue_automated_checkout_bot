# First you must open the python console and enter:

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


# Second you must specify the location of your browser executable.
# We will make the webdriver location a variable "browser"
# Make sure you have the webdriver for your browser downloaded.

browser = webdriver.Chrome(r'C:\Users\damie\Documents\GitHub\rouge_automation_bot\chromedriver')

# Now you must specify your URL for your desired website using the 'get' function.

browser.get('https://www.roguefitness.com/rogue-calibrated-kg-steel-plates')

# Now we are going to find the field for the quantity wanted for the desired product.

quantity = browser.find_element_by_id('grouped-product-item-32811')

# Now we will use 'send_keys' to enter the desired amount into the text field.

quantity.send_keys('4')

# Now you will need to checkout by clicking add to cart. We will make the "add to cart" button an element.

add = browser.find_element_by_class_name('add-to-box')

# Now click the add element that was created.

add.click()

# The checkout page should appear, now we must click checkout.

checkout = browser.find_element_by_class_name('v-btn-checkout-button')

checkout.click()








