import streamlit as st
import joblib
from pathlib import Path

HERE = Path(__file__).parent
MODEL_PATH = HERE / "phishing_model.joblib"

model = joblib.load(MODEL_PATH)

st.title("AI Phishing Email Detector")

email_text = st.text_area("Paste email text here:")

if st.button("Check Email"):
    if email_text.strip() == "":
        st.warning("Please enter some email text.")
    else:
        prob = model.predict_proba([email_text])[0][1]
        verdict = "PHISHING" if prob >= 0.5 else "LEGITIMATE"

        st.subheader("Result:")
        st.write(f"Phishing Probability: {prob:.3f}")
        st.write(f"Verdict: **{verdict}**")
