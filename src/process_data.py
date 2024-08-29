import json
import pandas as pd 
import os 

def transform_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            data = json.loads(line.strip())
            question = data.get("question", "")
            answer = data.get("answer", "")
            context=data.get("context","")
            transformed_data = {
                "messages": [
                    {"role": "system", "content": f"You are a chatbot for lawyers here is context to below question and answer: \n {context}"},
                    {"role": "user", "content": question},
                    {"role": "assistant", "content": answer}
                ]
            }
            
            json.dump(transformed_data, outfile, ensure_ascii=False)
            outfile.write('\n')

def qa_to_df(fp):
    df=pd.DataFrame(columns=['question','answer','context'])
    with open(fp, 'r', encoding='utf-8') as infile:
        for line in infile:
            data = json.loads(line.strip())
            question = data.get("question", "")
            answer = data.get("answer", "")
            context = data.get("context", "")
            df.loc[len(df)] = [question,answer,context]
            
    fname = os.path.basename(fp)
    print(fname)
    output_dir = './data/processed'
    
    # Ensure the directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Construct the output file path
    fname=fname.split('.')[0]
    output_path = os.path.join(output_dir, f'df_{fname}.csv')
    
    # Save the DataFrame to a CSV file
    df.to_csv(output_path, index=False)
    print(f"DataFrame saved to {output_path}")

# Usage
transform_file('./data/qa_agreement.txt', './data/transformed_qa_agreement.txt')


# Usage
#transform_file('./data/qa_agreement.txt', './data/transformed_qa_agreement.txt')
qa_to_df('./data/qa_agreement.txt')