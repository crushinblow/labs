import streamlit as st
import joblib
import re
from pathlib import Path

# Load model
HERE = Path(__file__).parent
MODEL_PATH = HERE / "phishing_model.joblib"
model = joblib.load(MODEL_PATH)


def hybrid_phishing_score(email_text, ml_model):
    # ML probability
    ml_prob = float(ml_model.predict_proba([email_text])[0][1])
    ml_score = ml_prob * 60

    # Rule-based scoring
    rule_score = 0
    text_lower = email_text.lower()

    rules = {
        'urgent action required': 10,
        'verify your account':    10,
        'click here':              8,
        'password':                7,
        'bank account':            8,
        'limited time':            6,
        'congratulations you won':10,
        'suspend':                 7,
        'unusual activity':        8,
    }

    for phrase, score in rules.items():
        if phrase in text_lower:
            rule_score += score

    # URL detection
    if re.search(r'http[s]?://', text_lower):
        rule_score += 10

    rule_score = min(rule_score, 40)
    total_score = float(ml_score + rule_score)

    if total_score >= 60:
        verdict = 'PHISHING'
    elif total_score >= 35:
        verdict = 'SUSPICIOUS'
    else:
        verdict = 'LEGITIMATE'

    return {
        'ml_probability': round(ml_prob, 3),
        'ml_score':       round(ml_score, 1),
        'rule_score':     round(rule_score, 1),
        'total_score':    round(total_score, 1),
        'verdict':        verdict
    }


# ── UI ──────────────────────────────────────────
st.title("AI Phishing Email Detector")

email_text = st.text_area("Paste email text here:", height=200)

if st.button("Check Email"):
    if email_text.strip() == "":
        st.warning("Please enter some email text.")
    else:
        result = hybrid_phishing_score(email_text, model)

        st.subheader("Result:")
        st.write(f"**Verdict:** {result['verdict']}")
        st.write(f"**Total Score:** {result['total_score']} / 100")
        st.write(f"**ML Score:** {result['ml_score']} / 60")
        st.write(f"**Rule Score:** {result['rule_score']} / 40")
        st.write(f"**ML Probability:** {result['ml_probability']}")
