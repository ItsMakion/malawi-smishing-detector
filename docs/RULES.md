# Smishing Detector Rules

This document explains the detection rules used in the Malawi Smishing Detector project.  
The rules are designed to flag SMS or WhatsApp messages that could be part of mobile money scams (Airtel Money, TNM Mpamba) or other local phishing attacks.

---

## 1. Rule Categories

### 1.1 English Keywords
| Pattern | Description |
|---------|-------------|
| `verify (your )?PIN` | Common in fake messages asking users to verify their account PIN |
| `claim (your )?(money|funds|award)` | Attempts to lure victims to click links or reveal credentials |
| `Mpamba` | Mentions the TNM mobile money service, often in scams |
| `Airtel` | Mentions Airtel Money in suspicious context |
| `update` | Requests action under the guise of account updates |
| `agent` | Refers to fake “agents” claiming to assist with funds |

### 1.2 Chichewa Keywords
| Pattern | Description |
|---------|-------------|
| `fufufuza` | Means “check/investigate,” often used in scams |
| `pereke` | Means “send/give,” frequently appears in social engineering attempts |
| `kulipira` | Means “pay,” may be used in fake payment requests |

---

## 2. Detection Logic

1. Each message is converted to lowercase for uniform scanning.
2. Patterns are matched using regular expressions.
3. If **any pattern matches**, the message is flagged as **smishing**.
4. If no pattern matches, the message is passed to the ML classifier for secondary analysis.

---

## 3. Notes

- These rules are **educational and demonstrative**; they are not exhaustive.
- Keywords are chosen based on **common mobile money scams in Malawi**.
- Additional rules can be added to expand coverage or adapt to new threats.
