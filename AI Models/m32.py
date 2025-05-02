import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns

# Simulate a final training dataset for the AI model
X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, n_classes=2, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the final AI model using Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# Visualizing the performance metrics
def plot_performance(accuracy, cm):
    # Accuracy Plot
    plt.figure(figsize=(12, 8))
    plt.subplot(1, 2, 1)
    plt.bar(['Accuracy'], [accuracy], color='green')
    plt.title(f'Model Accuracy: {accuracy * 100:.2f}%')
    plt.ylim(0, 1)

    # Confusion Matrix Plot
    plt.subplot(1, 2, 2)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Class 0', 'Class 1'], yticklabels=['Class 0', 'Class 1'])
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.tight_layout()
    plt.show()

# Display the performance plots
plot_performance(accuracy, cm)

# Save the trained model
import joblib
joblib.dump(model, 'final_ai_model.joblib')

# Simulate model deployment (Load the saved model and make predictions)
loaded_model = joblib.load('final_ai_model.joblib')
new_data = np.random.rand(5, 20)  # Simulate some new data (5 samples, 20 features)
predictions = loaded_model.predict(new_data)
print(f"Predictions on new data: {predictions}")
