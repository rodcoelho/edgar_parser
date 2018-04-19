#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

websites = ['https://github.com/TheDancerCodes']
option = webdriver.ChromeOptions()
option.add_argument(" - incognito")


def init_driver():
    browser = webdriver.Chrome(executable_path='/Users/rodrigocoelho/Downloads/chromedriver', chrome_options=option)
    browser.wait = WebDriverWait(browser, 15)
    return browser

def lookup(browser):
    # loads page
    for sites in websites:
        time.sleep(1)
        browser.get(sites)

        timeout = 20
        try:
            WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")
            browser.quit()

        # get GitHub Links name
        selenium_object = browser.find_elements_by_xpath("//a[@class='text-bold']")
        # <a href="/Some_link/some_folder" class="text-bold">

        text_from_object = [x.text for x in selenium_object]

        print(text_from_object)


if __name__ == "__main__":
    # init driver
    browser = init_driver()
    # tell driver to look up query on google
    lookup(browser)
    time.sleep(2)
    # close driver
    browser.quit()
