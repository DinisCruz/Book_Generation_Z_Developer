---
title : Python
status: content
weight: 20
what  : Programming language that all developers should master
task  : Create and publish an Python tool
price : free
---

[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is great language to master since it contains a large number of the key development paradigms that you need to know, while being easy to learn and read. 

Python started in 1991 by [Guido van Rossum](https://twitter.com/gvanrossum/) when he was 35 and the key focus was in making a simple but powerful language. 

A great feature added early on was the REPL (Read Eval Print Loop) environment. This is what you see when you run `python` from the command line and get an interactive shell that allows the execution of Python code. That said, I don't use the Python command line very often, since I have a similar (and more powerful) REPL environment using Python tests (and TDD)

### Use Python for AWS automation

Even if you are not using Python as your main development language, due to it massive adoption and powerful ability to write small apps/function, you should use it often (for all sorts of automation tasks).

A perfect example of the power of Python is in the development of Serverless functions (executed as an [AWS Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model-handler-types.html)) or in advanced customizations of event-driven workflows (like the one provided by [Zapier Python support](https://zapier.com/help/code-python/))

The [AWS SDK for python (boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) is something you should spend quite a lot of time with and really explore its capabilities (while learning to take python into another level). 

This API gives you access to just about everything you can do in AWS, and as a developer you need to really start thinking of AWS as an 'app' that you code your application on top of its capabilities. You need to get into the practice of writing code (driven by tests) vs clicking on things.

For example here is a code snippet that starts a virtual machine in AWS:

```
import boto3
ec2         = boto3.client('ec2')
instance_id = sys.argv[2]
response    = ec2.start_instances(InstanceIds=[instance_id])
print(response)
```

### Don't click on things

Clicking on an UI with your mouse, is a non-repeatable, non-automated and non-scalable way to perform a specific task. What you want to do is to write tools, APIs and DSLs that allow the easy and automated execution of those tasks.

For example here is a python script that tests the execution of an Lambda function

```
    def test_hello_world(self):
        handler         = 'lambdas.s3.hello_world.run'
        payload         = {"name": "lambda-runner"}
        expected_result = 'hello {0}'.format(payload.get('name'))

        self.aws.lambda_create_function(self.name, self.role, handler, self.s3_bucket, self.s3_key)
        result = self.aws.lambda_invoke_function(self.name, payload)
        assert result == expected_result
```

### Python for data parsing and analysis

Another really powerful use of Python is to perform all sorts of data parsing, modeling and analysis.

As a very practical real world scenario, if somebody sends me multiple excel documents with data to analyse, the first thing I do is to:

- export it to csv, 
- use python to normalize the raw data into json file(s)
- use an data visualizing tool or API (for example ELK, Neo4J or [visjs](http://visjs.org/)). 

This is not very hard to do, and is faster then trying to make sense of the excel documents (namely when needing to do data correlation between different excel sheets or files)