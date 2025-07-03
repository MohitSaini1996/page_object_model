import time
from selenium.webdriver.common.by import By
from page_object_model.pages.base import base

class EnterPassword(base):
    def __init__(self, driver, prod): # Expect 'prod' here
        super().__init__(driver, prod) # Pass 'prod' to the base class
        # self.driver = driver # Redundant

    def enterUsername(self,password):
        time.sleep(5)
        self.type('passwordtextbox_id', password)
        self.click('signinbtn_xpath')# This now correctly uses self.prod from base
        time.sleep(5)