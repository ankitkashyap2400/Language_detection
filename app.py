import streamlit as st
import pickle

# Load models (make sure these files exist)
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("lr_model.pkl", "rb"))   # you can change model
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

# Title
st.title("🌍 Language Detection App")

# Input
user_input = st.text_area("Enter text here:")

# Button
if st.button("Detect Language"):
    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        # Preprocess
        text = user_input.lower()
        text_vec = vectorizer.transform([text])

        # Prediction
        pred = model.predict(text_vec)
        result = label_encoder.inverse_transform(pred)[0]

        # Output
        st.success(f"Detected Language: {result}")