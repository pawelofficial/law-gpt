from openai import OpenAI, Completion
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

# start 
id=client.files.create(
  file=open("./data/cleaned_transformed_qa_agreement.txt", "rb"),  # client.fine_tuning.jobs.cancel("ftjob-KnzNA0G6KAlKt1zRj56e07uk")
  purpose="fine-tune"
)
id=id.id
print(id)
#
tup=client.fine_tuning.jobs.create(
  training_file=id, 
  model="gpt-4o-2024-08-06"
)
print(tup) # ftjob-LEPQvO1SYgIky2jscYHXACrK
exit(1)
# end 

## List 10 fine-tuning jobs
#_=client.fine_tuning.jobs.list(limit=1)
#print(_)
#exit(1)
# Retrieve the state of a fine-tune
#client.fine_tuning.jobs.retrieve("ftjob-abc123")
#
## Cancel a job

#
## List up to 10 events from a fine-tuning job
#client.fine_tuning.jobs.list_events(fine_tuning_job_id="ftjob-abc123", limit=10)
#
## Delete a fine-tuned model (must be an owner of the org the model was created in)
#client.models.delete("ft:gpt-3.5-turbo:acemeco:suffix:abc123")

import json

def clean_text(text):
    """Remove or replace non-ASCII characters in the text."""
    return ''.join(char if ord(char) < 128 else '?' for char in text)

def process_file(input_file_path, output_file_path):
    try:
        # Read and clean the data
        with open(input_file_path, 'r', encoding='utf-8') as file:
            # Assuming the input file might contain multiple JSON objects per line
            lines = file.readlines()

        # Process each line
        cleaned_lines = []
        for line in lines:
            try:
                # Parse the JSON data from each line
                data = json.loads(line)
                # Clean the text data; adjust according to the structure of your JSON
                data['text_field'] = clean_text(data['text_field'])
                cleaned_lines.append(json.dumps(data) + '\n')
            except json.JSONDecodeError:
                print("Error decoding JSON from line:", line)

        # Write cleaned data back to a new JSONL file
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            outfile.writelines(cleaned_lines)

        print("File processed and written successfully.")
    except Exception as e:
        print("An error occurred:", e)

    
fp='./data/transformed_qa_agreement.txt'
fp_clean='./data/cleaned_transformed_qa_agreement.txt'

with open(fp,'r',encoding='utf-8') as file:
    text=file.read()
    
clean_text=clean_text(text)

with open(fp_clean,'w') as f:
    for line in clean_text:
        f.write(line)