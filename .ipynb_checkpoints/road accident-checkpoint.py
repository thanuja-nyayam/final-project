import streamlit as st
import pickle

# Load the pre-trained model
loaded_model = pickle.load(open("accident_prediction.sav", "rb"))
# Define function to make predictions
def predict(data):
    prediction = loaded_model.predict(data)
    return prediction

# Streamlit app
def main():
    st.title("Accident_prediction Web App")
    
    # User input
    input_data = st.text_input("Enter some data:")
    
    # Make prediction
    if st.button("Predict"):
        result = predict(input_data)
        st.write("Prediction:", result)

if __name__ == "__main__":
    main()
