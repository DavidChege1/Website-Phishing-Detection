# Website Phishing Detection
![Module-4-image-1024x768-1](https://github.com/user-attachments/assets/895111b5-fb3c-4638-97b9-7df1089321d7)


## Team members
 - David Chege
 - Gladwell Chepkorir
 - Royce Bett
 - Winny Chepkoech

 ## Project Summary

This project focuses on developing a machine learning model to classify websites as phishing or legitimate, aiming to enhance online security by detecting phishing attempts. After gathering and cleaning the data, we conducted Exploratory Data Analysis (EDA) to identify patterns in website features, such as URL length, presence of suspicious characters, and HTTPS usage. These insights informed our feature selection and helped highlight characteristics often associated with phishing sites. 

Six models were trained: Logistic Regression, Decision Tree, Random Forest, LightGBM, XGBoost, and a Deep Neural Network (DNN), with model performance evaluated on accuracy, precision, recall, and F1-score.The models experienced overfitting and we used overfitting reduction techniques to reduce it. All six models performed well with high accuracy of above 90%, but Logistic Regression was chosen for deployment due to its interpretability and efficiency.

To make phishing detection accessible, we deployed a real-time prediction tool using Streamlit. The application allows users to input website features and uses the Logistic Regression model to predict if the site is phishing or legitimate. Future work could improve detection accuracy by integrating more advanced models or real-time data on threats, offering a comprehensive solution for phishing prevention.


## Contents
 - Business Overview
 - Business Understanding
 - Data Understanding
 - Data Preparation
 - Exploratory Data Analysis
 - Modeling and Evaluation


### Business Overview
#### Introduction
Phishing is a type of cyberattack where one impersonates trusted people or parties in an attempt to gain sensitive information such as usernames, passwords, bank details etc.
Things are becoming increasingly hosted online, which widens the pool of targets, while simultaneously empowering perpetrators further; with schemes going from simple ones targeted at individuals to more elaborate ones that go as far as targeting multi-national corporations.

#### Problem Statement
Phishing attacks pose a significant cybersecurity threat by luring users to malicious websites disguised as legitimate ones. Identifying phishing URLs can prevent users from falling victim to these attacks, which often lead to data theft and financial loss.

#### Objectives
To develop a machine learning model to classify URLs as either legitimate or malicious based on structural, content, and behavioral characteristics. The model aims to achieve high accuracy, precision, and recall in identifying potentially harmful URLs.

### Data Understanding
-	Source: Dataset contains URL-related features with labels indicating legitimacy or malicious intent.
- Key Features:
-	URL Structure: URLLength, Domain, NoOfSubDomain, TLD, CharContinuationRate
-	Content: Title, TitleMatchScore, HasFavicon, HasSocialNet
-	Behavior: Redirects (NoOfURLRedirect, NoOfSelfRedirect), popups (NoOfPopup), HasExternalFormSubmit
-	HTML Elements: NoOfCSS, NoOfJS, NoOfImage
-	Target Variable: label (1 = legitimate, 0 = malicious)

### Data Preparation
- Checking for duplicates
- Data cleaning
- Checking for missing values

### Exploratory Data Analysis
- Class Distribution

![download](https://github.com/user-attachments/assets/bb248592-ef91-4703-b2ca-4d2061642394)

- Feature Correlation

![download](https://github.com/user-attachments/assets/c2af8627-484d-41cd-bd36-9ceeef768c83)

- Feature Distribution

![download](https://github.com/user-attachments/assets/0ee009f8-8468-4e52-84c8-2a8615b6c8dc)
   
![download](https://github.com/user-attachments/assets/47a2c863-a5a4-4e8b-94c9-44ae1087cf08)

The dataset's features reveal notable outliers, particularly in fields like `NoOfSubDomain` (23,903 outliers), `NoOfDegitsInURL` and `DegitRatioInURL` (both with 20,863), and `IsHTTPS` (22,580), indicating abnormal URL structures. Financial keywords (`Bank`: 12,670, `Pay`: 23,857, `Crypto`: 2,421) also show significant outliers. Indicators of obfuscation (`HasObfuscation`: 192) and suspicious web behavior (`NoOfPopup`: 5,698, `NoOfiFrame`: 14,887) highlight irregular design and content patterns. 

- Feature Engineering

![download](https://github.com/user-attachments/assets/5ec9a7db-2b80-4a8f-a417-72465b062cca)

![download](https://github.com/user-attachments/assets/1660bca1-e430-4218-8170-d93394ff5494)

![download](https://github.com/user-attachments/assets/84529ec6-1252-41a0-ad7f-d1f83da75b6f)

The feature statistics and outlier removal results provide insights into the dataset's characteristics and cleanup process. Binary feature statistics reveal that most websites lack obfuscation, external form submission, self-redirection, and password fields, while many use HTTPS and have title tags, indicating typical attributes in legitimate websites. However, some features, like the presence of copyright information and social network links, are relatively balanced. 

Outlier removal focused on extreme values in various numerical columns, removing a significant 70.79% of rows, bringing the dataset to 29,210 rows. Key features affected include "NoOfSubDomain," "NoOfDegitsInURL," and "LineOfCode," suggesting these metrics had substantial variance and extreme values, likely from uncommon or malicious URLs. After outlier removal, the dataset should better reflect a standard distribution, enabling more reliable analysis. Visualizing pre- and post-cleaning distributions will highlight these adjustments and ensure data quality for modeling.

### Modeling

Initially, we used simple models before going into deep learning models for classification.
The models we used were:
- Logistic Regression
- Decision Tree
- Random Forest
- XG Boost
- Light GBM

After these, we implemented and tuned a deep neural network(DNN) to reduce overfitting.

### Deployment

It will be made in Streamlit and deployed in a cloud environment.

### Evaluation

 - Each of the models performs very well with indications of overfitting.
 - The Deep Neural Network achieves precision, recall, and F1-scores around 0.97 almost similar to Logistic Regression.
 - Logistic Regression model is a more practical choice for deployment because it is very simple and easy to deploy.

### Recommendations

- Adding a website checker tool that extracts information from the website to increase accuracy.
- We recommend employing additional features to make it possible to observe clearer patterns in the data.
- As we already have a model, we would recommend deploying it in an enclosed environment to allow us to properly monitor and tune it further.
- As time passes, we would need to alter the model to improve its performance even after deployment.
  


