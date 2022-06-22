![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

# Customer_segmentation_using_Deep_Learning


# Results
After :


![model_acc](model_accuracy.png) 


Referring to the result it is clear that Logistic Regression with MinMax 
scaler has the highest score which is 0.835. Hence we pick model to best 
tested further to find the best parameter.As the result for gridsearch parameter, 
we found out that the default parameter is the best parameter for this case. 
Hence we save the model for deployment.

To further check the model we test model using our test data send. Below is the 
classification report and confusion matrix:

![class_report](classification_report.png)


![conf_mat](confusion_matrix.png)

# Web apps
To check on my web app, you can download file app.py and run using streamlit. Below is the screenshot of my web app:

![webapp](webapp.png)

# Credit

1) Data sets : [Here](https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset)
2) Webapps Image : [Here](https://images.news18.com/ibnlive/uploads/2022/01/heart-health-16430292883x2.jpg?impolicy=website&width=510&height=356)
