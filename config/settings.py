import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://test.wing.work")
    TEST_USER = os.getenv("TEST_USER", "testsuttam@gmail.com")
    TEST_PASS = os.getenv("TEST_PASS", "Aa@123456789")
    API_BASE = os.getenv("API_BASE")
    API_TOKEN = os.getenv("API_TOKEN")
    HEADLESS = os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes")

settings = Settings()
