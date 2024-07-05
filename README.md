# Customer Churn Prediction
> Author: Michael King Sutanto
---
### Project Overview
In this project, I developed a machine learning model to predict customer churn using various customer-related features. The Flask app provides an easy-to-use interface for users to input customer data and receive predictions on whether a customer is likely to churn.  

This project encompasses a wide range of skills and technologies, including SQL queries, data visualization, building classification machine learning models, creating a Flask app with Python, HTML, and CSS, utilizing Docker, and deploying the application on AWS. Additionally, I set up an API to provide programmatic access to the model. I also built a CI/CD pipeline using GitHub Actions to automate the deployment process.

---
### Model
The final model chosen for deployment was the CatBoostClassifier due to its superior performance in terms of ROC-AUC score.
- **ROC-AUC Score**: 0.9148

---
### Deployment
The Flask web application was packaged using Docker and is hosted on AWS.

Users can input customer data through the web interface, and the app will return a prediction indicating whether the customer is likely to churn.

To use the Flask app, follow these steps:
1. Access the Flask app at [ec2-13-239-114-113.ap-southeast-2.compute.amazonaws.com/](http://ec2-13-239-114-113.ap-southeast-2.compute.amazonaws.com/).
2. Enter the customer details into the provided form.
3. Click the "Predict" button to receive the churn prediction. <br><br>

Additionally, the model can be accessed using API. This allows for programmatic queries and integration with other systems. For sample code on how to query the API, please refer to the `notebooks/api_query_example.ipynb` file.