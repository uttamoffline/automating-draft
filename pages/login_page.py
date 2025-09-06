from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import settings


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Log In']")

    def go_to_login_page(self):
        """Navigate to the login page"""
        self.driver.get(settings.BASE_URL)

    def login(self, username: str, password: str):
        """Fill credentials and log in"""
        email_el = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        email_el.clear()
        email_el.send_keys(username)

        pass_el = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        pass_el.clear()
        pass_el.send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def is_login_successful(self, success_locator=(By.CSS_SELECTOR, "nav")):
        """
        Optional: Verify login worked.
        Adjust success_locator to something visible only after login.
        """
        try:
            self.wait.until(EC.visibility_of_element_located(success_locator))
            return True
        except:
            return False
