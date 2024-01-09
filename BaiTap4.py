from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')

driver.implicitly_wait(10)

try:
    driver.find_element(By.XPATH, '//*[text()="Create new account"]').click()

    driver.find_element(By.NAME, 'firstname').send_keys('Tien')

    driver.find_element(By.NAME, 'lastname').send_keys('Nguyen')

    driver.find_element(By.NAME, 'reg_email__').send_keys('trieutien@gmail.com')

    driver.find_element(By.NAME, 'reg_email_confirmation__').send_keys('trieutien@gmail.com')

    driver.find_element(By.NAME, 'reg_passwd__').send_keys('Abc@123')

    birth_day = Select(driver.find_element(By.NAME,'birthday_day'))
    birth_day.select_by_visible_text('8')

    birth_month = Select(driver.find_element(By.NAME,'birthday_month'))
    birth_month.select_by_visible_text('Apr')

    birth_year = Select(driver.find_element(By.NAME,'birthday_year'))
    birth_year.select_by_visible_text('2003')

    driver.find_element(By.XPATH, '//label[text()="Male"]').click()

    driver.find_element(By.NAME, 'websubmit').click()

except Exception as ex:
    print(ex)

driver.quit()

