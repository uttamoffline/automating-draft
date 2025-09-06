import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CRMPage:
    NAV_LINK = (By.CSS_SELECTOR, "a[href*='/crm']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[data-testid='crm-search']")
    LEAD_ROWS = (By.CSS_SELECTOR, "tr[data-testid^='lead-']")
    LEAD_EMAIL_CELL = (By.CSS_SELECTOR, "td[data-testid='lead-email']")

    def __init__(self, driver):
        self.driver = driver

    def go_to_crm(self):
        self.driver.find_element(*self.NAV_LINK).click()

    def search_lead(self, email: str):
        search = self.driver.find_element(*self.SEARCH_INPUT)
        search.clear()
        search.send_keys(email)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

    def lead_exists(self, email: str) -> bool:
        rows = self.driver.find_elements(*self.LEAD_ROWS)
        for r in rows:
            try:
                cell = r.find_element(*self.LEAD_EMAIL_CELL)
                if email in cell.text:
                    return True
            except Exception:
                continue
        return False

    def get_lead_id(self, email: str):
        rows = self.driver.find_elements(*self.LEAD_ROWS)
        for r in rows:
            try:
                cell = r.find_element(*self.LEAD_EMAIL_CELL)
                if email in cell.text:
                    attr = r.get_attribute("data-testid")
                    if attr and attr.startswith("lead-"):
                        return attr.split("lead-")[-1]
            except Exception:
                continue
        return None
