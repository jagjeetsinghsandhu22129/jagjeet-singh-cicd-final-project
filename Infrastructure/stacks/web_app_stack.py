from aws_cdk import (
    aws_s3 as s3,
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
    CfnOutput,
    Stack
)
from constructs import Construct

import uuid 

class WebAppStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # S3 Bucket for frontend
        bucket = s3.Bucket(self, "FrontendBucket", versioned=True)

        # Lambda backend
        backend = lambda_.Function(self, "BackendFunction",
                                   runtime=lambda_.Runtime.PYTHON_3_9,
                                   handler="app.handler",
                                   code=lambda_.Code.from_asset("../backend"))

        # API Gateway with unique ID
        api = apigateway.LambdaRestApi(self, f"APIEndpoint-{uuid.uuid4()}", 
                                       handler=backend)

        # Outputs
        CfnOutput(self, "BucketName", value=bucket.bucket_name)
        CfnOutput(self, "APIEndpoint", value=api.url)
