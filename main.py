from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver =webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

time.sleep(3)
login=driver.find_element(By.LINK_TEXT,value='Log in')
login.click()

time.sleep(5)
more_options=driver.find_element(By.XPATH,value='//*[@id="o672545042"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button')
more_options.click()

time.sleep(5)
login_facbook=driver.find_element(By.XPATH,value='//*[@id="o672545042"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
login_facbook.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(2)
email=driver.find_element(By.XPATH,value='//*[@id="email"]')
email.send_keys("Your id")


time.sleep(2)
password=driver.find_element(By.XPATH,value='//*[@id="pass"]')
password.send_keys("your password")

final_login=driver.find_element(By.ID,value='loginbutton')
final_login.click()
time.sleep(10)

driver.switch_to.window(base_window)
time.sleep(5)


allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

for n in range(100):

    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
