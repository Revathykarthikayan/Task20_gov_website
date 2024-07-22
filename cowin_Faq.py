
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pyautogui

import time
# initialis webdriver
driver = webdriver.Chrome()
driver.get("https://www.cowin.gov.in/")
actions = ActionChains(driver)

icon_create= driver.find_element(By.CLASS_NAME,"loginBtnMobile")
icon_create.click()
time.sleep(5)
# navigate to 'faq'

FAQ=driver.find_element(By.XPATH,"//a[text()=' FAQ']")
actions.context_click(FAQ).perform()
time.sleep(5)

pyautogui.typewrite(['down','down','enter'])
time.sleep(5)
print("Faq window is opened")

# navigation to 'partners'
partner=driver.find_element(By.XPATH,"//a[text()=' Partners']")
actions.context_click(partner).perform()
time.sleep(5)
pyautogui.typewrite(['down', 'down', 'enter'])
time.sleep(5)
print("Partners window is opened")

# switching between windows
window_handles = driver.window_handles      


partner_window_handle = None


for handle in window_handles:
    if handle != driver.current_window_handle:
        partner_window_handle = handle

        break
    # switching to partner window to get frame id
driver.switch_to.window(partner_window_handle)


time.sleep(5)

iframe = driver.find_element(By.TAG_NAME, 'iframe')

# Print the iframe ID 
iframe_id = iframe.get_attribute('id')
print(f'The ID of the iframe is: {iframe_id}')

time.sleep(5)


driver.quit()

