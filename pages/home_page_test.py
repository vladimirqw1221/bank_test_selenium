from base.buse_page import Buse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home(Buse):
    url = "https://idemo.bspb.ru/"

    def __init__(self,  driver):
        super().__init__(driver)
        self.driver = driver


    # LOCATORS

    login_btn = "//button[@id='login-button']"


    # GETERS

    def get_login_btn(self):
        return  WebDriverWait(self.driver, 30).until( EC.presence_of_element_located((By.XPATH, self.login_btn)))


    # ACTIONS

    def click_login_btn(self):
        self.get_login_btn().click()
        print("click button login")


    # METHOD

    def open_bank_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_login_btn()

