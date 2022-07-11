from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

FACEBOOK_ID = 'myfacebooklogin@gmail.com'
PASSWORD = 'myfacebooklogin'

URL = 'https://bumble.com/app'
CHROME_DRIVER_PATH = 'C:\\PATH\\chromedriver.exe'

driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
main_window_handle = driver.current_window_handle

driver.get(URL)
driver.maximize_window()
time.sleep(5)

# click facebook login button
login = driver.find_element(By.CSS_SELECTOR, '.form__actions .button')
login.click()
time.sleep(3)

## Switch to pop-up window
for handle in driver.window_handles:
    if handle != main_window_handle:
        facebook_handle = handle

driver.switch_to.window(facebook_handle)

email = driver.find_element(By.NAME, 'email')
email.send_keys(FACEBOOK_ID)
time.sleep(3)

email = driver.find_element(By.NAME, 'pass')
email.send_keys(PASSWORD)
time.sleep(3)

login_button = driver.find_element(By.ID, 'loginbutton')
login_button.click()
time.sleep(5)

## Switch back to bumble window
driver.switch_to.window(main_window_handle)


while True:
    try:
        like_button = driver.find_element(By.CSS_SELECTOR, '.encounters-action--like')
        like_button.click()
        time.sleep(3)
    except:
        print('Swipe limit encountered.')
        break

    try:
        continue_button = driver.find_element(By.CSS_SELECTOR, '.encounters-match__cta-action .button')
        continue_button.click()
    except:
        continue

driver.quit()
