# Public_Cloud_Resume_Challenge_on_AWS_by_jclm1rt
Public repository of my resume website, here you can find the code for lambda functions and templates for IaC and website. Take it as an example to make your website. 

Here's what I did:
- Bought a domain on freenom.com
- Built the project in AWS.
- Created CICD for it.

Stack I used:
- Route 53 for name resolution.
- Certificate Manager for SSL.
- Cloudfront for faster loading.
- S3 for static hosting and to store logs.
- Cloudformation for deploy resources.
- API gateway to create apis.
- Lambda for Get, Put requests, send notification & events in dynamodb.
- DynamoDB for storing count.
- DynamoDB streams to generate response to an event in the database.
- SNS for send notification when my websited is visited.
- Slack for send notification when my websited is visited.
- Formspree to contact me through the website.
- Secret Manager to store credentials.

What I did to maintain the project:
- Automated workflow using GithubActions.
- AWS SAM for creation and deployment of serverless website.

I will improving constanly my resume website, stay tunned.

![Cloud Resume Challengue jclm1rt v2 0_diagrama](https://user-images.githubusercontent.com/55666859/184401605-61accfa4-7d5d-4f50-8efe-f8b6bbce68b9.jpg)
