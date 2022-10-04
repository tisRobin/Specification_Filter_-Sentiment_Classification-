import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

chrome_driver_path = "C:\\Users\\nicol\\OneDrive\\Desktop\\Datum Proj\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url_base = 'https://www.sephora.com/shop/'
product_sections = ['moisturizing-cream-oils-mists', 'cleanser', 'facial-treatments',
                    'wellness-skincare', 'eye-treatment-dark-circle-treatment', 'face-mask', 'skin-care-tools',
                    'sunscreen-sun-protection', 'self-tanning-products', 'lip-treatments', 'vegan-skin-care'
                    ]

product_url_df = pd.DataFrame(columns=['Category', 'URL'])


def scrollDrown(driver, n_scroll):
    body = driver.find_element_by_tag_name("body")
    while n_scroll >= 0:
        body.send_keys(Keys.PAGE_DOWN)
        n_scroll -= 1
    return driver


for product in product_sections:
    page_num = 1

    while True:
        url = url_base + product + '?pageSize=300&currentPage=' + str(page_num)
        driver.get(url)
        time.sleep(20)
        try:  # empty page
            xpath = '//*[@id="modalDialog"]/button'
            btn = driver.find_element_by_xpath(xpath)
            btn.click()
            time.sleep(20)
            if driver.find_elements_by_class_name('css-1kv743p 365zztl0').is_displayed():
                break
        except:
            pass

        old_len = 0  # check if no room to scroll

        while True:
            browser = scrollDrown(driver, 20)
            time.sleep(10)
            slug = driver.find_elements_by_class_name(
                'css-ix8kml')  # get product urls
            new_len = len(slug)
            if old_len == new_len:
                break
            else:
                old_len = new_len  # assign
        slugURL = []
        for a in slug:
            subURL = {}
            subURL['Category'] = product
            subURL['URL'] = a.get_attribute('href')
            slubURL.append(subURL)

        df = pd.DataFrame(slugURL)
        page_num += 1
        product_url_df = pd.concat(
            [product_url_df, df], axis=0, ignore_index=True)
driver.close()

product_url_df.to_csv('.product_urls.csv', index=False)

# code reference: https://github.com/LenaNevel/CAPSTONE
