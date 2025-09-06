import uuid

def unique_email() -> str:
    return f"autolead+{uuid.uuid4().hex[:8]}@example.com"
