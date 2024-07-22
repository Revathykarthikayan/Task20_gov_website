import os
import shutil
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


# Set the default download directory
cd = os.getcwd()
download_dir = cd+"\\Notes\\"
if os.path.exists(download_dir):
    shutil.rmtree(download_dir)
    os.mkdir(download_dir)
else:
    os.mkdir(download_dir)


chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "plugins.always_open_pdf_externally": True,
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,  # Disable prompt for download
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
chrome_options.add_argument("--safebrowsing-disable-download-protection")
chrome_options.add_argument("safebrowsing-disable-extension-blacklist")


# Initialize Chrome WebDriver with options
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


# Open the website
driver.get("https://labour.gov.in/")


# Click on "Monthly Progress Report" link
try:
    action = ActionChains(driver)
    # identify element
    documents = driver.find_element(By.XPATH, "//a[normalize-space()='Documents']")
    # hover over element
    action.move_to_element(documents).perform()


    monthly_progress_link = WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Monthly Progress Report")]'))
    )
    monthly_progress_link.click()


    # Click on the download link for a specific report 
   
    download_link = driver.find_element(By.LINK_TEXT, 'Download(190.44 KB)')
    download_link.click()



    # Accept the alert 
    pyautogui.press('enter')
    time.sleep(5)


except TimeoutException:
    print("timeout exception")

driver.quit()