import fastapi
import uvicorn
from pydantic import BaseModel

app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}



class ChatResponse(BaseModel):
    response: str

class ChatRequest(BaseModel):
    user_prompt: str

@app.post('/chat_response', response_model=ChatResponse)
async def this_chat_response(request: ChatRequest):
    # Process the input and generate a response
    response_text ='I am not sure.'
    return ChatResponse(response=response_text)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)