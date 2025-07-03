import time
from selenium.webdriver.common.by import By
from page_object_model.pages.EnterUsername import EnterUsername
from page_object_model.pages.base import base

class LoginPage(base):
    def __init__(self, driver, prod): # Expect 'prod' here
        super().__init__(driver, prod) # Pass 'prod' to the base class
        # self.driver = driver # Redundant

    def dologin(self):
        self.click('loginlink_xpath') # This now correctly uses self.prod from base
        return EnterUsername(self.driver, self.prod) # Pass 'prod' to EnterUsername