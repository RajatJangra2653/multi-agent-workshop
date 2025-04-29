import os
from openai import AzureOpenAI

def manage_task(prompt):
    client = AzureOpenAI(api_key=os.getenv('AZURE_OPENAI_KEY'), endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'))
    response = client.ChatCompletion.create(model="gpt-35-turbo", messages=[{"role": "user", "content": prompt}])
    return response['choices'][0]['message']['content']

print(manage_task("Create a reminder for tomorrow's meeting at 3 PM."))