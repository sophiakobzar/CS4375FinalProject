import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

# Read the CSV file (adjust the file path)
spam = pd.read_csv('spam.csv')

# Split data into features (email text) and labels (spam or ham)
X = spam['v2']  # Email text
y = spam['v1']  # Labels (spam or ham)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a CountVectorizer to convert text into numerical features
vectorizer = CountVectorizer()
X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

# Initialize an SVM model
model = svm.SVC()

# Train the model
model.fit(X_train_features, y_train)

# Evaluate accuracy on the test set
accuracy = model.score(X_test_features, y_test)
print(f"Accuracy: {accuracy:.2f}")
