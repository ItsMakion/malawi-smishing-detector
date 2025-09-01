import re

# Keywords for English & Chichewa
SMISH_KEYWORDS = [
    r"verify (your )?PIN",
    r"claim (your )?(money|funds|award)",
    r"Mpamba",
    r"Airtel",
    r"update",
    r"agent",
    # Chichewa examples
    r"fufufuza",
    r"pereke",
    r"kulipira",
]

def is_smishing(text):
    text_lower = text.lower()
    for pattern in SMISH_KEYWORDS:
        if re.search(pattern, text_lower):
            return True
    return False

if __name__ == "__main__":
    test_msgs = [
        "Airtel: Please verify your PIN to avoid service interruption",
        "Hey, long time no see! Let's catch up tomorrow."
    ]
    for msg in test_msgs:
        print(f"Message: {msg} → Smishing? {is_smishing(msg)}")
