import time
import numpy as np
from src.mitigation import mitigate_attack

def simulate_traffic(model, scaler):
    """
    Simulate real-time traffic and detect DDoS attacks.
    """
    print("Simulating real-time traffic...")
    while True:
        # Simulate incoming traffic (replace with real-time data)
        packet_rate = np.random.randint(100, 1000)
        byte_rate = np.random.randint(500, 5000)
        protocol_type = np.random.randint(0, 3)
        duration = np.random.uniform(0.1, 10.0)
        
        # Preprocess input
        traffic = np.array([[packet_rate, byte_rate, protocol_type, duration]])
        traffic = scaler.transform(traffic)
        
        # Predict using the model
        prediction = model.predict(traffic)
        
        if prediction == 1:
            print(f"DDoS Attack Detected! Packet Rate: {packet_rate}, Byte Rate: {byte_rate}")
            mitigate_attack()
        else:
            print(f"Normal Traffic. Packet Rate: {packet_rate}, Byte Rate: {byte_rate}")
        
        time.sleep(1)  # Simulate delay between traffic samples
