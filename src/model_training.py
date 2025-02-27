from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

def train_model(X_train, y_train):
    """
    Train a Random Forest classifier.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model's performance.
    """
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

def save_model(model, filename="models/random_forest.pkl"):
    """
    Save the trained model to a file.
    """
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")
