## Student Attendance Risk Predictor

Status: Completed | Academic Machine Learning Project
Author: Vaibhav Dabade  

A Machine Learning project that predicts whether a student is at risk of detention based on attendance data.  
The model is trained using synthetic academic records and deployed through an interactive Streamlit web application.


## Project Overview

This project analyzes student attendance patterns and classifies whether a student is likely to fall below the required 75% attendance threshold.  
It also includes a built-in attendance calculator to determine the minimum number of classes required to maintain eligibility.


## Features

- 75% Attendance Requirement Calculator  
- Risk Prediction using Random Forest Classifier  
- 98% Model Accuracy  
- Interactive Streamlit Web Application  


## Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  
- Joblib  


## Model Performance

- Accuracy: 98%  
- Balanced Precision and Recall  
- Trained on 500+ synthetic student records  


## Project Structure

```
Attendance_Risk_Predictor/
│
├── app/
│   └── app.py
│
├── database/
│   └── attendance_data.csv
│
├── model/
│   └── attendance_model.pkl
│
├── generate_dataset.py
├── train_model.py
└── requirements.txt
```

---

## How to Run

1. Install dependencies:
```
   pip install -r requirements.txt
 ```  

2. Generate dataset:
 ```  
   python generate_dataset.py
  ``` 

3. Train the model:
  ``` 
   python train_model.py
   ```

4. Launch the application:
  ``` 
   streamlit run app/app.py
   ```

## Application Preview

### Web Application Interface

![App Interface](assets/app_interface.png)

### Model Performance

![Model Accuracy](assets/model_accuracy.png)

---

## Future Improvements

- Deploy application to Streamlit Cloud
- Add real-world attendance dataset
- Implement additional ML models for comparison
- Add model evaluation visualization (confusion matrix, ROC curve)


