"AutoML Income Prediction System"

A fully automated machine learning engine that predicts whether a person earns more or less than 50K annually using multiple ML models and selects the best one automatically.

This project showcases:

Automated data preprocessing

Multiple ML model training

Auto-model selection

Full pipeline export

Optional Streamlit deployment

Perfect for Data Scientist, ML Engineer, and AI Engineer portfolios.

📌 Project Overview

This system takes the Adult Census Income dataset and automatically performs:

✔ Data Cleaning
✔ Feature Encoding & Scaling
✔ Training 7 ML Models
✔ Selecting the Best Model
✔ Saving the Final ML Pipeline
✔ Deploying a Streamlit Web App

No manual tuning required — the AutoML pipeline handles everything.

🧠 Tech Stack

Python 3

Pandas, NumPy

Scikit-Learn

XGBoost

Joblib

Streamlit

Matplotlib, Seaborn

🎯 Business Use Cases

Companies use this to predict whether someone earns > 50K for:

Credit card approval

Loan eligibility

Banking risk scoring

Income-based customer segmentation

Targeted marketing

📁 Project Structure
auto-ml-income/
│── app.py
│── model_training_notebook.ipynb   # optional
│── best_model.pkl                  # final chosen model
│── preprocessor.pkl                # preprocessing pipeline
│── requirements.txt
│── README.md

🧠 How the AutoML Engine Works
1️⃣ Data Preprocessing

Missing values filled

Numeric features scaled

Categorical features encoded

Full pipeline saved as preprocessor.pkl

2️⃣ Model Training

The system trains 7 models:

Algorithm	Status
Logistic Regression	✅
Decision Tree	✅
Random Forest	✅
Gradient Boosting	✅
Support Vector Machine	✅
KNN	✅
XGBoost	⭐ BEST
3️⃣ Model Selection

All models evaluated on:

Accuracy

Precision

Recall

F1 Score

Best Model: XGBoost — Accuracy: 84.8%

4️⃣ Model Saving

After training:

best_model.pkl
preprocessor.pkl


are exported, ready for deployment.

5️⃣ Streamlit App

User enters:

Age

Education Level

Working Hours

Capital gain/loss

Other attributes

The system predicts:

✔ Income > 50K
✘ Income ≤ 50K

▶️ Run This Project Locally
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run the Web App
streamlit run app.py

🌐 Deployment Guide (Optional)
Deploy to Streamlit Cloud:

Push repo to GitHub

Visit https://streamlit.io/cloud

Connect GitHub → Select repository

Set main file as:

app.py


Add environment file:

requirements.txt


Done! 🚀

📊 Example Prediction
Input Example	Output
Age: 45, Education-num: 13, Hours/week: 49	> 50K
Age: 23, Education-num: 9, Hours/week: 30	≤ 50K
🏁 Future Enhancements

Add SHAP explanations

Add AutoML hyperparameter tuning

Multiclass income bracket prediction

Add dataset explorer inside UI

API version using FastAPI

👩‍💻 Author

Lavisha Yadav — AI & ML Engineer

GitHub: https://github.com/lavcode23


LinkedIn: https://www.linkedin.com/in/lavishayadav-ai
