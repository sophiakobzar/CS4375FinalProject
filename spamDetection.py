import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

# Load the new dataset
try:
    spam = pd.read_csv('spam_ham_dataset.csv')
except FileNotFoundError:
    print("The file 'spam_ham_dataset.csv' does not exist in the current directory.")
    exit()

# No need for feature engineering in this case as we don't have an 'emailText' column

X = spam['text']  # Email text
y = spam['label_num']  # Labels (spam or ham)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a CountVectorizer to convert text into numerical features
vectorizer = CountVectorizer()
X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

# Initialize a Linear SVM model
model_linear = svm.SVC(kernel='linear')

# Train the model
model_linear.fit(X_train_features, y_train)

# Evaluate accuracy on the test set
accuracy_linear = model_linear.score(X_test_features, y_test)
print(f"Linear SVM Accuracy: {accuracy_linear:.2f}")

# Print a classification report
y_pred_linear = model_linear.predict(X_test_features)
print(classification_report(y_test, y_pred_linear))

# Get the instances where the Linear SVM model made errors
errors = X_test[y_test != y_pred_linear]

print("instances where the Linear SVM model made errors")
# Print the errors
print(errors)

# Initialize a Kernel SVM model
model_rbf = svm.SVC(kernel='rbf')

# Train the model
model_rbf.fit(X_train_features, y_train)

# Evaluate accuracy on the test set
accuracy_rbf = model_rbf.score(X_test_features, y_test)
print(f"\nKernel SVM Accuracy: {accuracy_rbf:.2f}")

# Print a classification report
y_pred_rbf = model_rbf.predict(X_test_features)
print(classification_report(y_test, y_pred_rbf))

# Get the instances where the Kernel SVM model made errors
errors_kernel = X_test[y_test != y_pred_rbf]
print("\ninstances where the Kernel SVM model made errors")
# Print the errors
print(errors_kernel)

print()
# Define the parameter grid
# This is a dictionary that contains the parameters we want to tune and their respective values we want to try out.
#param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001]}

# Initialize a GridSearchCV object
#grid = GridSearchCV(svm.SVC(kernel='rbf'), param_grid, refit=True, verbose=2)

# Fit the model to the training data
#grid.fit(X_train_features, y_train)

# Print the best parameters
#print(grid.best_params_)

# Initialize a Kernel SVM model with the best parameters
best_model = svm.SVC(kernel='rbf', C=100, gamma=0.001)

# Train the model
best_model.fit(X_train_features, y_train)

# Evaluate accuracy on the test set
accuracy_best = best_model.score(X_test_features, y_test)
print(f"Best Model Accuracy: {accuracy_best:.2f}")

# Print a classification report
y_pred_best = best_model.predict(X_test_features)
print(classification_report(y_test, y_pred_best))

# Get the instances where the best model made errors
errors_best = X_test[y_test != y_pred_best]

# Print the errors
print("Instances where the best model made errors:")
print(errors_best)
