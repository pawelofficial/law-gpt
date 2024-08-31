from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
# file-vzNjqbcAewsjFXYkIlQvcTp1
file_id='file-vzNjqbcAewsjFXYkIlQvcTp1'
ft_id='ftjob-TUmnPfxH5CzcgB1bOAPXHmfj'
#exit(1)
id=client.files.create(
  file=open("./data/transformed_qa_agreement.txt", "rb"),  # client.fine_tuning.jobs.cancel("ftjob-KnzNA0G6KAlKt1zRj56e07uk")
  purpose="fine-tune"
)
id=id.id
print(id)
#
tup=client.fine_tuning.jobs.create(
  training_file=file_id, 
  model="gpt-4o-2024-08-06"
)
print(tup) # ftjob-LEPQvO1SYgIky2jscYHXACrK
exit(1)


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