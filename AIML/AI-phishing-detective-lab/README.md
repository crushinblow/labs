# 🛡️ AI Phishing Detection System

An end-to-end NLP-based phishing email detection system built using TF-IDF and Logistic Regression, with an additional hybrid rule-based scoring layer to simulate real-world layered security.

---

## 📌 Project Objective

To design, train, evaluate, and deploy a machine learning model capable of detecting phishing emails based on textual patterns and linguistic signals.

This project demonstrates:
- Natural Language Processing (NLP)
- Feature engineering with TF-IDF
- Supervised machine learning (Logistic Regression)
- Model evaluation (precision, recall, F1-score, confusion matrix)
- Hybrid ML + rule-based risk scoring
- Deployment using Streamlit

---

## 🧠 How It Works

### 1️⃣ Text Vectorization (TF-IDF)
Email text is converted into numerical feature vectors using:

- **Term Frequency (TF)** – words that appear more frequently in an email get higher weight.
- **Inverse Document Frequency (IDF)** – common words across all emails get lower weight.
- **N-grams (1-2 grams)** – captures patterns like “click here”.

---

### 2️⃣ Logistic Regression Classifier

The model learns weights for each feature during training and predicts the probability that an email is phishing.

Default decision threshold: 0.5

---

### 3️⃣ Hybrid Risk Scoring Layer

To simulate layered security defense, a rule-based scoring system adds additional risk points based on suspicious patterns such as:

- "urgent action required"
- "verify your account"
- "click here"
- presence of URLs
- account suspension wording

Final verdict categories:
- LEGITIMATE
- SUSPICIOUS
- PHISHING

---

## 📊 Model Performance (Test Set)

Dataset: ealvaradob/phishing-dataset (HuggingFace)

Results on unseen test data:

- Accuracy: **96%**
- Phishing Precision: **98%**
- Phishing Recall: **92%**
- F1-score: **0.95**

Confusion Matrix Summary:

- True Positives: 1334
- False Negatives: 121
- False Positives: 31
- True Negatives: 2242

The model demonstrates strong generalization performance with low false positive rates and high phishing detection accuracy.

---

## 🛠 Tech Stack

- Python
- scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Streamlit
- Joblib

---

## 🚀 Deployment

This project includes a Streamlit web application where users can:

1. Paste an email message
2. Receive phishing probability
3. View hybrid risk score
4. Get final verdict

---

## 📂 Project Structure
AI-phishing-detective-lab/
│
├── app.py
├── phishing_model.joblib
├── requirements.txt
├── README.md
└── notebook.ipynb (model training)

---

## 🔮 Future Improvements

- Threshold tuning to reduce false negatives
- Character-level n-grams for URL detection
- Ensemble models (Random Forest / XGBoost)
- Transformer-based model (e.g., BERT)
- Real-time API integration

---

## 🎯 Key Learning Outcomes

- Understanding of supervised ML workflow
- Feature engineering for NLP
- Evaluation metrics in cybersecurity context
- Trade-off between recall and false positives
- Model deployment best practices

---

## 📎 Chunyao

Built as part of applied AI/ML lab work focusing on practical cybersecurity use cases.