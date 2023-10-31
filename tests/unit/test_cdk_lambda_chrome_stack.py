import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_lambda_chrome.cdk_lambda_chrome_stack import CdkLambdaChromeStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_lambda_chrome/cdk_lambda_chrome_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkLambdaChromeStack(app, "cdk-lambda-chrome")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
