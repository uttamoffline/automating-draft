import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import settings

log = logging.getLogger(__name__)

def login(driver, wait=None):
    """Logs into the app using TEST_USER and TEST_PASS from settings.py"""
    driver.get(settings.BASE_URL)
    if not wait:
        wait = WebDriverWait(driver, 60)

    log.info("Waiting for email field...")
    email_el = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Email']")))
    email_el.send_keys(settings.TEST_USER)
    log.info("✅ Email entered")

    log.info("Waiting for password field...")
    pass_el = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']")))
    pass_el.send_keys(settings.TEST_PASS)
    log.info("✅ Password entered")

    log.info("Waiting for login button...")
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Log In']")))
    login_btn.click()
    log.info("✅ Login button clicked")

    # give time for the heavy dashboard to render
    time.sleep(5)
