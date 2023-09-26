<div align="center">

## Fortune Teller

</div>

### Introduction
This project is a simple serverless application that returns random responses (Yes,No,Maybe) to Yes/No questions.
It provides a comprehensive example of **building**, **testing**, and **deploying** an application using **Aws Lambda** and **API Gateway**.

### Features

* Serverless function using Aws Lambda
* API built with API Gateway Service to trigger the lambda function

### Prerequisites

- An Aws Account
- An Internet Connection

### Getting Started

#### Create and configure aws lambda function

- **Step 1 :**  Open Aws Lambda Management Console

![](./screenshots/lambda/lambda_step1.png)


- **Step 2 :**  Choose Name and Runtime Environment 

![](./screenshots/lambda/lambda_step2.png)


- **Step 3 :**  Optional : Rename "lambda_function" file to fortune_teller 

![](./screenshots/lambda/lambda_step3.png)

- **Step 4 :**  Copy and Paste the Function Code into the Code Box and Click Deploy

![](./screenshots/lambda/lambda_step4.png)

- **Step 5 :**  Change the Runtime settings

![](./screenshots/lambda/lambda_step5.png)

- **Step 6 :**  Test the lambda function

![](./screenshots/lambda/lambda_step6.png)

#### Create and Configure Aws APi Gateway

- **Step 1 :**  Open Aws API Gateway Management Console

![](./screenshots/api_gateway/api_step1.png)

- **Step 2 :**  Choose a Name and Integrate with the Lambda Function

![](./screenshots/api_gateway/api_step2.png)

- **Step 3 :**  Configure API Route

![](./screenshots/api_gateway/api_step3.png)


- **Step 4 :**  Review and Create

![](./screenshots/api_gateway/api_step5.png)