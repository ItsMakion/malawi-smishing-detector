# Malawi Smishing Detector

A lightweight SMS/WhatsApp smishing detector tailored for Malawi's mobile money ecosystem (Airtel Money, TNM Mpamba).  
Built with Python, scikit-learn, and rule-based detection. Includes a small demo bot and sample dataset.

---

## 🚨 Why this project?
Mobile money scams are one of the biggest cyber threats in Malawi. Attackers send fake SMS or WhatsApp messages like:
- "Verify your Airtel PIN to keep your account active"
- "TNM Mpamba: You have received K2,500. Click link to claim"
- Messages in Chichewa tricking users into sending codes or money

This tool shows how **local-language smishing detection** can work in practice.

---

## 🛠 How it works
1. **Dataset**  
   - `data/sample_messages.csv` → example SMS/WhatsApp messages (English & Chichewa).  
   - `data/labels.csv` → whether each is `ham` (safe) or `smishing`.

2. **Detection methods**
   - **Rule-based detector**: Looks for suspicious keywords/phrases (e.g. “verify PIN”, “Mpamba”, “agent”).  
   - **Machine learning model**: Uses scikit-learn (TF-IDF + Logistic Regression) to classify new messages.

3. **Demo bot**  
   - Simple Telegram bot that lets you paste a message.  
   - It replies with `Likely smishing` or `Looks safe`.  

4. **Notebook demo**  
   - `demo/notebook_demo.ipynb` → shows how to load data, train model, and test rules.

---

## 📊 Features
- Keyword-based detection with local language awareness (English + Chichewa).  
- Lightweight ML model (trainable in seconds).  
- Telegram bot demo for real-time message checks.  
- Documented rules in `docs/RULES.md`.  
- Reporting flow (`docs/REPORTING_FLOW.md`) → how a detected scam could be reported to **mwCERT**.

---

## 🔧 Installation
```bash
git clone https://github.com/YOURNAME/malawi-smishing-detector.git
cd malawi-smishing-detector
