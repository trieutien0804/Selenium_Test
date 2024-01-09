from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.conferenceseries.com/past-conference-reports.php')

item = driver.find_element(By.CLASS_NAME, 'list-group')

print(item.text)

driver.close()