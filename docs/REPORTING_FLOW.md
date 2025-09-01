# Smishing Detection Reporting Flow

This document outlines how flagged messages can be handled responsibly.  
It is intended to demonstrate alignment with ethical standards and Malawi’s cyber guidelines.

---

## 1. Detection Process

1. **Message Input**  
   - User sends SMS/WhatsApp message to the bot or runs a script with a message.

2. **Detection Stage**  
   - Rule-based detection checks for local scam patterns.
   - ML classifier provides secondary verification.

3. **Logging**  
   - Detected messages are logged in `demo/sample_alert.log` for reference.
   - Include: message content (anonymized if needed), detection type (rule/ML), timestamp.

---

## 2. Reporting Options

1. **User Education**
   - Notify user: "⚠️ Likely smishing! Be careful."
   - Provide tips to avoid scams (e.g., never share PINs, confirm with official channels).

2. **Community Reporting**
   - Users can forward suspicious messages to **mwCERT** via official portal/email.
   - Include anonymized content and time of detection.

3. **Internal Review**
   - Collect flagged messages to analyze trends and improve rules/ML models.
   - Use only synthetic or anonymized data when sharing externally.

---

## 3. Ethical Guidelines

- Do not connect to real mobile money systems without authorization.
- Do not store sensitive personal information.
- This project is for **educational and demonstration purposes** only.
- Always align detection and reporting with Malawi’s **Electronic Transactions and Cyber Security Act (2016)** and mwCERT guidance.

---

## 4. Optional Enhancements

- Auto-generate weekly trend reports for demonstration purposes.
- Visualize flagged message counts over time using dashboards (e.g., Grafana or Jupyter plots).
- Extend bot to include educational messages for new users.
