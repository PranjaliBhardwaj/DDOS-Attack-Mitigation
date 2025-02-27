import pytest
from src.data_preprocessing import generate_dataset, preprocess_data

def test_generate_dataset():
    data, labels = generate_dataset()
    assert len(data) == 10000
    assert len(labels) == 10000

def test_preprocess_data():
    X_train, X_test, y_train, y_test, scaler = preprocess_data()
    assert X_train.shape[0] == 8000
    assert X_test.shape[0] == 2000
