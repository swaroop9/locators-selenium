import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils import BaseClass


class TestIDLOCATOR(BaseClass):

    def test_e2e(self):
        log = self.getLogger()

    @pytest.mark.skip
    def test_id_locator(self):
        # service = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service)
        # # driver = webdriver.Chrome('./chromedriver') # deprecated
        # driver.get("https://the-internet.herokuapp.com/login")
        # driver.maximize_window()
        # print(driver.title)
        # username = driver.find_element_by_id("username") # deprecated
        driver = self.driver
        id_locator = (By.ID, "username")
        username = driver.find_element(*id_locator)
        username.clear()
        username.send_keys("tomsmith")
        # search_bar.send_keys(Keys.RETURN)
        print(username.text)
        assert username.text == 'tomsmith'
        print(driver.current_url)
        driver.close()

    def test_id_locator_using_form(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        # driver = webdriver.Chrome('./chromedriver') # deprecated
        driver.get("https://the-internet.herokuapp.com/login")
        form = driver.find_element(By.ID, "login")
        id_locator = (By.ID, "username")
        username = form.find_element(*id_locator)
        username.send_keys("tomsmith")
        print("Username", username.text)
        driver.close()
