import streamlit as st
import pickle
import numpy as np

#  Page Config 
st.set_page_config(
    page_title="Loan Approval System",
    page_icon="🏦",
    layout="centered"
)

# Load Model 
@st.cache_resource
def load_model():
    with open('loan_approval_model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

# ─ UI
st.title("🏦 Loan Approval System")
st.markdown("Fill in the details below to check loan eligibility.")
st.divider()

# ── Numeric Inputs 
col1, col2 = st.columns(2)

with col1:
    applicant_income    = st.number_input("Applicant Income (₹)", min_value=0)
    age                 = st.number_input("Age", min_value=18, max_value=100)
    existing_loans      = st.number_input("Existing Loans", min_value=0)
    loan_amount         = st.number_input("Loan Amount (₹)", min_value=0)
    dti_ratio           = st.number_input("DTI Ratio", min_value=0.0, format="%.4f")

with col2:
    coapplicant_income  = st.number_input("Co-applicant Income (₹)", min_value=0)
    dependents          = st.number_input("Dependents", min_value=0)
    savings             = st.number_input("Savings (₹)", min_value=0)
    loan_term           = st.number_input("Loan Term (months)", min_value=1)
    credit_score        = st.number_input("Credit Score", min_value=300, max_value=900)
    collateral_value    = st.number_input("Collateral Value (₹)", min_value=0)

st.divider()

# ── Dropdown Inputs 
col3, col4 = st.columns(2)

with col3:
    gender              = st.selectbox("Gender", ["Male", "Female"])
    employment_status   = st.selectbox("Employment Status", ["Salaried", "Self-employed", "Unemployed"])
    loan_purpose        = st.selectbox("Loan Purpose", ["Car", "Education", "Home", "Personal"])

with col4:
    education_level     = st.selectbox("Education Level", ["Graduate", "Non Graduate"])
    marital_status      = st.selectbox("Marital Status", ["Single", "Married"])
    property_area       = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])
    employer_category   = st.selectbox("Employer Category", ["Government", "MNC", "Private", "Unemployed"])

st.divider()

# ── Feature Engineering 
def prepare_input():
    dti_ratio_sq    = dti_ratio ** 2
    credit_score_sq = credit_score ** 2

    # One-Hot Encoding
    emp_salaried        = 1 if employment_status == "Salaried"      else 0
    emp_self            = 1 if employment_status == "Self-employed"  else 0
    emp_unemployed      = 1 if employment_status == "Unemployed"     else 0

    marital_single      = 1 if marital_status == "Single"           else 0

    area_semiurban      = 1 if property_area == "Semiurban"         else 0
    area_urban          = 1 if property_area == "Urban"             else 0

    purpose_car         = 1 if loan_purpose == "Car"                else 0
    purpose_education   = 1 if loan_purpose == "Education"          else 0
    purpose_home        = 1 if loan_purpose == "Home"               else 0
    purpose_personal    = 1 if loan_purpose == "Personal"           else 0

    employer_govt       = 1 if employer_category == "Government"    else 0
    employer_mnc        = 1 if employer_category == "MNC"           else 0
    employer_private    = 1 if employer_category == "Private"       else 0
    employer_unemployed = 1 if employer_category == "Unemployed"    else 0

    gender_male         = 1 if gender == "Male"                     else 0

    # Education (binary)
    education_graduate  = 1 if education_level == "Graduate"        else 0

    # Final array — same order as X_train columns
    features = [
        applicant_income, coapplicant_income, age, dependents,
        existing_loans, savings, collateral_value, loan_amount,
        loan_term, education_graduate,
        emp_salaried, emp_self, emp_unemployed,
        marital_single,
        area_semiurban, area_urban,
        purpose_car, purpose_education, purpose_home, purpose_personal,
        employer_govt, employer_mnc, employer_private, employer_unemployed,
        gender_male,
        dti_ratio_sq, credit_score_sq
    ]
    return np.array(features).reshape(1, -1)

# ─ Predict Button 
if st.button("🔍 Check Loan Eligibility", use_container_width=True):
    input_data = prepare_input()
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    st.divider()
    if prediction == 1:
        st.success(f"✅ Loan APPROVED! (Confidence: {probability[1]*100:.1f}%)")
    else:
        st.error(f"❌ Loan REJECTED (Confidence: {probability[0]*100:.1f}%)")