import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Set the default download directory

download_dir = os.path.join(os.getcwd(), "PhotoGallery")
if not os.path.exists(download_dir):
    os.makedirs(download_dir)


# Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Open Chrome in incognito mode
chrome_options.add_experimental_option("prefs", {
    "plugins.always_open_pdf_externally": True,
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,  # Disable prompt for download
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})


# Initialize Chrome WebDriver with options

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


# Open the website

driver.get("https://labour.gov.in/")


try:
    # Hover over "Media" menu

    media_menu = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Media']"))
    )
    # ActionChains(driver).move_to_element(media_menu).perform()

    media_menu.click()

    # Click on "Photo Gallery" submenu

    more_info = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Click for more info of Press Releases']"))
    )
    more_info.click()


    photo = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Photo Gallery'])[2]"))
    )
    href = photo.get_attribute('href')

    # Wait for the page to load

    driver.get(href)
    time.sleep(5)
    window_after = driver.window_handles[0]
    image_elements = driver.find_elements(By.XPATH, "//table//img")
    time.sleep(2)

    # Extract the URLs of the first 10 images

    image_urls = [element.get_attribute('src') for element in image_elements[:10]]
    # Download the images

    for i, url in enumerate(image_urls, 1):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(os.path.join(download_dir, f"image_{i}.jpg"), "wb") as f:
                    f.write(response.content)
                    print(f"Downloaded image {i}")
            else:
                print(f"Failed to download image {i}")
        except Exception as e:
            print(f"Error occurred while downloading image {i}: {str(e)}")


except Exception as e:
    print(f"An error occurred: {str(e)}")


finally:
    
    driver.quit()



   
 