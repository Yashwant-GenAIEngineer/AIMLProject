#Problem Statement
#Problem: Create a recipe from list of ingredients.

#Steps:

#     Import the necessary packages (openai, json).

#     Store your private API key in a JSON file and load it in ‘openai.api_key’.

#     Inside the prompt type we have to provide the list of ingredients list on which recipe will be generated.
#Here, for instance, we have taken the example of the Caramel Custard.

#     To view the result of your prompt, you need to drill down to the “text” key.

import openai
import json

#Import and load the secret key

response = openai.Completion.create(
  engine="davinci-instruct-beta",
  prompt="Write a recipe based on these ingredients and instructions:\n\nCaramel Custard\n\nIngredients:\nMilk\nCustard Powder\n\nSugar\nMilkmaid\n\n Steps to be followed:",
  temperature=0,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.5
)

#print(response)
print(response['choices'][0]["text"])