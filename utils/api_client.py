import requests
from config.settings import settings

class APIClient:
    def __init__(self):
        self.base = settings.API_BASE
        self.token = settings.API_TOKEN

    def _headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def get_lead(self, lead_id):
        if not self.base or not self.token:
            return None
        resp = requests.get(f"{self.base.rstrip('/')}/leads/{lead_id}", headers=self._headers())
        resp.raise_for_status()
        return resp.json()

    def delete_lead(self, lead_id):
        if not self.base or not self.token:
            return None
        resp = requests.delete(f"{self.base.rstrip('/')}/leads/{lead_id}", headers=self._headers())
        return resp.status_code in (200, 204)
