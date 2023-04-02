import boto3

# Initialize Dynnamo resources
dynamodb = boto3.resource('dynamodb')
# Replace a table name you want to store from Cognito User's pool
table = dynamodb.Table('user')

def lambda_handler(event, context):

    try:
        # Get authorization header in lowercase
        authorization_header = {k.lower(): v for k, v in event['headers'].items() if k.lower() == 'authorization'}

        # Get the username:password encoded from the authorization header
        username_password = authorization_header['authorization'].split()[1]

        # Get the password from DynamoDB for the username
        item = table.get_item(ConsistentRead=True, Key={"authentication": username_password})
        if item.get('Item') is not None:
            return {
                "principalId": event['requestContext']['accountId'],
                "policyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Action": "execute-api:Invoke",
                            "Resource": event['methodArn']
                        }
                    ]
                }
            }
        else:
            raise Exception('Unauthorized')

    except Exception as e:
        raise Exception('Unauthorized')