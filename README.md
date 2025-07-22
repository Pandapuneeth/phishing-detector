# 🛡️ Cybersecurity Phishing Email Classifier

An AI-powered Streamlit app that detects whether an email is a **phishing attack or a legit message**. Paste a single email or upload a CSV — get predictions in seconds. Perfect for cybersecurity demos, freelance gigs, and portfolio flex.

## 🚀 Features

- 📧 Paste an email to classify instantly
- 📂 Upload a CSV of emails and detect in batch
- 🎯 Detects phishing vs. legit emails with AI
- ⬇️ Download CSV with prediction results
- Built using Python, Streamlit, Scikit-learn

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn (Random Forest Classifier)
- TF-IDF Vectorizer
- Pandas

## 📁 File Structure

phishing-detector/
├── app.py
├── email_utils.py
├── phishing_model.pkl
├── vectorizer.pkl
├── train_model.py
├── sample_emails.csv
├── requirements.txt
└── README.md
├──output
   screenshot_1
   screenshot_2

## 📦 Installation

```bash
pip install -r requirements.txt
streamlit run app.py

🧪 Sample Usage
Paste this email to test:

Your account has been suspended. Click here to verify your details.

📬 Contact
🔗 GitHub: Pandapuneeth
📩 Open to freelance work & collaborations!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://phishing-detector-njkzerzsknrix3jhchdbzg.streamlit.app/)