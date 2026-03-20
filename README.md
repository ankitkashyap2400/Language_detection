🚀 Overview

This project is a Machine Learning / NLP / Web App built using Python and Streamlit. It allows users to:

Detect language from text

Predict using trained ML models

Interact through a simple UI

🛠️ Tech Stack

Python 

Streamlit 


Scikit-learn 

Pandas & NumPy 

Pickle (for model saving)

📂 Project Structure
├── app.py                 # Streamlit app
├── vectorizer.pkl        # Saved vectorizer
├── model.pkl             # Trained model
├── label_encoder.pkl     # Label encoder
└── README.md             # Documentation
⚙️ Installation



Install dependencies:

pip install -r requirements.txt
▶️ Run the App
streamlit run app.py
💡 Features

✅ Real-time prediction

✅ Clean UI with Streamlit

✅ Multiple ML models support

✅ Easy to extend

🧠 Models Used

Logistic Regression

Naive Bayes

Support Vector Machine
⚠️ Common Errors & Fix
❌ FileNotFoundError: vectorizer.pkl

Solution:
Make sure these files are present:

vectorizer.pkl

label_encoder.pkl

model.pkl

Or retrain and save:

import pickle
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
📊 Example Usage

Input:

Bonjour tout le monde

Output:

Predicted Language: French
🤝 Contributing

Feel free to fork this repo and improve it. Pull requests are welcome!

Your Name

Ankit kumar
