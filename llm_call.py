# llm_call.py (inside level1/)

import openai

openai.api_key = "your-api-key-here"  # Replace with your OpenAI key

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or another model
    messages=[
        {"role": "user", "content": "What is the capital of Japan?"}
    ]
)

print("LLM Response:", response['choices'][0]['message']['content'])

