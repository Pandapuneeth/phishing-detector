# app.py

import streamlit as st
import pandas as pd
import joblib
from email_utils import clean_email

# Load model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.set_page_config(page_title="Phishing Email Classifier", layout="centered")
st.title("🛡️ Cybersecurity Phishing Email Classifier")

st.markdown("Upload an email or dataset to detect potential phishing attacks using AI.")

# 📝 Single email input
st.subheader("📧 Check a Single Email")
email_text = st.text_area("Paste the email text here:")

if st.button("Analyze Email"):
    if email_text.strip() == "":
        st.warning("Please paste some email content.")
    else:
        clean_text = clean_email(email_text)
        vect = vectorizer.transform([clean_text])
        prediction = model.predict(vect)[0]
        proba = model.predict_proba(vect).max()

        label = "🚨 Phishing" if prediction == "phishing" else "✅ Legit"
        st.markdown(f"**Prediction:** {label} ({proba*100:.2f}% confidence)")

# 📁 Batch upload
st.subheader("📂 Upload CSV of Emails")
csv_file = st.file_uploader("Upload CSV file with a column named 'text'", type=["csv"])

if csv_file:
    try:
        df = pd.read_csv(csv_file)
        df["clean_text"] = df["text"].astype(str).apply(clean_email)
        X = vectorizer.transform(df["clean_text"])
        df["Prediction"] = model.predict(X)

        st.success("Detection complete!")
        st.dataframe(df[["text", "Prediction"]])

        # Download result
        csv = df[["text", "Prediction"]].to_csv(index=False).encode("utf-8")
        st.download_button("Download Results", csv, "classified_emails.csv", "text/csv")

    except Exception as e:
        st.error(f"Error: {e}")
