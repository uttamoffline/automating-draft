import time
import pytest
import re
from config.settings import settings
from pages.chat_page import ChatPage
from pages.crm_page import CRMPage
from utils.data_loader import load_test_data


# Load datasets
happy_cases = load_test_data("happy_path.txt")
clutter_cases = load_test_data("clutter_with_email.txt")
abusive_cases = load_test_data("abusive_dialogue.txt")
long_cases = load_test_data("long_messages.txt")
invalid_cases = load_test_data("invalid_inputs.txt")


@pytest.mark.parametrize("message", happy_cases)
def test_happy_cases(driver, api_client, message):
    email = re.search(r"[\w\.-]+@[\w\.-]+", message).group(0)

    driver.get(settings.BASE_URL)
    chat = ChatPage(driver)
    crm = CRMPage(driver)

    chat.open_chat()
    chat.send_message(message)
    time.sleep(3)

    crm.go_to_crm()
    crm.search_lead(email)
    assert crm.lead_exists(email)


@pytest.mark.parametrize("message", clutter_cases)
def test_clutter_cases(driver, api_client, message):
    email = re.search(r"[\w\.-]+@[\w\.-]+", message).group(0)

    driver.get(settings.BASE_URL)
    chat = ChatPage(driver)
    crm = CRMPage(driver)

    chat.open_chat()
    chat.send_message(message)
    time.sleep(3)

    crm.go_to_crm()
    crm.search_lead(email)
    assert crm.lead_exists(email)


@pytest.mark.parametrize("message", abusive_cases)
def test_abusive_cases(driver, message):
    """Abusive/no-email dialogues should not create leads"""
    driver.get(settings.BASE_URL)
    chat = ChatPage(driver)
    crm = CRMPage(driver)

    chat.open_chat()
    chat.send_message(message)
    time.sleep(2)

    crm.go_to_crm()
    crm.search_lead("no-such-email@example.com")
    assert not crm.lead_exists("no-such-email@example.com")


@pytest.mark.parametrize("message", long_cases)
def test_long_messages(driver, api_client, message):
    email = re.search(r"[\w\.-]+@[\w\.-]+", message).group(0)

    driver.get(settings.BASE_URL)
    chat = ChatPage(driver)
    crm = CRMPage(driver)

    chat.open_chat()
    chat.send_message(message)
    time.sleep(3)

    crm.go_to_crm()
    crm.search_lead(email)
    assert crm.lead_exists(email)


@pytest.mark.parametrize("message", invalid_cases)
def test_invalid_inputs(driver, message):
    """Messages without valid email should not create leads"""
    driver.get(settings.BASE_URL)
    chat = ChatPage(driver)
    crm = CRMPage(driver)

    chat.open_chat()
    chat.send_message(message)
    time.sleep(2)

    crm.go_to_crm()
    crm.search_lead("no-such-email@example.com")
    assert not crm.lead_exists("no-such-email@example.com")
