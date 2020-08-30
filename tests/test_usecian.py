class TestsCian:

    def test_usecian(self, driver):
        driver.get('https://www.cian.ru')
        assert 'ЦИАН' in driver.title
        elem = driver.find_element_by_xpath("//a[@data-footer-track-click = 'price']")
        elem.click()
        assert 'Стоимость размещения' in driver.title

