from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="APIKEY",
)
command='''
// happens automatically done by the model
'''
completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="deepseek/deepseek-chat-v3.1:free",
  messages=[
    {"role": "system","content": "You are a person named debtanu datta who speaks hindi,english as well as bengali. He is from india and is a coder. you analyse chat history and respond like debtanu datta"},
    {"role": "user","content": command}
  ]
)

print(completion.choices[0].message.content)

