from selenium.webdriver.common.by import By
'''
chatboticon = //a[@class='nav-item active w-full']
new_chat_button = //button[@aria-label='New Chat']
chat_boc = //div[@class='w-full max-w-3xl mx-auto px-4']//textarea[@placeholder='Ask me anything...']
chat_box_css_selector = div[class='w-full max-w-3xl mx-auto px-4'] textarea[placeholder='Ask me anything...']
send_button = (//button[@aria-label='Send message'])[1]



'''
class ChatPage:
    CHAT_OPEN = (By.CSS_SELECTOR, "button[data-testid='open-chat']")
    CHAT_INPUT = (By.CSS_SELECTOR, "textarea[data-testid='chat-input']")
    SEND_BTN = (By.CSS_SELECTOR, "button[@aria-label='Send message']")
    NEW_CHAT_BTN = (By.CSS_SELECTOR, "button[@aria-label='New Chat']")

    def __init__(self, driver):
        self.driver = driver

    def open_chat(self):

        self.driver.find_element(*self.CHAT_OPEN).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.NEW_CHAT_BTN).click()

    def send_message(self, message: str):
        inp = self.driver.find_element(*self.CHAT_INPUT)
        inp.clear()
        inp.send_keys(message)
        self.driver.find_element(*self.SEND_BTN).click()
