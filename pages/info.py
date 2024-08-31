import streamlit as st 
import pandas as pd 
import json 
s="""
This is a gpt fine tuned LLM for talking to this document https://contracts.justia.com/companies/amgen-inc-93/contract/565667/

currently it can only zero shot a question answer, aka you can ask 
    What is this agreement about?
You get an answer, but there is no follow up available, aka this wont work:
    - What is this agreement about?
    - This is an agreement is about XXX
    - Are you sure? ( this will be sent as a standalone question rather than a follow up to above conversation)

it's trained on ~2/3rds of the document due to context limitations 

"""



st.write(s)
fp='./data/transformed_qa_agreement_short.txt'



@st.cache_resource  # This decorator will cache the results of the function
def load_and_process_data(filepath):
    data = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            json_line = json.loads(line)
            messages = json_line['messages']
            question = messages[1]['content']
            answer = messages[2]['content']
            data.append({'question': question, 'answer': answer})
    return pd.DataFrame(data)

# Usage of the cached function
fp = './data/transformed_qa_agreement_short.txt'
df = load_and_process_data(fp)

# Displaying the DataFrame in Streamlit
st.write('training data used: ')
st.write(df)