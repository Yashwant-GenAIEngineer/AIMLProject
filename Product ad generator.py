#Problem Statement
#Turn a product description into ad copy

#Steps:

#Import the necessary packages (openai, json). 

#Store your private API key in a JSON file and load it in ‘openai.api_key’. 

#Inside the prompt, type in the description of the product you want to generate an advertisement for 
#Here, for instance, we have taken the example of an offroad motorbike XR350. We will let the system design an advertisement for this bike. 

#To view the result of your prompt, you need to drill down to the “text” key.

!pip install openai

#importing libraries
import openai
import json

#loading the secret key json
with open(r'secret_key.json') as f:
    key = json.load(f)
    
#setting the key from the value of secret key json
openai.api_key = key["secret_key"]

#setting engine, prompt and other parameters
response = openai.Completion.create(
  engine="davinci-instruct-beta",
  prompt="Write a creative ad for the following product to run on Instagram:\n\"\"\"\"\"\"\nXR350 motorcycle for offroad and mountain riders. High performance 349cc engine. Available in 3 color segments. Customization available.\n\"\"\"\"\"\"\nThis is the ad I wrote for Instagram aimed at motorbiking lovers:\n\"\"\"\"\"\"",
  temperature=0.8,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\"\"\"\"\"\""]
)

#Printing the result
print(response['choices'][0]["text"])




