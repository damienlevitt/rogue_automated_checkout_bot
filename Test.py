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
#product = ('grouped-product-item-75737', 'grouped-product-item-75739', 'grouped-product-item-75741')
product = ('grouped-product-item-85751', 'grouped-product-item-85749', 'grouped-product-item-85745', 'grouped-product-item-85743', 'grouped-product-item-85741')
# URL = 'https://www.roguefitness.com/rogue-add-on-change-plate-pair'
URL = 'https://www.roguefitness.com/rogue-fleck-plates'


# Personal Checkout Info
first_name = 'FIRSTNAME'
last_name = 'LASTNAME'
address = '1234 Something Lane'
state = 'CA'
city = 'San Jose'
zipcode = '95219'
telephone_number = '4089999999'
email = 'jondoe@gmail.com'
card_number = '4111111111111111'
exp_month = '7'
exp_year = '2021'
cvv = '999'


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
    for i in product:
        try:
            quantity = browser.find_element_by_id(i)
            quantity.send_keys('1')
        except:
            print("item", i, "was not in stock")
            pass        # Will move on to the next item if one of the items is not in stock

# Now we will use 'send_keys' to enter the desired amount into the text field.

    # quantity.send_keys('1')

# Now you will need to checkout by clicking add to cart. We will make the "add to cart" button an element.

    add = browser.find_element_by_class_name('add-to-box')

# Now click the add element that was created.

    add.click()

# The checkout page should appear, now we must click checkout.

    checkout = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#side-cart > div > div.off-canvas-footer > div:nth-child(1) > div.v-col-8 > button')))
    # checkout = browser.find_element_by_class_name('v-btn-checkout-button')
    # time.sleep(.5)      Optimized to avoid waiting by using wait until element clickable
    checkout.click()

# This should bring you to the checkout method screen. We will pick checkout as guest.

    checkout_guest = browser.find_element_by_xpath("//button[text()= 'Checkout as Guest']")
    checkout_guest.click()

    # This should bring you to the shipping information page and autofill information you defined at beginning.

    # time.sleep(5)
    first_name_field = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.NAME, 'firstname')))
    # first_name_field = browser.find_element_by_name('firstname')
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
    time.sleep(1)

    view_shipping_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[text()= "View Shipping Options"]')))
    # view_shipping_button = browser.find_element_by_xpath('//button[text()= "View Shipping Options"]')
    view_shipping_button.click()
    # time.sleep(7)

    confirm_ship_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[text()= "Continue with this address"]')))
    # confirm_ship_button = browser.find_element_by_xpath("//button[text()= 'Continue with this address']")
    confirm_ship_button.click()

    continue_to_payment_button = browser.find_element_by_xpath("//button[text()= 'Continue to Payment']")
    continue_to_payment_button.click()
    # time.sleep(5)

    curr_frame = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//iframe[@src="https://core.spreedly.com/v1/embedded/number-frame.html?v=1.49"]')))
    # curr_frame = browser.find_element_by_xpath(
    #     '//iframe[@src="https://core.spreedly.com/v1/embedded/number-frame.html?v=1.49"]')
    browser.switch_to.frame(curr_frame)

    card_number_field = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'card_number')))
    #card_number_field = browser.find_element_by_id('card_number')
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

    # time.sleep(.5)
    review_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[text()= "Continue to Review"]')))
    # review_button = browser.find_element_by_xpath('//button[text()= "Continue to Review"]')
    review_button.click()

    # time.sleep(2)
    place_order_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout > div > div.funneled-layout-content > div:nth-child(2) > div.add-shipping-address-container > div > "
        "div.main-checkout-col.main-checkout-col-right > button")))
    # place_order_button = browser.find_element_by_css_selector(
    #     "#checkout > div > div.funneled-layout-content > div:nth-child(2) > div.add-shipping-address-container > div > "
    #     "div.main-checkout-col.main-checkout-col-right > button")
    place_order_button.click()
