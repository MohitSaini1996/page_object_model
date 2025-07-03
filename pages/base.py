import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object_model.testresources import constants


class base:
    def __init__(self, driver, prod):
        self.driver = driver
        self.prod = prod

    def openbrowser(self, browsername):
        if(browsername == constants.CHROME):
            self.driver = webdriver.Chrome()
        elif(browsername == constants.FIREFOX):
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()


    def navigate(self):
        url = self.prod['URL']
        print(url)
        self.driver.get(url)

    def click(self, obj):
        self.getelement(obj).click()

    def type(self, obj, data):
        self.getelement(obj).send_keys(data)

    #common utility function
    def waitforpagetobeloaded(self):
        i=1
        while(i!=10):
            load_status = self.driver.execute_script("return document.readyState;")
            if(load_status=="complete"):
                break
            else:
                time.sleep(2)

    def iselementpresent(self,obj):
        wait = WebDriverWait(self.driver, 20)
        element = self.prod[obj]
        self.waitforpagetobeloaded()
        if (obj.endswith('_xpath')):
            elementlist = wait.until(EC.presence_of_all_elements_located((By.XPATH, element)))
        elif (obj.endswith('_id')):
            elementlist = wait.until(EC.presence_of_all_elements_located((By.ID, element)))
        elif (obj.endswith('_name')):
            elementlist = wait.until(EC.presence_of_all_elements_located((By.NAME, element)))
        elif (obj.endswith('_cssSelector')):
            elementlist = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, element)))
        else:
            elementlist = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, element)))
        if (len(elementlist) == 0):
            return False
        else:
            return True


    def iselementvissible(self, obj):
        wait = WebDriverWait(self.driver, 20)
        element = self.prod[obj]
        self.waitforpagetobeloaded()
        try:
            if (obj.endswith('_xpath')):
                wait.until(EC.visibility_of_element_located((By.XPATH, element)))
            elif (obj.endswith('_id')):
                wait.until(EC.visibility_of_element_located((By.ID, element)))
            elif (obj.endswith('_name')):
                wait.until(EC.visibility_of_element_located((By.NAME, element)))
            elif (obj.endswith('_cssSelector')):
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
            else:
                wait.until(EC.visibility_of_element_located((By.TAG_NAME, element)))
            return True  # If the wait succeeds, the element is visible
        except TimeoutException:
            return False # If a TimeoutException occurs, the element is not visible within the timeout


    def getelement(self, locator):
        obj = self.prod[locator]
        if(self.iselementpresent(locator)) and self.iselementvissible(locator):
            try:
                if(locator.endswith('_xpath')):
                    element = self.driver.find_element(By.XPATH, (obj))
                elif(locator.endswith('_id')):
                    element = self.driver.find_element(By.ID, (obj))
                elif (locator.endswith('_name')):
                    element = self.driver.find_element(By.NAME, (obj))
                elif (locator.endswith('_cssSelector')):
                    element = self.driver.find_element(By.CSS_SELECTOR, (obj))
                else:
                    return False
                return element
            except Exception:
                print("Element not found")