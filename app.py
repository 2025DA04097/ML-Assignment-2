import streamlit as st
import pandas as pd
import joblib

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    matthews_corrcoef,
    roc_auc_score,
    confusion_matrix
)

st.title("Machine Learning Classification Dashboard")

uploaded_file = st.file_uploader(
    "Upload Test Data CSV",
    type=["csv"]
)

model_option = st.selectbox(
    "Choose Model",
    [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Naive Bayes",
        "Random Forest"
    ]
)

model_files = {
    "Logistic Regression":"logistic_regression.pkl",
    "Decision Tree":"decision_tree.pkl",
    "KNN":"knn.pkl",
    "Naive Bayes":"naive_bayes.pkl",
    "Random Forest":"random_forest.pkl"
}

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    X = df.drop("target", axis=1)
    y = df["target"]

    model = joblib.load(model_files[model_option])

    y_pred = model.predict(X)

    y_prob = model.predict_proba(X)[:,1]

    st.subheader("Evaluation Metrics")

    st.write("Accuracy:", round(accuracy_score(y, y_pred),4))
    st.write("Precision:", round(precision_score(y, y_pred),4))
    st.write("Recall:", round(recall_score(y, y_pred),4))
    st.write("F1 Score:", round(f1_score(y, y_pred),4))
    st.write("AUC:", round(roc_auc_score(y, y_prob),4))
    st.write("MCC:", round(matthews_corrcoef(y, y_pred),4))

    st.subheader("Confusion Matrix")

    cm = confusion_matrix(y, y_pred)

    st.write(cm)