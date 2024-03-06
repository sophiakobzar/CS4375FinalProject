import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Check if the file exists
try:
    spam = pd.read_csv('spam.csv')
except FileNotFoundError:
    print("The file 'spam.csv' does not exist in the current directory.")
    exit()
    
# Feature Engineering
spam['email_length'] = spam['emailText'].apply(len)

X = spam[['emailText', 'email_length']]  # Email text and length
y = spam['labels']  # Labels (spam or ham)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a CountVectorizer to convert text into numerical features
vectorizer = CountVectorizer()
X_train_features = vectorizer.fit_transform(X_train['emailText'])
X_test_features = vectorizer.transform(X_test['emailText'])

# Add the new feature to the feature matrix
X_train_features = np.hstack((X_train_features.toarray(), X_train[['email_length']].values))
X_test_features = np.hstack((X_test_features.toarray(), X_test[['email_length']].values))

# Initialize a Random Forest model
model = RandomForestClassifier()

# Train the model
model.fit(X_train_features, y_train)

# Evaluate accuracy on the test set
accuracy = model.score(X_test_features, y_test)
print(f"Accuracy: {accuracy:.2f}")

# Print a classification report
y_pred = model.predict(X_test_features)
print(classification_report(y_test, y_pred))
