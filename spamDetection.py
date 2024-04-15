import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier

# Load the new dataset
try:
    spam = pd.read_csv('spam_ham_dataset.csv')
except FileNotFoundError:
    print("The file 'spam_ham_dataset.csv' does not exist in the current directory.")
    exit()

X = spam['text']  # Email text
y = spam['label_num']  # Labels (spam or ham)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a CountVectorizer to convert text into numerical features
vectorizer = CountVectorizer()
X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

# Define models
models = {
    1: svm.SVC(kernel='linear'),
    2: svm.SVC(kernel='rbf'),
    3: MLPClassifier(hidden_layer_sizes=(3,), activation='relu', solver='adam', max_iter=75, random_state=42),
    4: MLPClassifier(hidden_layer_sizes=(10,), activation='relu', solver='adam', max_iter=100, random_state=42)
}

while True:
    # Ask the user which model they want to run
    print("Please select a model to run:")
    print("1: Linear SVM")
    print("2: Kernel SVM")
    print("3: Feedforward Neural Network")
    print("4: Best Model (Takes about 15-30 seconds)")
    print("5: Exit")

    # Get the user's choice
    choice = int(input("Your choice: "))

    # If the user chooses to exit
    if choice == 5:
        print("Exiting the program.")
        break

    # If the user chooses a valid model
    elif choice in [1, 2, 3, 4]:
        # Get the chosen model
        model = models[choice]

        # Train the model
        model.fit(X_train_features, y_train)

        # Evaluate accuracy on the test set
        accuracy = model.score(X_test_features, y_test)
        print(f"Model Accuracy: {accuracy:.5f}")

        # Print a classification report
        y_pred = model.predict(X_test_features)
        print(classification_report(y_test, y_pred))

        # Get the instances where the model made errors
        errors = X_test[y_test != y_pred]
        print("Instances where the model made errors:")
        print(errors)
        print()
    # If the user chooses an invalid option
    else:
        print("Invalid choice. Please choose a number between 1 and 5.")