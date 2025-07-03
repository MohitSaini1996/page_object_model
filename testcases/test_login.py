import allure
import pytest
from typing import List, Any, Dict, Union

from selenium import webdriver

from page_object_model.pages.LandingPage import LandingPage
from page_object_model.testresources import constants
from page_object_model.testresources.readingexcel import getcelldata, isRunnable


@pytest.mark.usefixtures("base_fixture")
class TestLogin:
    @pytest.mark.parametrize("argvals", getcelldata("LoginTest", constants.XLS_FILEPATH))
    def test_login(self, argvals, base_fixture): # <--- Add base_fixture as an argument here
        #testcase - firstlevel check
        testrunmode = isRunnable("LoginTest", constants.XLS_FILEPATH)
        #datasheet - secondlevel check
        datarunmode = argvals[constants.RUNMODE]

        prod = base_fixture # <--- Get the 'prod' object from the fixture

        if(testrunmode):
            if(datarunmode == constants.RUNMODE_Y):
                for i in range(0,len()):
                    print(argvals[i])
                driver = webdriver.Chrome()
                # Pass the 'prod' object obtained from the fixture
                landing = LandingPage(driver, prod) # <--- Use 'prod' here
                login = landing.landing()
                username = login.dologin()
                password = username.enterUsername(argvals[constants.USERNAME])
                password.enterUsername(argvals[constants.PASSWORD])
                # You have 'username = login.dologin()' which returns EnterUsername object.
                # Then 'password = username.enterusername()'. It seems 'password' is not used,
                # and 'enterusername()' is called twice (once for assignment, once again for 'password').
                # You probably meant to call a method like enterpassword() or similar.
                # Assuming `enterusername()` is the correct method for the username page.
                #username.enterUsername() # Call the method on the username object.
            else:
                pytest.skip("test case skiped")
        else:
            pytest.skip("test case skipped")
