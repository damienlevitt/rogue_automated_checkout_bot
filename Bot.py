# Make sure to read the INSTRUCTIONS and fill in all the REQUIRED information below. I recommend taking a look at
# the README to ensure you have the correct libraries and necessary tools downloaded.

# After testing, it may be faster to have twilio send you the link for the item as soon as it is in stock and then
# Apple Pay is used to checkout.

# INSTRUCTIONS #
# First locate the line at the end of the script that says "browser = webdriver.Chrome(r'....').
# Replace the directory with the directory the chrome webdriver you have downloaded.
# Next, I recommend performing a test run of the script to ensure everything is functioning properly before continuing.
# After you have verified proper functionality, inspect the element on the webpage for the product you want and
# change the 5 digit number following 'grouped-product-item-xxxxx'. You can add multiple items as long as they
# are on the same page. Then change the URL to that of your desired product.
# You should run one last test to ensure functionality before entering personal information.
# Make sure to enter in all of the REQUIRED information below.

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client
import time
import os


# Info from Rogue Website
class WebpageInfo:
    #product = ('grouped-product-item-75745', 'grouped-product-item-75739', 'grouped-product-item-75741')    # REQUIRED
    #URL = 'https://www.roguefitness.com/rogue-add-on-change-plate-pair'                                     # REQUIRED
    URL = 'https://www.roguefitness.com/rogue-fleck-plates'
    product = ('grouped-product-item-85751', 'grouped-product-item-85749','grouped-product-item-85747', 'grouped-product-item-85745', 'grouped-product-item-85743', 'grouped-product-item-85741')


# Personal Checkout Info
class PersonalInfo:
    first_name = 'FIRSTNAME'                    # REQUIRED
    last_name = 'LASTNAME'                      # REQUIRED
    address = '1234 Something Lane'             # REQUIRED
    state = 'CA'                                # REQUIRED
    city = 'San Jose'                           # REQUIRED
    zipcode = '95219'                           # REQUIRED
    telephone_number = '4089999999'             # REQUIRED
    email = 'jondoe@gmail.com'                  # REQUIRED
    card_number = '4111111111111111'            # REQUIRED
    exp_month = '7'                             # REQUIRED
    exp_year = '2021'                           # REQUIRED
    cvv = '999'                                 # REQUIRED

# A twilio account is REQUIRED to opt-in for text message updates when your
# item is in stock. To enable, fill in the required information below with your twilio account ID, twilio auth token,
# twilio phone number, and the number where you want to receive the notifications.


def twilio_stock_alert():
    optin = False       # Change optin to True to get text updates with twilio.
    if optin is True:
        account_sid = 'TWILIO_ACCOUNT_ID'  # REQUIRED FOR TEXT ALERTS
        auth_token = 'TWILIO_AUTH_TOKEN'     # REQUIRED FOR TEXT ALERTS

        client = Client(account_sid, auth_token)
        client.messages.create(from_='TWILIO_PHONE_NUMBER',        # REQUIRED FOR TEXT ALERTS
                               to='CELL_PHONE_NUMBER',           # REQUIRED FOR TEXT ALERTS
                               body='One or more of the products you are watching are in stock. Proceeding to checkout.'
                               )
    return 0


def twilio_purchase_alert():
    optin = False       # Change optin to True to get text updates with twilio.
    if optin is True:
        account_sid = 'TWILIO_ACCOUNT_ID'      # REQUIRED FOR TEXT ALERTS
        auth_token = 'TWILIO_AUTH_TOKEN'         # REQUIRED FOR TEXT ALERTS

        client = Client(account_sid, auth_token)
        client.messages.create(from_='TWILIO_PHONE_NUMBER',            # REQUIRED FOR TEXT ALERTS
                               to='CELL_PHONE_NUMBER',               # REQUIRED FOR TEXT ALERTS
                               body='The Rogue Automated Checkout Bot has successfully completed.\n'
                                    'Please check email to verify purchase, thank you for using.\n'
                                    ''
                               )
    return 0


def reddit_restock_post():
    thread = 'https://www.reddit.com/r/homegym/comments/hx101e/stock_and_shipping_thread_24_july_2020/'
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {'profile.default_content_setting_values.notifications': 2})
    driver2 = webdriver.Chrome(chrome_options=chrome_options)
    driver2.get(thread)
    login = driver2.find_element_by_css_selector(
        '#SHORTCUT_FOCUSABLE_DIV > div:nth-child(4) > div > div._1npCwF50X2J7Wt82SZi6J0._3OGqXkiUb_0ZMlksb26boO > div.u35lf2ynn4jHsVUwPmNU.Dx3UxiK86VcfkFQVHNXNi._3KaECfUAGLfWQPO5eNjMNl > div.uI_hDmU5GSiudtABRz_37 > div._2GTMVdV2t3ka_zfkVHHo95 > a._1HunhFR-0b-AYs0WG9mU_P._3fM1M9rFBqKwfG-KJLnxPY._2nelDm85zKKmuD94NequP0')
    login.click()
    time.sleep(.2)
    login_frame = WebDriverWait(driver2, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[3]/div[2]/div/iframe')))
    driver2.switch_to.frame(login_frame)
    username = driver2.find_element_by_css_selector('#loginUsername')
    username.send_keys('USERNAME')
    password = driver2.find_element_by_css_selector('#loginPassword')
    password.send_keys('PASSWORD')
    login_button = driver2.find_element_by_css_selector('body > div > div > div.PageColumn.PageColumn__right > div > form > div.Onboarding__step.narrow > fieldset:nth-child(17) > button')
    login_button.click()
    driver2.switch_to.default_content()
    textbox = WebDriverWait(driver2, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#SHORTCUT_FOCUSABLE_DIV > div:nth-child(4) > div > div > div > div._3ozFtOe6WpJEMUtxDOIvtU > div._1vyLCp-v-tE5QvZovwrASa > div._1OVBBWLtHoSPfGCRaPzpTf._3nSp9cdBpqL13CqjdMr2L_._2udhMC-jldHp_EpAuBeSR1.PaJBYLqPf_Gie2aZntVQ7 > div.uI_hDmU5GSiudtABRz_37 > div._1r4smTyOEZFO91uFIdWW6T.aUM8DQ_Nz5wL0EJc_wte6 > div:nth-child(2) > div > div > div._2baJGEALPiEMZpWB2iWQs7 > div > div:nth-child(1) > div > div > div')))
    textbox.send_keys('Flecks in stock, go. https://www.roguefitness.com/rogue-fleck-plates')
    comment_button = driver2.find_element_by_css_selector('#SHORTCUT_FOCUSABLE_DIV > div:nth-child(4) > div > div > div > div._3ozFtOe6WpJEMUtxDOIvtU > div._1vyLCp-v-tE5QvZovwrASa > div._1OVBBWLtHoSPfGCRaPzpTf._3nSp9cdBpqL13CqjdMr2L_._2udhMC-jldHp_EpAuBeSR1.PaJBYLqPf_Gie2aZntVQ7 > div.uI_hDmU5GSiudtABRz_37 > div._1r4smTyOEZFO91uFIdWW6T.aUM8DQ_Nz5wL0EJc_wte6 > div:nth-child(2) > div > div > div._17TqawK-44tH0psnHPIhzS.RQTXfVRnnTF5ont3w58rx > div._3SNMf5ZJL_5F1qxcZkD0Cp > button')
    comment_button.click()


def webpage_status(browser):
    browser.get(WebpageInfo.URL)
    update = 0
    print("\nChecking Webpage Status...\n")
    while update == 0:                              # Condition for if page is updated.
        for x in WebpageInfo.product:
            try:
                element = browser.find_element_by_id(x)
                # availability = browser.find_element_by_class_name('availability')
                if element.is_displayed() is True: # and availability.is_displayed() is False:
                    update = 1
                    break
            except:
                pass
        if update is 1:
            break
        browser.refresh()
        time.sleep(20)   # This is the page refresh frequency in seconds. Don't refresh too often or you risk an IP ban.
    print("One or more target products in stock, proceeding to checkout.\n")
    twilio_stock_alert()
    return browser

# def rouge_checkout_barbell(browser):


def rogue_checkout_plates(browser):
    done = 0
    for i in WebpageInfo.product:
        try:
            quantity = browser.find_element_by_id(i)

            # Change this to your desired quantity for each product (default is one).
            quantity.send_keys('1')                       # REQUIRED
        except:
            print("item", i, "was not in stock")
            pass        # Will move on to the next item if one of the items is not in stock

    add = browser.find_element_by_class_name('add-to-box')          # Find add to cart element on page.
    add.click()                                                     # Click add to cart.
    main_checkout(browser)

def rouge_checkout_box_select(browser):


def main_checkout(browser):
# The checkout page should appear
#     if WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#side-cart > div > div.cart-messages-container > div > div'))):
#         return done is False        # Checks if there is an error message when adding items to cart.

    # Finds checkout element on the side cart.
    checkout = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#side-cart > div > div.off-canvas-footer > div:nth-child(1) > div.v-col-8 > button')))
    checkout.click()        # Clicks checkout element.

    # Find checkout as guest element and click.
    checkout_guest = browser.find_element_by_xpath("//button[text()= 'Checkout as Guest']")
    checkout_guest.click()

    # Autofill information defined in Personal Info.

    first_name_field = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.NAME, 'firstname')))
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

    # One paused needed for view shipping option to become clickable.
    time.sleep(1)

    # Find and click the view shipping options button.
    view_shipping_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[text()= "View Shipping Options"]')))
    view_shipping_button.click()

    # Find and click the confirm shipping button.
    confirm_ship_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[text()= "Continue with this address"]')))
    confirm_ship_button.click()

    # Find and click the continue to payment button.
    continue_to_payment_button = browser.find_element_by_xpath("//button[text()= 'Continue to Payment']")
    continue_to_payment_button.click()

    # Changes iframe to that of credit card number element location.
    curr_frame = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//iframe[@src="https://core.spreedly.com/v1/embedded/number-frame.html?v=1.51"]')))

    # Selects and fills the card number section from the Personal Info.
    browser.switch_to.frame(curr_frame)
    card_number_field = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'card_number')))
    card_number_field.send_keys(PersonalInfo.card_number)

    # Switches browser out of the credit card iframe. Needs to be done to locate the iframe for the cvv.
    browser.switch_to.default_content()

    # Switches to the iframe for the cvv then fills with information from Personal Info.
    curr_frame = browser.find_element_by_xpath(
        '//iframe[@src="https://core.spreedly.com/v1/embedded/cvv-frame.html?v=1.51"]')
    browser.switch_to.frame(curr_frame)
    cvv_field = browser.find_element_by_id('cvv')
    cvv_field.send_keys(PersonalInfo.cvv)

    # Switches back out of the cvv iframe to the default body.
    browser.switch_to.default_content()

    expire_month_field = browser.find_element_by_id('expirationmonth')
    expire_month_field.send_keys(PersonalInfo.exp_month)

    expire_year_field = browser.find_element_by_id('expirationyear')
    expire_year_field.send_keys(PersonalInfo.exp_year)

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

    twilio_purchase_alert()
    if done is 1:
        print("\nThe bot successfully placed an order, check your email to verify.\n"
              "Thank you for using my Rogue Automated Checkout Bot, hope it helped you, happy lifting!")


if __name__ == '__main__':
    driver = webdriver.Chrome(r'C:\Users\damie\Documents\GitHub\Rogue_automated_checkout_bot\chromedriver')
    webpage_status(driver)
    #rogue_checkout_plates(driver)
    reddit_restock_post()

