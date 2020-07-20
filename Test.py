# This script requires you find the product item number of the desired item.
# This can be done by inspecting the item in chrome and replacing the 5 digit number with that of your desired product.
# The URL must be changed to the location of the desired product page.

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Info from Rogue Website
product = 'grouped-product-item-35913'
URL = 'https://www.roguefitness.com/rogue-kg-fractional-plates'


# Personal Checkout Info
first_name = 'Ricky'
last_name = 'Bobby'
address = '1234 Something Lane'
state = 'CA'
city = 'San Jose'
zipcode = '95219'
telephone_number = '408999999'
email = 'jondoe@gmail.com'
card_number = '4111111111111111'
exp_month = '2'
exp_year = '2021'
cvv = '201'


# Second you must specify the location of your browser executable.
# We will make the webdriver location a variable "browser"
# Make sure you have the webdriver for your browser downloaded.

def browser_init():
    browser = webdriver.Chrome(r'C:\Users\damie\Documents\GitHub\rouge_automated_checkout_bot\chromedriver')
    browser.get(URL)
    return browser

# Now we are going to find the field for the quantity wanted for the desired product.
if __name__ == '__main__':

    browser = browser_init()
    quantity = browser.find_element_by_id(product)

# Now we will use 'send_keys' to enter the desired amount into the text field.

    quantity.send_keys('4')

# Now you will need to checkout by clicking add to cart. We will make the "add to cart" button an element.

    add = browser.find_element_by_class_name('add-to-box')

# Now click the add element that was created.

    add.click()

# The checkout page should appear, now we must click checkout.

    checkout = browser.find_element_by_class_name('v-btn-checkout-button')
    time.sleep(.5)
    checkout.click()

# This should bring you to the checkout method screen. We will pick checkout as guest.

    checkout_guest = browser.find_element_by_xpath("//button[text()= 'Checkout as Guest']")
    checkout_guest.click()

    # This should bring you to the shipping information page and autofill information you defined at beginning.

    time.sleep(5)
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

    email_field = browser.find_element_by_id('checkout:email')
    email_field.send_keys(email)
    time.sleep(10)

    shipping_page_button = browser.find_element_by_xpath('//button[text()= "View Shipping Options"]')
    shipping_page_button.click()
    time.sleep(7)

    confirm_ship_button = browser.find_element_by_xpath("//button[text()= 'Continue with this address']")
    confirm_ship_button.click()

    continue_to_payment_button = browser.find_element_by_xpath("//button[text()= 'Continue to Payment']")
    continue_to_payment_button.click()
    time.sleep(5)

    curr_frame = browser.find_element_by_xpath(
        '//iframe[@src="https://core.spreedly.com/v1/embedded/number-frame.html?v=1.49"]')
    browser.switch_to.frame(curr_frame)
    card_number_field = browser.find_element_by_id('card_number')
    card_number_field.send_keys(card_number)

    browser.switch_to.default_content()

    curr_frame = browser.find_element_by_xpath(
        '//iframe[@src="https://core.spreedly.com/v1/embedded/cvv-frame.html?v=1.49"]')
    browser.switch_to.frame(curr_frame)
    cvv_field = browser.find_element_by_id('cvv')
    cvv_field.send_keys(cvv)

    browser.switch_to.default_content()

    expire_month_field = browser.find_element_by_id('expirationmonth')
    expire_month_field.send_keys(exp_month)

    expire_year_field = browser.find_element_by_id('expirationyear')
    expire_year_field.send_keys(exp_year)

    time.sleep(.5)
    review_button = browser.find_element_by_xpath('//button[text()= "Continue to Review"]')
    review_button.click()

    time.sleep(2)

    place_order_button = browser.find_element_by_css_selector("#checkout > div > div.funneled-layout-content > div:nth-child(2) > div.add-shipping-address-container > div > div.main-checkout-col.main-checkout-col-right > button")
    place_order_button.click()
