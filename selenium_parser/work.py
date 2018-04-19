#!/usr/bin/env python3

#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# from writeout import write_out_to_log

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
        website = 'https://www.sec.gov/cgi-bin/browse-edgar?CIK={cik}'.format(cik=cik)
        time.sleep(1)
        driver.get(website)
        timeout = 20

        try:
            WebDriverWait(driver, timeout)
            # driver.implicitly_wait(25)

            # extract data here
            elements = driver.find_elements_by_class_name('tableFile2')
            print(elements[0].get_attribute('innerHTML'))


            # rows = driver.find_elements(By.TAG_NAME, "tr")
            # # for row in rows:
            # #     col = row.find_elements(By.TAG_NAME, "td")
            # #     print(col)
            # tds = rows[0].find_elements(By.TAG_NAME, "td")
            # print(tds[1].text)

            # writeout data here
        except:
            print('ERROR')


if __name__ == "__main__":
    # init driver
    driver = init_driver()
    lookup(driver)
    # write_out_to_log(payload=0, cik_id=0)
    # close driver
    time.sleep(1)
    driver.quit()

