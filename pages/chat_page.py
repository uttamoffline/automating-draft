from selenium.webdriver.common.by import By

class ChatPage:
    CHAT_OPEN = (By.CSS_SELECTOR, "button[data-testid='open-chat']")
    CHAT_INPUT = (By.CSS_SELECTOR, "textarea[data-testid='chat-input']")
    SEND_BTN = (By.CSS_SELECTOR, "button[data-testid='send-message']")

    def __init__(self, driver):
        self.driver = driver

    def open_chat(self):
        self.driver.find_element(*self.CHAT_OPEN).click()

    def send_message(self, message: str):
        inp = self.driver.find_element(*self.CHAT_INPUT)
        inp.clear()
        inp.send_keys(message)
        self.driver.find_element(*self.SEND_BTN).click()
