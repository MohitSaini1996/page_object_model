import os

from selenium import webdriver
from page_object_model.pages.LandingPage import LandingPage
from page_object_model.testresources import constants


class TestDummy:
    def test_dummy(self, base_fixture):  # base_fixture now provides the 'prod' object
        prod = base_fixture  # Get the properties object from the fixture
        driver = webdriver.Chrome()
        try:
            # Pass both driver and prod to LandingPage
            landing = LandingPage(driver, prod)
            landing.landing()  # landing() method now performs navigation and returns LoginPage

            login_page = landing.landing()  # landing() returns LoginPage instance
            username_page = login_page.dologin()  # dologin() returns EnterUsername instance

            # Get the username from the prod object
            username = prod.getProperty(constants.USERNAME)  # Assuming 'constants.USERNAME' holds the key 'defaultusername'
            if username is None:
                # Fallback if the constant key is not found or empty
                username = prod.getProperty("defaultusername")

            username_page.enterUsername(username)  # Pass the username here
        except Exception as e:
            # Take screenshot on failure
            screenshot_path = os.path.join(os.getcwd(), "screenshot_on_failure.png")
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to: {screenshot_path}")
            raise e  # Re-raise the exception to mark the test as failed