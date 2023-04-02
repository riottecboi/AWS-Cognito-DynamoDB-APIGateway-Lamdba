
# AWS serverless (Cognito-Lambda-DynamoDB-APIGateway-Lambda)

This project provides the way how to set up an AWS serverless to register new user from Cognito then storing email, username ... to DynamoDB by triggering Lambda function which also generating random encoded basic authentication and being used on the APIGateway side, to authorized user by custom Authorizer (Lambda function).





## Sample architecture

![](https://github.com/riottecboi/AWS-Cognito-DynamoDB-APIGateway-Lamdba/blob/main/diagram.png)


## What we needs

- Cognito's user pool

- Lambda function `cognitoLambda.py` as triggered function for Post Confirmation on Sign in Configuration

- DynamoDB with table name, `user` in my case, with `authentication` as primary key

- API Gateway with custom authentication (Lambda function `authorizerLambda,py`)

- IAM for 2 Lambda functions (**CloudWatchFullAccess**, **AmazonDynamoDBFullAccess**, **AWSLambdaExecute**) - not recommend for FULL ACCESS policies

- Source server, where API Gateway can reach to. In this particularly case, I have a sample FastAPI server which randomly generating fake user records

 

## Achievements

- Can store register's record to DynamoDB by Lambda from Cognito

- Can build a proxy integration API (REST API or HTTP API) with Lambda Authorizer

- Lambda Authorizer can forward traffic to the source server while user authenticated and preventing access while user cannot pass an authorization.

- Reduce the time response by increasing more memory for lambda to execute a code

## Sample Cognito response

````````````````````````````````````
 {
     'version': '1', 'region': 'us-east-1', 'userPoolId': 'us-east-1_sJ9EEEEEE',
     'userName': '1d3e62b0-1dc6-4fed-9872-b67bfaaaaaa',
     'callerContext': {'awsSdkVersion': 'aws-sdk-unknown-unknown', 'clientId': '7bead3niq15471jo3eeeeeee'},
     'triggerSource': 'PostConfirmation_ConfirmSignUp',
     'request': {'userAttributes': {'sub': '1d3e62b0-1dc6-4fed-9872-b67bf9gggggg', 'email_verified': 'true',
     'cognito:user_status': 'CONFIRMED', 'cognito:email_alias': 'abc@gmail.com', 'email': 'abc@gmail.com'}},'response': {}
 }

`````````````````````````````````````




