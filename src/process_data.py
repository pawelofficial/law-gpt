import json

def transform_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            data = json.loads(line.strip())
            question = data.get("question", "")
            answer = data.get("answer", "")
            
            transformed_data = {
                "messages": [
                    {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
                    {"role": "user", "content": question},
                    {"role": "assistant", "content": answer}
                ]
            }
            
            json.dump(transformed_data, outfile, ensure_ascii=False)
            outfile.write('\n')

# Usage
transform_file('./data/qa.txt', './data/transformed_qa.txt')