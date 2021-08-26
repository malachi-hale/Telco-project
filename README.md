# Classification Project
# Why do customers churn?


## Objectives 

### Project Goals
 - To document **code**, our **process** (_data acquisition_, _data preparation_, _exploratory data analysis and statistical testing_, _modeling_, and _model evaluation_), **findings**, and **key takeaways** in a Jupyter Notebook report. 
 
 - To create modules (such as acquire.py, prepare.py) that make our process repeatable. 
 
 - To construct a model to predict customer churn using classification techniques. 
 
 - To deliver a five-minute presentation of high-level notebook walkthrough of a Jupyter Notebook. 
 
 - To answer panel questions about the code, the process, the findings, the key takeaways, and the model. 

### Business Goals 
 - To find drivers for churn at Telco.
     - To answer the question: **Why are customers churning?**
 - To construct a machine learning classification model that accurately predicts customer churn. 
 - To document the process to be presented like a report. 
 
### Audience 
 - The Codeup Data Science team. 
  
## Data Dictionary
**Target Variable**

| Target   | Dataype   | Definition                            |
|:---------|:----------|:--------------------------------------|
| churn    | object    | Whether or not a customer has churned |

**Features of our data, before cleaning**
| Feature                  | Dataype   | Definition                                                                                                     |
|:-------------------------|:----------|:---------------------------------------------------------------------------------------------------------------|
| customer_id              | object    | Identification number for customer                                                                             |
| gender                   | object    | Customer gender, male or female                                                                                |
| senior_citizen           | int64     | Yes or no, is the customer a senior citizen                                                                    |
| partner                  | object    | Yes or no, does the customer customer has a parter                                                             |
| dependents               | object    | Number of dependents a customer has                                                                            |
| tenure                   | int64     | Number of days a customer has been with the company                                                            |
| phone_service            | object    | Type of phone service plan a customer has                                                                      |
| multiple_lines           | object    | Yes or no, does the customer have multiple lines                                                               |
| internet_service_type_id | int64     | 1 for DSL, 2 for Fiber Optic, 3 for None                                                                       |
| online_security          | object    | Yes, no, or no internet service                                                                                |
| online_backup            | object    | Yes, no, or no internet service                                                                                |
| device_protection        | object    | Yes, no, or no internet service                                                                                |
| tech_support             | object    | Yes, no, or no internet service                                                                                |
| streaming_tv             | object    | Yes, no, or no internet service                                                                                |
| streaming_movies         | object    | Yes, no, or no internet service                                                                                |
| contract_type_id         | int64     | 1 for month-to-month, 2 for year, and 3 for two-year contract                                                  |
| paperless_billing        | object    | Yes or no, whether or not the customer uses paperless billing                                                  |
| payment_type_id          | int64     | 1 for electronic check, 2 for mailed check, 3 for automatic bank transfer, 4 for automatic credit card payment |
| monthly_charges          | float64   | Monthly charges the customer pays                                                                              |
| total_charges            | object    | Total charges the customer has paid                                                                            |
| churn                    | object    | Yes or no, whether or not the customer has churned                                                             |
| contract_type            | object    | Month-to-month, year, or two-year contract                                                                     |
| internet_service_type    | object    | DSL, Fiber Optic, or None                                                                                      |
| payment_type             | object    | Electronic check, mailed check, automatic bank transfer, or automatic credit card payment                      |
| has_churned              | int64     | 0 for has not churned, 1 for has churned                                                                       |


## Initial Hypotheses 

### Hypothesis 1
 - **alpha** = 0.05
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no difference in the churn rate for customers on month-to-month contracts and the churn rate for customers on either year or two-year contracts. 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant difference in the churn rate for customers on month-to-month contracts and the churn rate for customers on either year or two-yera contracts. 
 - **Outcome**: I rejected the Null Hypothesis. There is a significant difference in the churn rate for customers on month-to-month contracts and customers on either year or two-year contracts. 
 
### Hypothesis 2 
 - **alpha** = 0.05
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no correlation between customer churn rate and monthly charges. 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a correlation between customer churn rate and monthly charges.
 - **Outcome**: I rejected the Null Hypothesis. The churn rate and monthly charges are correlated.
 
## Executive Summary - Conclusions & Next Steps 
 - With the goal of determining the biggest drivers of churn. I used two classification models: **Random forest** and **Decision Tree**.
 - Utilitizing **feature_importances** of **Random forest** I was able to determine the relative importance of each variable for predicting churn. The data indicated in the table below shows us that **tenure**, **monthly charges**, **contract type**, and **payment type** are the biggest drivers of churn.
     
    |                                       |   relative importance |
    |:--------------------------------------|----------------------:|
    | tenure                                |            0.24197    |
    | monthly_charges                       |            0.156533   |
    | contract_type_id                      |            0.148934   |
    | payment_type_id                       |            0.0805465  |
    | internet_service_type_id              |            0.0434827  |
    | tech_support_Yes                      |            0.0404554  |
    | online_security_Yes                   |            0.0367749  |
    | gender_Male                           |            0.0235222  |
    | online_backup_Yes                     |            0.0222814  |
    | senior_citizen                        |            0.0203455  |
    | partner_Yes                           |            0.019818   |
    | multiple_lines_Yes                    |            0.0197366  |
    | dependents_Yes                        |            0.018233   |
    | device_protection_Yes                 |            0.0172931  |
    | streaming_movies_Yes                  |            0.0162566  |
    | streaming_tv_Yes                      |            0.0161795  |
    | online_backup_No internet service     |            0.0144566  |
    | tech_support_No internet service      |            0.0116313  |
    | online_security_No internet service   |            0.0116167  |
    | streaming_tv_No internet service      |            0.0101157  |
    | device_protection_No internet service |            0.0087282  |
    | streaming_movies_No internet service  |            0.00830758 |
    | multiple_lines_No phone service       |            0.00655208 |
    | phone_service_Yes                     |            0.00622841 |

