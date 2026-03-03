{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww12720\viewh7800\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import joblib\
\
# Load trained model\
model = joblib.load("phishing_model.joblib")\
\
st.title("\uc0\u55357 \u57057 \u65039  AI Phishing Detection System")\
st.write("Paste an email below to check if it is phishing.")\
\
email_text = st.text_area("Enter email text here")\
\
if st.button("Analyze Email"):\
    if email_text.strip() == "":\
        st.warning("Please enter email content.")\
    else:\
        prob = model.predict_proba([email_text])[0][1]\
        verdict = "PHISHING" if prob >= 0.5 else "LEGITIMATE"\
\
        st.subheader("Result:")\
        st.write(f"Phishing Probability: \{prob:.3f\}")\
        st.write(f"Verdict: **\{verdict\}**")}