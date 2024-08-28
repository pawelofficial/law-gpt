from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

###id=client.files.create(
###  file=open("./data/transformed_qa.txt", "rb"),
###  purpose="fine-tune"
###)
###
###tup=client.fine_tuning.jobs.create(
###  training_file=id.id, 
###  model="gpt-3.5-turbo"
###)
###print(tup)
#### ftjob-USdFwWXP9gvSMlD0m5jH8KSU

job='ftjob-USdFwWXP9gvSMlD0m5jH8KSU'
# List 10 fine-tuning jobs
_=client.fine_tuning.jobs.list(limit=10)
print(_)
# Retrieve the state of a fine-tune
#client.fine_tuning.jobs.retrieve("ftjob-abc123")
#
## Cancel a job
#client.fine_tuning.jobs.cancel("ftjob-abc123")
#
## List up to 10 events from a fine-tuning job
#client.fine_tuning.jobs.list_events(fine_tuning_job_id="ftjob-abc123", limit=10)
#
## Delete a fine-tuned model (must be an owner of the org the model was created in)
#client.models.delete("ft:gpt-3.5-turbo:acemeco:suffix:abc123")