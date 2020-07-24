# This script requires you find the product item number of the desired item.
# This can be done by inspecting the item in chrome and replacing the 5 digit number with that of your desired product.
# The URL must be changed to the location of the desired product page.

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


# Info from Rogue Website
class WebpageInfo:
    product = ('grouped-product-item-75745', 'grouped-product-item-75739', 'grouped-product-item-75741')
    #product = ('grouped-product-item-85751', 'grouped-product-item-85749', 'grouped-product-item-85745', 'grouped-product-item-85743', 'grouped-product-item-85741')
    URL = 'https://www.roguefitness.com/rogue-add-on-change-plate-pair'
    #URL = 'https://www.roguefitness.com/rogue-fleck-plates'


# Personal Checkout Info
class PersonalInfo:
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

def webpage_status(browser):
    browser.get(WebpageInfo.URL)
    update = 0
    while update == 0:                              #Condition for if page is updated.
        for x in WebpageInfo.product:
            try:
                element = browser.find_element_by_id(x)
                # availability = browser.find_element_by_class_name('availability')
                if element.is_displayed() is True: #and availability.is_displayed() is False:
                    update = 1
                    break
            except:
                pass
        if update is 1:
            break
        browser.refresh()
        time.sleep(25)          #This is the page refresh frequency in seconds. Don't refresh too often or you risk and IP ban.
    return browser


def rouge_checkout(browser):
    done = 0
    for i in WebpageInfo.product:
        try:
            quantity = browser.find_element_by_id(i)
            quantity.send_keys('1')                        # Change this to your desired quantity for each product
        except:
            print("item", i, "was not in stock")
            pass        # Will move on to the next item if one of the items is not in stock

# Now you will need to checkout by clicking add to cart. We will make the "add to cart" button an element.

    add = browser.find_element_by_class_name('add-to-box')

# Now click the add element that was created.

    add.click()

# The checkout page should appear, now we must click checkout.
#     if WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#side-cart > div > div.cart-messages-container > div > div'))):
#         return done is False        # Checks if there is an error message when adding items to cart.

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
    first_name_field.send_keys(PersonalInfo.first_name)

    last_name_field = browser.find_element_by_name('lastname')
    last_name_field.send_keys(PersonalInfo.last_name)

    address_field = browser.find_element_by_name('address')
    address_field.send_keys(PersonalInfo.address)

    city_field = browser.find_element_by_name('city')
    city_field.send_keys(PersonalInfo.city)

    state_field = browser.find_element_by_id('checkout:region_id')
    state_field.send_keys('CA')
    state_field.send_keys(Keys.ENTER)

    zip_code_field = browser.find_element_by_name('zip')
    zip_code_field.send_keys(PersonalInfo.zipcode)

    telephone_field = browser.find_element_by_name('telephone')
    telephone_field.send_keys(PersonalInfo.telephone_number)

    email_field = browser.find_element_by_id('checkout:email')
    email_field.send_keys(PersonalInfo.email)
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
        (By.XPATH, '//iframe[@src="https://core.spreedly.com/v1/embedded/number-frame.html?v=1.50"]')))
    # curr_frame = browser.find_element_by_xpath(
    #     '//iframe[@src="https://core.spreedly.com/v1/embedded/number-frame.html?v=1.49"]')
    browser.switch_to.frame(curr_frame)

    card_number_field = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'card_number')))
    #card_number_field = browser.find_element_by_id('card_number')
    card_number_field.send_keys(PersonalInfo.card_number)

    browser.switch_to.default_content()

    curr_frame = browser.find_element_by_xpath(
        '//iframe[@src="https://core.spreedly.com/v1/embedded/cvv-frame.html?v=1.50"]')
    browser.switch_to.frame(curr_frame)
    cvv_field = browser.find_element_by_id('cvv')
    cvv_field.send_keys(PersonalInfo.cvv)

    browser.switch_to.default_content()

    expire_month_field = browser.find_element_by_id('expirationmonth')
    expire_month_field.send_keys(PersonalInfo.exp_month)

    expire_year_field = browser.find_element_by_id('expirationyear')
    expire_year_field.send_keys(PersonalInfo.exp_year)

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
    done = 1

    if done is 1:
        print("\nThe bot successfully placed an order, check your email to verify.\n"
              "Thank you for using my Rouge Automated Checkout Bot, hope it helped you, happy lifting!")

if __name__ == '__main__':
    browser = webdriver.Chrome(r'C:\Users\damie\Documents\GitHub\rouge_automated_checkout_bot\chromedriver')
    # while done is False:
    webpage_status(browser)
    rouge_checkout(browser)

