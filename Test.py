# First you must open the python console and enter:

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

first_name = 'Ricky'
last_name = 'Bobby'
address = '1234 Something Lane'
city = 'San Jose'
zipcode = '95112'
telephone_number = '408999999'
email = 'jondoe@gmail.com'


# Second you must specify the location of your browser executable.
# We will make the webdriver location a variable "browser"
# Make sure you have the webdriver for your browser downloaded.

browser = webdriver.Chrome(r'C:\Users\damie\Documents\GitHub\rouge_automated_checkout_bot\chromedriver')

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

checkout_button = browser.find_element_by_class_name('v-btn-checkout-button')
time.sleep(.5)
checkout_button.click()

# This should bring you to the checkout method screen. We will pick checkout as guest.
# Added delay for page to refresh fully.

checkout = 0
while checkout is not 1:
    checkout_guest = browser.find_element_by_xpath("//button[text()= 'Checkout as Guest']")
    checkout_guest.click()
    checkout = 1
else:
    time.sleep(.5)


# This should bring you to the shipping information page and autofill information you defined at beginning.

time.sleep(3)
first_name_field = browser.find_element_by_name('firstname')
first_name_field.send_keys(first_name)

last_name_field = browser.find_element_by_name('lastname')
last_name_field.send_keys(last_name)

address_field = browser.find_element_by_name('address')
address_field.send_keys(address)

city_field = browser.find_element_by_name('city')
city_field.send_keys(city)

state_field = browser.find_element_by_id('checkout:region_id')
state_field.send_keys('CA')
state_field.send_keys(Keys.ENTER)

zip_code_field = browser.find_element_by_name('zip')
zip_code_field.send_keys(zipcode)

telephone_field = browser.find_element_by_name('telephone')
telephone_field.send_keys(telephone_number)

email_done = 0
while email_done is not 1:
    email_field = browser.find_element_by_id('checkout:email')
    email_field.send_keys(email)
    email_done = 1
else:
    time.sleep(.5)

# The shipping page should be filled out now. Next we view shipping options.

shipping_option_button = browser.find_element_by_xpath("//button[text()= 'View Shipping Options']")
shipping_option_button.click()


















