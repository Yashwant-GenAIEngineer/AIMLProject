#Problem: Generating SQL commands from English text

#Steps:

#      Load the key stored in json file

#      Create an instance of gpt model

#      Add few examples to make gpt-3 understand what we are trying to accomplish.

#      Test whether gpt-3 can generate SQL commands for a given English text.

import openai
import json
with open('GPT-3-SECRET-KEY.json') as f:
    key = json.load(f)
openai.api_key = key["OPEN_API_KEY"]
from gpt import GPT
from gpt import Example
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

#Adding Examples for GPT-3 model
#Example1
gpt.add_example(Example('Find unique values of DEPARTMENT from Employee table.', 
                        'Select distinct DEPARTMENT from Employee;'))

#Example2
gpt.add_example(Example("Find the count of employees in department ECE.", 
                        "SELECT COUNT(*) FROM Employee WHERE DEPARTMENT = 'ECE';"))