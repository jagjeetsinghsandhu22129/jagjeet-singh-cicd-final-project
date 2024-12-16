
# Web Application Project using AWS CDK

This project demonstrates deploying a full-stack web application using AWS CDK. The backend is hosted on AWS Lambda and exposed via API Gateway, while the frontend is hosted in an S3 bucket with static website hosting.

## Project Architecture
- **Frontend**: A static website hosted in an Amazon S3 bucket.
- **Backend**: A REST API implemented using AWS Lambda and exposed via API Gateway.
- **Infrastructure**: Managed using AWS Cloud Development Kit (CDK).

## Deployed Resources
1. **S3 Bucket**:
   - Hosts the frontend application files.
   - Configured with static website hosting.

2. **AWS Lambda**:
   - Backend logic is implemented as a Lambda function.

3. **API Gateway**:
   - Exposes the Lambda function as a REST API.

## How to Access the Application
### Frontend
- **URL**: `http://<bucket-name>.s3-website-<region>.amazonaws.com`
- Ensure the S3 bucket has static website hosting enabled.

### Backend
- **API URL**: `https://rewlayg5g7.execute-api.us-east-1.amazonaws.com/prod/`
- Use this endpoint to interact with the backend API.

## Local Development
### Backend
1. Install dependencies:
   ```bash
   pip install -r requirements.txt


npm install -g aws-cdk@^2

cdk --version

pip uninstall aws-cdk.core aws-cdk.aws-s3 aws-cdk.aws-lambda aws-cdk.aws-apigateway
pip install aws-cdk-lib constructs

cdk bootstrap aws://<account-id>/<region>
cdk bootstrap aws://211125394827/us-east-1


rm -rf __pycache__

cdk synth --app "python app.py"

cdk deploy --app "python app.py"



Use AWS CLI
You can also use the AWS CLI to list the resources:

List Lambda Functions:


aws lambda list-functions
List S3 Buckets:

aws s3 ls
List API Gateway APIs:

aws apigateway get-rest-apis

## Tools & Technologies
AWS CDK: Infrastructure as Code
AWS Lambda: Serverless backend
API Gateway: REST API
S3: Static website hosting
