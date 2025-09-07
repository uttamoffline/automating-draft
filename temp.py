import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# --- LOGGING ---
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

# --- CONFIG ---
BASE_URL = "https://test.wing.work"
USER = "testsuttam@gmail.com"
PASS = "Aa@123456789"

# --- DRIVER SETUP ---
options = Options()
# options.add_argument("--headless=new")   # enable if you want headless
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

# ✅ This prevents waiting for images/scripts/fonts
options.page_load_strategy = "eager"  # alternatives: "normal", "eager", "none"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 60)  # wait only for elements we need

try:
    log.info("Opening the app without waiting for heavy rendering...")
    driver.get(BASE_URL)

    log.info("Waiting for email field...")
    email_el = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Email']")))
    email_el.send_keys(USER)
    log.info("✅ Email entered")

    log.info("Waiting for password field...")
    pass_el = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']")))
    pass_el.send_keys(PASS)
    log.info("✅ Password entered")

    log.info("Waiting for login button...")
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Log In']")))
    login_btn.click()
    log.info("✅ Login button clicked")

    # optional: wait a bit to observe result
    time.sleep(40)
    log.info("✅ Test finished without errors")

except Exception as e:
    log.error(f"❌ Test failed: {e}")

# finally:
#     driver.quit()
