from src.data_preprocessing import preprocess_data
from src.model_training import train_model, evaluate_model, save_model
from src.real_time_detection import simulate_traffic
from src.utils import setup_logging

def main():

    setup_logging()
  
    X_train, X_test, y_train, y_test, scaler = preprocess_data()
    

    model = train_model(X_train, y_train)
    

    evaluate_model(model, X_test, y_test)
    

    save_model(model)
    
 
    simulate_traffic(model, scaler)

if __name__ == "__main__":
    main()
