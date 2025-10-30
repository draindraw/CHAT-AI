from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)
command='''[10:35 PM, 9/14/2025] Bipul: Teree
[10:36 PM, 9/14/2025] Bipul: Kyaa
[8:46 AM, 9/15/2025] Bipul: Raat mai niklege
[8:46 AM, 9/15/2025] Bipul: 11.30
[8:46 AM, 9/15/2025] Bipul: Ko
[8:49 AM, 9/15/2025] Bipul: Titin aaj khegaa
[8:49 AM, 9/15/2025] Bipul: Chicken subh
[9:06 AM, 9/15/2025] Debtanu datta: Ye kya matlab hai bhai
[9:06 AM, 9/15/2025] Debtanu datta: Nhi ho sakta jab kyu kar raha hai
[9:07 AM, 9/15/2025] Bipul: Abee tunee hmee prty di hmee bhi toh deni hai isliyee kr rha hu
[9:08 AM, 9/15/2025] Debtanu datta: Toh abhi possible nhi hai na
[9:08 AM, 9/15/2025] Bipul: Kb hai btegaa
[9:08 AM, 9/15/2025] Bipul: Shaam mai
[9:08 AM, 9/15/2025] Bipul: Aajioo bnaa ke rkhege
[9:10 AM, 9/15/2025] Debtanu datta: Chomu abhi busy hu meri maa agyi hai
[9:10 AM, 9/15/2025] Debtanu datta: Abhi iss mahine nhi hoga'''
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