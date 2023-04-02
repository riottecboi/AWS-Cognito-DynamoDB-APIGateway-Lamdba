import boto3
import random
import string
import base64
from datetime import datetime

# Initialize Dynnamo resources
dynamodb = boto3.resource('dynamodb')
# Replace a table name you want to store from Cognito User's pool
userTable = dynamodb.Table('user')


# Sample event from event

# {'version': '1', 'region': 'us-east-1', 'userPoolId': 'us-east-1_sJ9EEEEEE',
# 'userName': '1d3e62b0-1dc6-4fed-9872-b67bfaaaaaa',
# 'callerContext': {'awsSdkVersion': 'aws-sdk-unknown-unknown', 'clientId': '7bead3niq15471jo3eeeeeee'},
# 'triggerSource': 'PostConfirmation_ConfirmSignUp',
# 'request': {'userAttributes': {'sub': '1d3e62b0-1dc6-4fed-9872-b67bf9gggggg', 'email_verified': 'true',
# 'cognito:user_status': 'CONFIRMED', 'cognito:email_alias': 'abc@gmail.com', 'email': 'abc@gmail.com'}}, 'response': {}}

def encode_authentication(authentication):
    base64_bytes = base64.b64encode(bytes(authentication, encoding='utf-8'))
    base64_string = base64_bytes.decode('utf-8')
    return base64_string


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def lambda_handler(event, context):
    print(event)
    username = event['userName']
    useremail = event['request']['userAttributes']['email']
    basicAuth = f"{username}:{get_random_string(8)}"
    basicAuthEncode = encode_authentication(basicAuth)

    dateUpdated = datetime.now()
    user = {
        'authentication': basicAuthEncode,
        'username': username,
        'email': useremail,
        'active': True,
        'updated': dateUpdated.strftime('%Y-%m-%d')
    }

    userTable.put_item(Item=user)
    return event