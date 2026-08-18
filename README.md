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
# Observations
## Logistic Regression

Logistic Regression achieved the highest accuracy (96.49%) and MCC score (0.9245) among all evaluated models. The model demonstrated excellent classification capability with a very high AUC score of 0.9954, indicating strong discrimination between malignant and benign cases. The high recall value shows that the model successfully identified most positive cases.

## Decision Tree

Decision Tree provided reasonable performance with an accuracy of 91.23%. Although the model is highly interpretable and easy to visualize, it achieved the lowest AUC score among all models, suggesting a weaker ability to distinguish between classes compared to other techniques. The lower MCC value also indicates reduced prediction consistency.

## K-Nearest Neighbors (KNN)

KNN achieved the same accuracy as the Decision Tree model but delivered a significantly better AUC score of 0.9559. The model performed well in identifying similar patterns in the dataset; however, its overall predictive power remained lower than Logistic Regression and Random Forest.

## Naive Bayes

Naive Bayes achieved strong performance despite its assumption of feature independence. With an accuracy of 93.86% and an AUC of 0.9878, the model demonstrated robust classification ability while remaining computationally efficient and simple to implement.

## Random Forest

Random Forest delivered excellent results across all evaluation metrics. The model achieved an accuracy of 95.61%, a high AUC score of 0.9937, and strong precision and recall values. The ensemble approach effectively reduced overfitting and improved generalization, making it one of the most reliable models in this study.

# Overall Winner

Although Random Forest performed exceptionally well, Logistic Regression achieved the highest Accuracy (96.49%), highest F1 Score (0.9726), highest Recall (0.9861), highest AUC (0.9954), and highest MCC (0.9245). Therefore, Logistic Regression is considered the best-performing model for the Breast Cancer Wisconsin Dataset used in this project.
# Git hub repository link - https://github.com/2025DA04097/ML-Assignment-2

# Conclusion

This project evaluated five machine learning classification algorithms on the Breast Cancer Wisconsin Dataset. The models were assessed using Accuracy, AUC, Precision, Recall, F1-Score, and Matthews Correlation Coefficient (MCC). All models achieved satisfactory performance, with Logistic Regression and Random Forest producing the best results. Logistic Regression emerged as the overall best-performing model due to its superior predictive accuracy, robustness, and excellent class discrimination capability. The results demonstrate that machine learning techniques can effectively support breast cancer diagnosis and classification tasks.
