#Problem Statement
#Steps:

#     Import the necessary packages (openai, json).

#     Store your private API key in a JSON file and load it in ‘openai.api_key’.

#     Inside the prompt type in an essay topic on which you want your outline to be generated.

#     To view the result of your prompt, you need to drill down to the “text” key.

import openai
import json
with open('secret_key.json') as f:
    key = json.load(f)
openai.api_key = key["secret_key"]

response = openai.Completion.create(
  engine="davinci-instruct-beta",
  prompt="Create a list of questions for my interview with a data scientist:\n\n1.",
  temperature=0.8,
  max_tokens=200,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n\n"]
)

print(response['choices'][0]["text"])