.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec iamadmin --no-session -- sam deploy

deploy-site:
	aws-vault exec iamadmin --no-session -- aws s3 sync ./resume-site s3://my-amazing-website-jclm1rt
