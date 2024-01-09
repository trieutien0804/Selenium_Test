from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.get('https://vnexpress.net/')

#driver.implicitly_wait(10)

article = driver.find_elements(By.CSS_SELECTOR, 'article.item-news')

for ar in article:
    try:
        text = ar.find_element(By.CSS_SELECTOR, 'a').get_attribute('title')
        link = ar.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        print(text)
        print(link)
        print("================")
    except NoSuchElementException:
        print('Loi')
        print("================")

driver.close()
