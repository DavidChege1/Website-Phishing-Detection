# Website Phishing Detection
![Module-4-image-1024x768-1](https://github.com/user-attachments/assets/895111b5-fb3c-4638-97b9-7df1089321d7)
## Team members
 - David Chege
 - Gladwell Chepkorir
 - Royce Bett
 - Winny Chepkoech

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
-	Target Variable: label (0 = legitimate, 1 = malicious)

### Data Preparation
- Checking for duplicates
- Data cleaning
- Checking for missing values

### Exploratory Data Analysis
 - Class Distribution
![download](https://github.com/user-attachments/assets/3fe5fba8-387f-4a6d-8e63-8f090a9dc4db)

 - Feature Correlation
![download](https://github.com/user-attachments/assets/c2af8627-484d-41cd-bd36-9ceeef768c83)

 - Feature Distribution
![download](https://github.com/user-attachments/assets/0ee009f8-8468-4e52-84c8-2a8615b6c8dc)

![download](https://github.com/user-attachments/assets/47a2c863-a5a4-4e8b-94c9-44ae1087cf08)

 - Feature Engineering
![download](https://github.com/user-attachments/assets/5ec9a7db-2b80-4a8f-a417-72465b062cca)

![download](https://github.com/user-attachments/assets/1660bca1-e430-4218-8170-d93394ff5494)

![download](https://github.com/user-attachments/assets/84529ec6-1252-41a0-ad7f-d1f83da75b6f)
