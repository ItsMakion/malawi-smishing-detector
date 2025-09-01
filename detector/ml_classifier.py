import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load sample data
messages = pd.read_csv("data/sample_messages.csv")
labels = pd.read_csv("data/labels.csv")

X = messages['message_text']
y = labels['label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ML pipeline
clf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('lr', LogisticRegression())
])

clf.fit(X_train, y_train)

# Test
y_pred = clf.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Function for predicting a single message
def predict_message(text):
    pred = clf.predict([text])[0]
    return pred

if __name__ == "__main__":
    print(predict_message("TNM Mpamba: You have received K2,500. Click link to claim."))
    print(predict_message("Lunch tomorrow?"))
