import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("set_up")
class BaseClass:

    @staticmethod
    def get_logger():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    # def verifyLinkPresence(self, text):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT, text))
    #
    # @staticmethod
    # def selectOptionByTest(self, locator, text):
    #     sel = Select(locator)
    #     sel.select_by_visible_text(text)
