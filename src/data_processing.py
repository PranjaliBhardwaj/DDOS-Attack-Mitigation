import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def generate_dataset(num_samples=10000):
    """
    Generate a synthetic dataset for DDoS detection.
    """
    np.random.seed(42)
    packet_rate = np.random.randint(100, 1000, num_samples)
    byte_rate = np.random.randint(500, 5000, num_samples)
    protocol_type = np.random.randint(0, 3, num_samples)  # 0: TCP, 1: UDP, 2: ICMP
    duration = np.random.uniform(0.1, 10.0, num_samples)
    
    # Simulate DDoS traffic (higher packet_rate and byte_rate)
    labels = np.zeros(num_samples)
    labels[(packet_rate > 800) & (byte_rate > 4000)] = 1
    
    data = np.column_stack((packet_rate, byte_rate, protocol_type, duration))
    return data, labels

def preprocess_data():
    """
    Preprocess the dataset: normalize and split into train/test sets.
    """
    data, labels = generate_dataset()
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test, scaler
