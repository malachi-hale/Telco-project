# Classification Project
# Why do customers churn?


## Objectives 

### Project Goals
 - To document **code**, our **process** (*data acquisition*, *data preparation*, *exploratory data analysis*, and *statistical testing*, *modeling*, and *model evaluation*), **findings**, and **key takeaways** in a Jupyter Notebook report. 
 
 - To create modules (such as `acquire.py`, `prepare.py`) which contain functions that make our process repeatable. 
 
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
### Target Variable

| Target   | Dataype   | Definition                            |
|:---------|:----------|:--------------------------------------|
| churn    | object    | Whether or not a customer has churned |

### Features of our data, before cleaning
| Feature                  | Dataype   | Definition                                                                                                     |
|:-------------------------|:----------|:---------------------------------------------------------------------------------------------------------------|
| customer_id              | object    | Identification number for customer                                                                             |
| gender                   | object    | Customer gender, male or female                                                                                |
| senior_citizen           | int64     | Yes or no, is the customer a senior citizen                                                                    |
| partner                  | object    | Yes or no, does the customer customer has a parter                                                             |
| dependents               | object    | Number of dependents a customer has                                                                            |
| tenure                   | int64     | Number of months a customer has been with the company                                                            |
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


### Features of our data after cleaning 
| Feature                               | Dataype   | Definition                                                                                                     |
|:--------------------------------------|:----------|:---------------------------------------------------------------------------------------------------------------|
| customer_id                           | object    | Identification number for customer                                                                             |
| senior_citizen                        | int64     | 0 for not senior citizen, 1 for senior citizen                                                                 |
| tenure                                | int64     | Months the customer has been with the company                                                                  |
| internet_service_type_id              | int64     | 1 for DSL, 2 for Fiber Optic, 3 for None                                                                       |
| contract_type_id                      | int64     | 1 for month-to-month, 2 for year, and 3 for two-year contract                                                  |
| payment_type_id                       | int64     | 1 for electronic check, 2 for mailed check, 3 for automatic bank transfer, 4 for automatic credit card payment |
| monthly_charges                       | float64   | Charges a customer pays per months                                                                             |
| total_charges                         | float64   | Total charges a customer has paid                                                                              |
| has_churned                           | int64     | 0 for has not churned, 1 for has churned                                                                       |
| paperless_billing_numeric             | int64     | 0 for non-paperless billing, 1 for paperless billing                                                           |
| partner_Yes                           | uint8     | 0 for no partner, 1 for has partner                                                                            |
| dependents_Yes                        | uint8     | 0 for no dependents, 1 for has dependents                                                                      |
| gender_Male                           | uint8     | 0 for female, 1 for male                                                                                       |
| phone_service_Yes                     | uint8     | 0 for no phone service, 1 for phone service                                                                    |
| multiple_lines_No phone service       | uint8     | 0 for phone service, 1 for no phone service                                                                    |
| online_security_No internet service   | uint8     | 0 for internet service, 1 for no internet service                                                              |
| online_security_Yes                   | uint8     | 0 for no online security, 1 for online security                                                                |
| online_backup_No internet service     | uint8     | 0 for internet service, 1 for no internet service                                                              |
| online_backup_Yes                     | uint8     | 0 for no online backup, 1 for online backup                                                                    |
| device_protection_No internet service | uint8     | 0 for internet service, 1 for no internet service                                                              |
| device_protection_Yes                 | uint8     | 0 for no device protection, 1 for device protection                                                            |
| tech_support_No internet service      | uint8     | 0 for internet service, 1 for no internet service                                                              |
| tech_support_Yes                      | uint8     | 0 for no tech support, 1 for tech support                                                                      |
| streaming_tv_No internet service      | uint8     | 0 for internet service, 1 for no internet service                                                              |
| streaming_tv_Yes                      | uint8     | 0 for no streaming TV, 1 for streaming TV                                                                      |
| streaming_movies_No internet service  | uint8     | 0 for internet service, 1 for no internet service                                                              |
| streaming_movies_Yes                  | uint8     | 0 for no streaming movies, 1 for streaming movies                                                              |

## Initial Hypotheses 

### Hypothesis 1
 - **alpha** = 0.05
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no significant difference in the churn rate for customers on month-to-month contracts and the churn rate for customers on either year or two-year contracts. 
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant significant difference in the churn rate for customers on month-to-month contracts and the churn rate for customers on either year or two-year contracts. 
 
 - **Outcome**: I rejected the Null Hypothesis. There is a significant difference in churn rate for customers on a month-to-month contract and customers on either year or two-year contracts.
 
### Hypothesis 2 
 - **alpha** = 0.05
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no significant correlation between customer churn rate and contract type. 
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant correlation between customer churn rate and contract type.
 
 - **Outcome**: I rejected the Null Hypothesis. There is a significant correlation between customer churn rate and contract type.
 
### Hypothesis 3 
 - **alpha** = 0.05
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no significant correlation between customer churn rate and payment type ID. 
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant correlation between customer churn rate and payment type ID.
 
 - **Outcome**: I rejected the Null Hypothesis. There is a significant correlation between customer churn rate and payment type ID.

### Hypothesis 4
 - **alpha** = 0.05
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no significant correlation between customer churn rate and monthly charges. 
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant correlation between customer churn rate and monthly charges.
 
 - **Outcome**: I rejected the Null Hypothesis. There is a significant correlation between customer churn rate and monthly charges.

### Hypothesis 5
 - **alpha** = 0.05
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no significant correlation between customer churn rate and internet service type ID. 
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant correlation between customer churn rate and internet service type ID.
 
 - **Outcome**: I rejected the Null Hypothesis. There is a significant correlation between customer churn rate and internet service type ID.

### Hypothesis 6
 - **alpha** = 0.05
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no significant difference between the mean tenure for customers who churn and customers who don't churn. 
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant difference between the mean tenure for customers who churn and customers who don't churn. 
 
 - **Outcome**: I rejected the Null Hypothesis. There is a significant difference between the mean tenure for customers who churn and customers who don't churn.

### Hypothesis 7
 - **alpha** = 0.05
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no significant difference between the mean monthly charges for customers who churn and customers who don't churn. 
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant difference between the mean mean monthly charges for customers who churn and customers who don't churn. 
 
 - **Outcome**: I rejected the Null Hypothesis. There is a significant difference between the mean monthly charges for customers who churn and customers who don't churn.
 
### Hypothesis 8 
 - **alpha** = 0.05
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no significant difference between the mean total charges for customers who churn and customers who don't churn. 
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant difference between the mean mean total charges for customers who churn and customers who don't churn. 
 
 - **Outcome**: I rejected the Null Hypothesis. There is a significant difference between the mean total charges for customers who churn and customers who don't churn.

## Executive Summary - Conclusions & Next Steps 
 - With the goal of determining the biggest drivers of churn. I used three classification models: **Decision Tree**, **RandomForest**, and **K Nearest Neighbors**. I varied the parameters on each of these models several times. All of the models we produced have a higher accuracy than the baseline of 0.73.

 - I found that the `RandomForest` with `max_depth=10` and `min_samples_leaf=1` performed with a high level of recall, while still maintaining high accuracy and precision. I concluded that recall score was most important to us because we want to capture all customers who churn. Overestimating churn rate is better than underestimating churn rate. 
     - Additionally, this model outperformed our baseline accuracy of 0.73, so it has value. 
 
 - We utilize the `feature_importances` function on our selected `RadomForest` model to obtain the features in the data with the most relative importances.
 
    |                  |   relative importance |
    |:-----------------|----------------------:|
    | total_charges    |             0.169107  |
    | tenure           |             0.165327  |
    | monthly_charges  |             0.130737  |
    | contract_type_id |             0.1261    |
    | payment_type_id  |             0.0777759 |
    
 - Our `DecisionTree` model with `max_depth=3` helps us to determine how to associate these values, 
    

### Key findings
 - We find that `total_charges` is the biggest predictor of churn. 
     - However, because `total_charges = monthly_charges * tenure`, the `total_charges` feature is essentially a combination of `monthly_charges` and `tenure`. 
 - Our `DecisionTree` model with `max_depth=3` indicates to us that the customers on a month-to-month contract are more likely to churn than customers on a year or two-year contract. 
     - Among customers on a month-to-month contract additional predictors of cuhrn are having `tenure` of 5 months or less and monthly charges less than $68.43. 
     
### Recommendations
 - Based on this data, I recommend that the month-to-month contract be limited to either customers who meet either of the following criteria:
     - tenure with the company of at least 5 months. 
     - Monthly charges greater than or equal to $68.43. 
 - I also recommend that we explore the data further, particularly looking at our most important features (`total_charges`, `tenure`, `monthly_charges`, `contract_type_id`, and `payment_type_id`) and their association with churn. 
     - We may be able to adjust the contract requirements based on these criteria to reduce the probability of customer churn. 
     
## Pipeline Stages Breakdown

### Project planning
#### *Plan*
 - Create a README.md file with a data dictionary, project and business goals, state our initial hypotheses. 

 - Create an `acquire.py` model to acquire data from the Codeup Database. 
 
 - Create a `prepare.py` model to prepare data for the Final Report notebook. 
 
 - Define initial hypotheses, reject or fail to reject the Null Hypotheses. Document key findings. 
 
 - Establish baseline accuracy. 
 
 - Train classification models. 
 
 - Evaluate the models on our train and validate datasets. 
 
 - Choose the best model to try on the test data.
 
 - Create a CSV file with customer_id, probability of churn, and prediction of churn. 
 
 - Document conclusions, takeaways, and next steps in the Final Report Notebook. 
 
### Data Acquisition
#### Plan -> *Acquire*
**In the `acquire.py` module:**
 - Store function that are needed to acquire data from the `customers` table. We will join the `contract_types`, `internet_service_types`, and `payment_types` tables. 
 
 - The final function should be in a pandas DataFrame. 
 
**In the Notebook:**
 - Import the acquire function from `acquire.py` and use it to acquire the relevant data. 
 
 - Complete initial data summarization (`info()`, `describe()`, `value_counts()`, ...)
 
 - Plot distributions of individual variables. 
 
### Data Preparation 
#### Plan -> Acquire -> *Prepare*
**In the `prepare.py` module:**
 - Store functions needed to prepare the customer churn data. The final function will: 
     - Split the data into train/validate/test.
     - Handle missing values. 
     - Encode variables as needed.
     - Create new features as needed. 

**In the Notebook:**
 - Explore missing values and document takeaways/actions for handling them. 
 - Import the prepare function from `prepare.py` and use this function to prepare the data in the notebook.
 
 
### Data Exploration & Analysis
#### Plan -> Acquire -> Prepare -> *Explore*
**In the Notebook:**
 - Answer the key questions posed by my hypotheses and figure out the features that can be used in a classification model to predict the target variable, churn. 
 
 - Run at least two statistics tests in data exploration. Document the hypotheses, set an alpha, and document the findings well. 
 
 - Create visualizations and statistical tests to determine variable relationships. 
 
 - Summarize conclusions and provide clear takeaways. 
 
### Modeling and Evaluation 
#### Plan -> Acquire -> Prepare -> Explore -> *Model and Evaluate*
**In the Notebook:**
 - Establish a baseline accuracy. Compare this baseline accuracy to at least three different models. 
 
 - Train multiple models, varying the algorithm and hyperparameters 
 
 - Compare evaluation metrics across models
     - Select the models we want to use to evaluate the validate dataframe.
     
 - Feature selection: find which variables provide the most and the least information. 
 
 - Chose the best model to use to evaluate the test data. 
 
 - Test the final model on the testing data, summarize the performance, interpret and document the results. 
 
### Delivering 
#### Plan -> Acquire -> Prepare -> Explore -> Model and Evaluate -> *Deliver*
 - Introduce self and goals at the beginning of the project. 
 
 - Summarize findings at the beginning of the project.
 
 - Walk through the analysis. Clearly state questions and answers. 
 
 - Offer insights and recommendations. 
 
 - Finish with key takeaways, recommendations, and next steps. 
 
 ## Reproduce my project 
 To reproduce my project, you will need you own `env.py` file with database credentials, in addition to the files listed below:
 - Read this `README.md` file.
 - Download `acquire.py`, `prepare.py`, and `final_report.ipynb`.
 - Add your own `env.py` file to your directory. 
 - Run the `final_report.ipynb` notebook. 