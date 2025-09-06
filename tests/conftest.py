import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import settings
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    return APIClient()

@pytest.fixture
def driver(request):
    options = Options()
    if settings.HEADLESS:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(8)
    yield drv
    drv.quit()

# Save screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            ts = int(time.time())
            fname = f"failure-{item.name}-{ts}.png"
            driver.save_screenshot(fname)
            print(f"[SCREENSHOT SAVED] {fname}")
