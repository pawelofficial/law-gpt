from dotenv import load_dotenv
from openai import OpenAI
import os
import re 
import json 

# Load the environment variables from the .env file
load_dotenv()
# from dotenv 

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def call_openai(sys_prompt,user_prompt,client=client,model="gpt-4o-mini"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"{sys_prompt}",
            },
            {
                "role": "user",
                "content": f"{user_prompt}",
            }
        ],
        model=model,
    )
    answer=chat_completion.choices[0].message.content # lmao     
    return answer 

# reads chunk of text from a file 
def read_chunk(fp, min_length=50):
    with open(fp, 'r', encoding="utf-8") as file:
        chunk = []
        for line in file:
            if line.strip() == "":
                if chunk:
                    s = "\n".join(chunk)
                    if len(s) < min_length:
                        s = ""
                    yield s
                    chunk = []
            else:
                chunk.append(line.strip())
        if chunk:
            s = "\n".join(chunk)
            if len(s) < min_length:
                s = ""
            yield s

def count_chunks(fp, chunk_size):
    chunk_count = 0
    with open(fp, 'r', encoding="utf-8") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            chunk_count += 1
    return chunk_count
#print (chat_completion)

def parse_to_json(text,context):
    qa_pairs = []
    question_pattern = re.compile(r'<question>(.*?)</question>', re.DOTALL)
    answer_pattern = re.compile(r'<answer>(.*?)</answer>', re.DOTALL)

    questions = question_pattern.findall(text)
    answers = answer_pattern.findall(text)
    for question, answer in zip(questions, answers):
        qa_pairs.append({
            "question": question.strip(),
            "answer": answer.strip()
            ,"context":context
        })

    return qa_pairs


def dump_js(js_list,mode, fp='./data/qa.txt'):
    with open(fp, mode, encoding='utf-8') as file:
        for js in js_list:
            file.write(json.dumps(js, ensure_ascii=False))
            file.write('\n')

fp='./data/processed/agreement.txt'
chunk_size=2048
num_chunks = count_chunks(fp, chunk_size)

#if __name__=='__main__':


sys_prompt="""Given provided text write me 3-4 comprehensive question - answer pairs that corresponds to it.
Embed the QA in html tags <question>...</question> <answer>...</answer>""" 

mode='w'
for no,chunk in enumerate(read_chunk(fp)):
#    print(chunk)
#    print(len(chunk))
#    input('wait')
    if chunk=='':
        continue
    a=call_openai(sys_prompt=sys_prompt,user_prompt=chunk)
    js=parse_to_json(a,chunk)
    print(js)
    dump_js(js,mode=mode,fp='./data/qa_agreement.txt')
    mode='a'

        