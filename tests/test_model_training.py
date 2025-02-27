import pytest
from src.model_training import train_model
from src.data_preprocessing import preprocess_data

def test_train_model():
    X_train, X_test, y_train, y_test, _ = preprocess_data()
    model = train_model(X_train, y_train)
    assert model is not None
