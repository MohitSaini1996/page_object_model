from page_object_model.pages.LoginPage import LoginPage
from page_object_model.pages.base import base

class LandingPage(base):
    def __init__(self, driver, prod): # Expect 'prod' here
        super().__init__(driver, prod) # Pass 'prod' to the base class
        # self.driver = driver # Redundant, super().__init__ handles it

    def landing(self):
        self.navigate() # This now correctly uses self.prod from base
        return LoginPage(self.driver, self.prod) # Pass 'prod' to LoginPage