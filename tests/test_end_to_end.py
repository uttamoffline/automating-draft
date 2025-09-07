import time
import pytest
import re
from config.settings import settings
from pages.chat_page import ChatPage
from pages.crm_page import CRMPage
from utils.api_client import APIClient
from utils.data_loader import load_test_data
from utils.login import login   # ✅ import login helper

happy_message = load_test_data("happy_path.txt")[0]
clutter_message = load_test_data("clutter_with_email.txt")[0]
abusive_message = load_test_data("abusive_dialogue.txt")[0]
long_message = load_test_data("long_messages.txt")[0]
invalid_message = load_test_data("invalid_inputs.txt")[0]


@pytest.mark.order(1)
def test_happy_path(driver, api_client):
    """Happy path: Chat → CRM lead → API cross-check"""
    login(driver)   # ✅ call login util

    email_match = re.search(r"[\w\.-]+@[\w\.-]+", happy_message)
    assert email_match, "Happy path message must contain an email"
    email = email_match.group(0)

    chat = ChatPage(driver)
    crm = CRMPage(driver)

    chat.open_chat()
    chat.send_message(happy_message)
    time.sleep(3)

    crm.go_to_crm()
    crm.search_lead(email)
    assert crm.lead_exists(email), f"Lead {email} not found in CRM"

    lead_id = crm.get_lead_id(email)
    if lead_id:
        data = api_client.get_lead(lead_id)
        assert data and data.get("email") == email
        api_client.delete_lead(lead_id)


@pytest.mark.order(2)
def test_negative_case(driver):
    """Negative: abusive text should not create lead"""
    login(driver)   # ✅ login before starting

    chat = ChatPage(driver)
    crm = CRMPage(driver)

    chat.open_chat()
    chat.send_message(abusive_message)
    time.sleep(2)

    crm.go_to_crm()
    crm.search_lead("no-such-email@example.com")
    assert not crm.lead_exists("no-such-email@example.com")




@pytest.mark.order(3)
def test_edge_case_long_message(driver):
    """Edge: very long message with email still creates lead"""
    email = re.search(r"[\w\.-]+@[\w\.-]+", long_message).group(0)

    driver.get(settings.BASE_URL)
    logging = login(driver)
    logging.go_to_login_page()
    logging.login(settings.TEST_USER, settings.TEST_PASS)

    chat = ChatPage(driver)
    crm = CRMPage(driver)

    chat.open_chat()
    chat.send_message(long_message)
    time.sleep(3)

    crm.go_to_crm()
    crm.search_lead(email)
    assert crm.lead_exists(email)


@pytest.mark.order(4)
def test_invalid_input(driver):
    """Invalid input: random text without email should not create lead"""
    driver.get(settings.BASE_URL)
    logging = login(driver)
    logging.go_to_login_page()
    logging.login(settings.TEST_USER, settings.TEST_PASS)

    chat = ChatPage(driver)
    crm = CRMPage(driver)

    chat.open_chat()
    chat.send_message(invalid_message)
    time.sleep(2)

    crm.go_to_crm()
    crm.search_lead("no-such-email@example.com")
    assert not crm.lead_exists("no-such-email@example.com")
