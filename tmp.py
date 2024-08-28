import dotenv 
from openai import OpenAI
import os
from src import utils 
dotenv.load_dotenv()


_=utils.openai_completion(user_prompt='Jaki dokument jest omawiany w treści?')
print(_)
