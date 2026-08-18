# ML-Assignment-2
# Problem Statement
The objective of this project is to compare the performance of multiple machine learning classification algorithms on a medical diagnosis dataset. The project involves model training, evaluation, visualization of results and deployment using Streamlit Community Cloud.
# Implemented models:

#	Model
1	Logistic Regression
2	Decision Tree Classifier
3	K-Nearest Neighbour (kNN) Classifier
4	Gaussian Naive Bayes
5	Random Forest Classifier
# Dataset Description
# Dataset Name: Breast Cancer Wisconsin Dataset
Source: UCI Machine Learning Repository / Scikit-Learn Dataset Library
### Number of Instances: 569
### Number of Features: 30
Target Classes:
Malignant
Benign
The dataset contains measurements computed from digitized images of breast mass samples. The objective is to classify tumors as malignant or benign

## Model performance

| Model | Accuracy | AUC | Precision | Recall | F1 | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9649 | 0.9954 | 0.9595 | 0.9861 | 0.9726 | 0.9245 |
| Decision Tree | 0.9123 | 0.9157 | 0.9559 | 0.9028 | 0.9286 | 0.8174 |
| KNN | 0.9123 | 0.9559 | 0.9429 | 0.9167 | 0.9296 | 0.8139 |
| Naive Bayes | 0.9386 | 0.9878 | 0.9452 | 0.9583 | 0.9517 | 0.8676 |
| Random Forest | 0.9561 | 0.9937 | 0.9589 | 0.9722 | 0.9655 | 0.9054 |
