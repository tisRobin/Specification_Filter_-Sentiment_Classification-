from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

chrome_driver_path = "C:\\Users\\nicol\\OneDrive\\Desktop\\Datum Proj\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url_base = 'https://www.sephora.com/shop/'
product_sections = ['moisturizing-cream-oils-mists', 'cleanser', 'facial-treatments',
                    'wellness-skincare', 'eye-treatment-dark-circle-treatment', 'face-mask', 'skin-care-tools',
                    'sunscreen-sun-protection', 'self-tanning-products', 'lip-treatments', 'vegan-skin-care'
                    ]

product_url_df = pd.DataFrame(columns=['Category', 'URL'])


def scrollDown(driver, n_scroll):  # function for scrolling page down
    body = driver.find_element_by_tag_name("body")
    while n_scroll >= 0:
        body.send_keys(Keys.PAGE_DOWN)
        n_scroll -= 1
    return driver


for product in product_sections:
    url = url_base + product
    driver.get(url)
    WebDriverWait(driver, 10)

    # check for country code pop up & dismiss
    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/div/button').click()
        WebDriverWait(driver, 10)
    except:
        pass

    # pagination
    current_page = 1
    while True:
        print(f"Processing page {current_page}")

        # scroll until no more room & collect all urls
        old_len = 0
        while True:
            scrollDown(driver, 20)
            sleep(10)
            find_product_urls = driver.find_elements_by_class_name(
                "css-ix8km1")  # list of elements, need get to pull href
            new_len = len(find_product_urls)
            if old_len == new_len:  # no new urls
                break
            else:
                old_len = new_len
        # print(f"find product url: {find_product_urls}")  # test

        # organize collected urls in temporary df and push to main df
        organized_urls = []
        for url in find_product_urls:
            category_url = {}
            category_url['Category'] = product
            category_url['URL'] = url.get_attribute('href')
            organized_urls.append(category_url)

        df = pd.DataFrame(organized_urls)
        print(df.head())  # testing
        product_url_df = pd.concat(
            [product_url_df, df], axis=0, ignore_index=True)

       # check if click next page is disabled
        try:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/main/div[3]/div/div[2]/div[2]/nav/ul/button[@disabled='']")
            break
        except NoSuchElementException:
            pass

        try:  # click next page
            next_page = driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/main/div[3]/div/div[2]/div[2]/nav/ul/button")
            next_page.click()
            WebDriverWait(driver, 10)
            current_page += 1
        except ElementNotInteractableException:
            try:  # check for sign in pop up
                driver.find_element_by_xpath(
                    '//*[@id="modal1Dialog"]/button').click()
                WebDriverWait(driver, 10)
            except NoSuchElementException:
                pass

        except NoSuchElementException:
            print(f"Last Page {product}: {current_page}")
            break

driver.close()

product_url_df
product_url_df.to_csv('product_urls.csv', index=False)
# code references: https://github.com/LenaNevel/CAPSTONE,
# credit for scrolldown function code code: https://www.hackerearth.com/fr/practice/notes/praveen97uma/crawling-a-website-that-loads-content-using-javascript-with-selenium-webdriver-in-python/
