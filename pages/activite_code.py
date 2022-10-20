from base.buse_page import Buse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Code_activite(Buse):


    def __init__(self,  driver):
        super().__init__(driver)
        self.driver = driver


    # LOCATORS

    login_btn_code = "//button[@id='login-otp-button']"


    # GETERS

    def get_login_btn_code(self):
        return  WebDriverWait(self.driver, 30).until( EC.presence_of_element_located((By.XPATH, self.login_btn_code)))


    # ACTIONS

    def click_get_login_btn_code(self):
        self.get_login_btn_code().click()
        print("Click Login button code")


    # METHOD

    def open_activite_code(self):
        self.get_current_url()
        self.click_get_login_btn_code()


