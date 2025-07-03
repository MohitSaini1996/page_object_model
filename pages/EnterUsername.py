import time
from selenium.webdriver.common.by import By

from page_object_model.pages.EnterPassword import EnterPassword
from page_object_model.pages.base import base

class EnterUsername(base):
    def __init__(self, driver, prod): # Expect 'prod' here
        super().__init__(driver, prod) # Pass 'prod' to the base class
        # self.driver = driver # Redundant

    def enterUsername(self,username):
        time.sleep(5)
        self.type('usernametextbox_id', username)
        self.click('submitemailbtn_xpath')
        return EnterPassword(self.driver,self.prod)# This now correctly uses self.prod from base
        time.sleep(5)