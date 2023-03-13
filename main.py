"""
@author: boachiejude
summary: This is the main file for the casual_llm project.
"""

import openai
from printer import type_it

# Set up the OpenAI API client
with open("my_key.txt", 'r') as file:
    openai.api_key = file.read()

# Choose a GPT-2 model size
model_engine = "gpt-3.5-turbo"

# Generate text using GPT-2
prompt_text = input(" How may I help you? (Type 'stop' to exit.)\n$ ")
while True:
    if prompt_text.lower() == "stop":
        break
    response = openai.ChatCompletion.create(engine=model_engine,
                                        prompt=prompt_text,
                                        max_tokens=100,
                                        temperature=0.7,)
    generated_text = response.choices[0].text
    type_it(generated_text)
    prompt_text = input("\n$ ")

type_it("(^-^) Bye and thanks for using casual_llm :)\n")
