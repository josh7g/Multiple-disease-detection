# Multiple-disease-detection

Introduction:
This project aims to predict heart disease and diabetes outcomes using machine learning models. The project includes data retrieval, model development, and the creation of a Streamlit web application for interactive visualization and prediction.

Steps Undertaken:
1. Data Retrieval
I gathered health data related to heart diseases and diabetes from online sources. The datasets included relevant parameters such as age, blood pressure, cholesterol levels, and more.

2. Data Preprocessing
Before training the models, the collected data underwent preprocessing to ensure it was suitable for machine learning. This included handling missing values, normalizing or scaling features, and encoding categorical variables.

3. Heart Disease Prediction
Logistic Regression Model

I developed a Logistic Regression model to predict the likelihood of heart disease. The following steps were taken:

Feature Selection: After analyzing the dataset, I selected relevant features that could contribute to predicting heart disease outcomes.
Model Training: I split the dataset into training and testing sets, and trained the Logistic Regression model using the training data.
Model Evaluation: The model's accuracy was evaluated using the testing dataset. The achieved accuracy was approximately 85%.
4. Diabetes Prediction
Support Vector Machine (SVM) Model

For predicting diabetes outcomes, I chose to use a Support Vector Machine model. The process involved the following steps:

Feature Engineering: Similar to the heart disease model, I selected pertinent features for diabetes prediction.
Data Splitting: The dataset was split into training and testing sets.
Model Training: The Support Vector Machine model was trained on the training data.
Model Assessment: The accuracy of the SVM model was evaluated using the testing data, achieving an accuracy of around 77%.
5. Streamlit Web App
I incorporated the trained models into a Streamlit web application to provide an interactive platform for users. The app allows users to input relevant health parameters and receive predictions for heart disease and diabetes outcomes. The app's interface is user-friendly and facilitates easy exploration of the predictive models.

Usage

Clone this repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Run the Streamlit app by executing streamlit run app.py in your terminal.
Input the required health parameters in the app's interface to receive predictions for heart disease and diabetes outcomes.
Conclusion

This project showcases the process of collecting health data, developing accurate predictive models for heart disease and diabetes, and creating an interactive Streamlit web application for real-world usage. The achieved accuracy rates of 85% for heart disease prediction and 77% for diabetes prediction demonstrate the effectiveness of the models.

Feel free to explore the code and adapt it to your own needs. If you have any questions or feedback, please don't hesitate to contact me.

