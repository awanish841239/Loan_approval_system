# 🏦 Loan Approval Prediction System

## 📌 Overview
A Machine Learning web application that predicts whether a loan 
will be approved or rejected based on applicant financial details. 
Built using Logistic Regression with Feature Engineering and 
deployed via Streamlit.

---

## 🤖 Models Compared

### ✅ With Feature Engineering
| Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---|---|
| **Logistic Regression** ⭐ | **87.5%** | **0.790** | **0.803** | **0.796** |
| KNN | 75.5% | 0.620 | 0.508 | 0.550 |
| Naive Bayes | 86.0% | 0.780 | 0.776 | 0.776 |

✅ **Best Model: Logistic Regression (with Feature Engineering)**

---

## 🔧 Features Used
- Applicant & Co-applicant Income
- Age, Dependents, Existing Loans
- Savings, Collateral Value
- Loan Amount & Loan Term
- Credit Score & DTI Ratio
- Employment Status, Education Level
- Gender, Marital Status
- Property Area, Loan Purpose
- Employer Category

---

## ⚙️ Feature Engineering Applied
- `DTI_Ratio_sq` = DTI_Ratio²
- `Credit_Score_sq` = Credit_Score²
- One-Hot Encoding on categorical variables

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/yourusername/loan-approval-prediction
cd loan-approval-prediction
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Live Demo
[Click Here to Try the App](https://loanapprovalsystem-h3xvxuqdehq5rxrpqhcngp.streamlit.app/)  


---

## 🛠️ Tech Stack
Python , Numpy, Pandas, Matplotlib, scikit-learn ,Streamlit

## 📁 Project Structure
```
loan-approval-prediction/
├── app.py                        # Streamlit web app
├── loan_approval_model.pkl       # Trained Logistic Regression model
├── requirements.txt              # Dependencies
└── README.md                     # Project documentation
```

---

## 👨‍💻 Author
Awanish | Bsc Physics Honours,BHU varanasi [Linkedin]()
**Awanish** | BSc Physics Honours, BHU Varanasi  
[GitHub](#) • [LinkedIn](#)
