
# QA Automation Framework – Chat Agent & CRM

Automated test suite for the Chat Agent + CRM integration.  
Covers the **lead intake flow** as the core scenario, with **happy path, negative cases, and edge cases** included.
---

## Project Layout

- **config/** → Settings (URL, credentials via env vars)
- **data/** → Input datasets (`happy_path.txt`, `invalid_inputs.txt`, etc.)
- **pages/** → Page Objects (Login, Chat, CRM)
- **tests/** → Pytest test suites
- **utils/** → Helpers (API client, data loader)
- **report.html** → Test report (pytest-html)
- **failure-*.png** → Screenshots on failures

---

## How It Works

- **Page Object Model (POM):** Pages wrap locators & actions.  
- **Data-driven tests:** Messages are pulled from `data/` text files.  
- **API client:** Optional backend cross-check for created leads.  
- **Pytest runner:** Orchestrates UI + API, captures screenshots on failure.
- **CI runner:** Orchestrates Suite on every Push.

Command to run:

```bash
pytest -q tests/test_end_to_end.py --html=report.html --self-contained-html
```

---

## Test Cases

1. **Happy Path** → Send valid lead → CRM should show lead.  
2. **Negative** → Abusive text → No lead created.  
3. **Edge** → Very long input with email → Lead still created.  
4. **Invalid Input** → Random text, no email → No lead created.

---

## Failure Evidence

- Failures trigger screenshots (`failure-*.png`).  
- `report.html` gives consolidated run results.

---

## Next Steps

- Stabilize login & slow page loads.  
- Add multiple scenarios for user entrypoint & onboarding 
- Add smoke vs. regression suites.  
- Run in CI (Jenkins).  

---

This is a **first QA automation setup**. It’s modular and can grow into a full CI-ready test system.