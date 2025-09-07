import time
import pytest
from config.settings import settings
from pages.login_page import LoginPage
from pages.chat_page import ChatPage
from pages.crm_page import CRMPage
from utils.data_factory import unique_email


@pytest.mark.order(1)
def test_happy_path_lead_intake(driver, api_client):
    """Happy path: Login → Send chat → Verify CRM lead → Cross-check API."""
    email = unique_email()
    message = f"Hi, I want info. My email is {email}"

    # Step 1: Login
    login = LoginPage(driver)
    login.go_to_login_page()
    login.login(settings.TEST_USER, settings.TEST_PASS)

    # Step 2: Chat
    chat = ChatPage(driver)
    chat.open_chat()
    chat.send_message(message)
    time.sleep(3)

    # Step 3: CRM
    crm = CRMPage(driver)
    crm.go_to_crm()
    crm.search_lead(email)
    assert crm.lead_exists(email), f"Lead {email} not found in CRM"

    # Step 4: API Cross-check
    lead_id = crm.get_lead_id(email)
    if lead_id:
        data = api_client.get_lead(lead_id)
        assert data and data.get("email") == email
        api_client.delete_lead(lead_id)
