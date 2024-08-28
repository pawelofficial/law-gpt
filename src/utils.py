import requests 
from openai import OpenAI
def send_request(endpoint, data,method='GET' ):
    url=f'http://127.0.0.1:8000/{endpoint}'
    if method=='GET':
        response = requests.get(url, params=data)
    elif method=='POST':
        response = requests.post(url, json=data)
    return response.json()



def openai_completion(user_prompt='hello!'
                      ,model='ft:gpt-3.5-turbo-0125:personal::A1EFRSfA'
                      ,job='ftjob-USdFwWXP9gvSMlD0m5jH8KSU'):
    client = OpenAI()
    if model is None:
        _=client.fine_tuning.jobs.retrieve(job)
        model=_.fine_tuned_model
    completion = client.chat.completions.create(
      model=model,
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"{user_prompt}"}
      ]
    )
    
    return completion.choices[0].message.content

def hello():
    return 'hello'