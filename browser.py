from functools import lru_cache
import time
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOption
from selenium.webdriver.chrome.options import Options as ChromeOption

WINDOW_HEIGHT = "1080"
WINDOW_WIDTH = "1920"

firefox_options = FirefoxOption()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--width=%s" % WINDOW_WIDTH)
firefox_options.add_argument("--height=%s" % WINDOW_HEIGHT)

chrome_options = ChromeOption()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument(
    "--window-size=%s,%s" %
    (WINDOW_WIDTH, WINDOW_HEIGHT))

@lru_cache(maxsize=16)
def make_screenshot(url: str, date: str) -> bytes:
    if "USE_FIREFOX" in os.environ.keys():
        driver = webdriver.Firefox(
            options=firefox_options
        )
    else:
        driver = webdriver.Chrome(
            options=chrome_options
        )

    driver.get(url)
    time.sleep(4)
    screenshot = driver.get_screenshot_as_png()
    driver.close()

    return screenshot
