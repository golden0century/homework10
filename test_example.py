import pytest
from selenium import webdriver
from helpers import CHROME_DRIVER_PATH

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get('https://www.cian.ru')
assert 'ЦИАН' in driver.title
elem = driver.find_element_by_xpath("//a[contains(@href, 'analiz-rynka-nedvizhimosti-b2b')and contains(@class, 'top-menu-item')]")
elem.click()
assert 'Анализ' in driver.title
driver.quit()
