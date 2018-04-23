#!/usr/bin/env python3

#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

from writeout import write_out_to_log

urlhead = 'https://www.sec.gov/'

#ciks = ['0001166559', '0001067983']
ciks = ['0001166559']


def init_driver():
    option = webdriver.ChromeOptions()
    option.add_argument(" - incognito")

    driver = webdriver.Chrome(executable_path='/Users/rodrigocoelho/Downloads/chromedriver', chrome_options=option)
    driver.wait = WebDriverWait(driver, 15)
    return driver


def lookup(driver):
    for cik in ciks:
        website = '{head}cgi-bin/browse-edgar?CIK={cik}'.format(head=urlhead, cik=cik)
        time.sleep(1)
        driver.get(website)
        timeout = 20

        try:
            WebDriverWait(driver, timeout)
            # driver.implicitly_wait(25)

            # extract data here
            elements = driver.find_elements_by_class_name('tableFile2')
            payload = elements[0].get_attribute('innerHTML')
            # write_out_to_log(payload=payload, cik_id=cik)


            thirteen_link = []
            soup = BeautifulSoup(payload, 'html.parser')


            rows = soup.findAll('tr')
            for tr in rows:
                cols = tr.findAll('td')

                if len(cols) >= 1 and '13F-HR' in cols[0].text:
                    link = cols[1].find('a').get('href')
                    print(link)



        except:
            print('ERROR')


if __name__ == "__main__":
    # init driver
    driver = init_driver()
    lookup(driver)
    # close driver
    time.sleep(1)
    driver.quit()

