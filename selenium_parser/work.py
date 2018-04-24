#!/usr/bin/env python3

#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from lxml import html
import requests

from writeout import write_out_to_log

urlhead = 'https://www.sec.gov'

#ciks = ['0001166559', '0001067983']
ciks = ['0001166559']

thirteen_link = {}
xml_link = {}


def init_driver():
    option = webdriver.ChromeOptions()
    option.add_argument(" - incognito")

    driver = webdriver.Chrome(executable_path='/Users/rodrigocoelho/Downloads/chromedriver', chrome_options=option)
    driver.wait = WebDriverWait(driver, 15)
    return driver


def lookup(driver):
    for cik in ciks:
        mini_payload = []
        website = '{head}/cgi-bin/browse-edgar?CIK={cik}'.format(head=urlhead, cik=cik)
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

            soup = BeautifulSoup(payload, 'html.parser')

            rows = soup.findAll('tr')
            for tr in rows:
                cols = tr.findAll('td')

                if len(cols) >= 1 and '13F-HR' in cols[0].text:
                    filling_date = cols[3].text
                    link = cols[1].find('a').get('href')
                    mini_payload.append([filling_date, str(link)])
            thirteen_link[cik] = mini_payload
        except:
            print('ERROR 1')


def getxmlpages(driver):
    for key, value in thirteen_link.items():
        mini_payload = []
        for link in value:
            website = '{head}{link}'.format(head=urlhead, link=link[1])
            time.sleep(1)
            driver.get(website)
            timeout = 20

            try:
                WebDriverWait(driver, timeout)
                # driver.implicitly_wait(25)

                # extract data here
                elements = driver.find_elements_by_class_name('tableFile')
                payload = elements[0].get_attribute('innerHTML')
                # write_out_to_log(payload=payload, cik_id=cik)

                soup = BeautifulSoup(payload, 'html.parser')

                rows = soup.findAll('tr')
                for tr in rows:
                    cols = tr.findAll('td')

                    if len(cols) >= 1 and 'INFORMATION TABLE' in cols[1].text:
                        xlink = cols[2].find('a').get('href')
                        if 'xslForm' in str(xlink):
                            mini_payload.append([link[0], xlink])
                xml_link[key] = mini_payload
            except:
                print('ERROR 2')


def data_extraction():
    for key, value in xml_link:
        for datalink in value:
            website = '{head}{link}'.format(head=urlhead, link=datalink[1])
            page = requests.get(website)
            tree = html.fromstring(page.content)

            try:
                # data extraction
                table = tree.xpath("//table")[3]
                for row in table.xpath(".//tr"):
                    # get the text from all the td's from each row
                    row_list = [td.text for td in row.xpath(".//td[text()]")]
                    print('\t'.join(map(str, row_list)))

            except:
                print('ERROR 3')


if __name__ == "__main__":
    # init driver
    driver = init_driver()
    # gets the 13F links and stores them in thirteen_link list
    lookup(driver)
    getxmlpages(driver)
    data_extraction()
    # close driver
    time.sleep(5)
    driver.quit()
    driver.quit()

