from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

# Configure the API key for Google Gemini
genai.configure(api_key="AIzaSyCUo9v0WB5WB5-IZPQklBhrJ374dqD2Ae8")

app = FastAPI()

# CORS settings for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserMessage(BaseModel):
    message: str

# Function to interact with Gemini AI for generating chat responses
def ask_gemini(message: str) -> str:
    try:
        # Initialize the chat with Gemini model (e.g., "gemini-2.0-flash")
        model = genai.GenerativeModel("gemini-2.0-flash")
        chat = model.start_chat()
        response = chat.send_message(message)
        
        # Return the generated response from Gemini
        return response.text.strip()

    except Exception as e:
        # Handle any error and return a message
        return f"Oops! Something went wrong. ({str(e)})"

@app.post("/chat")
async def chat(user_msg: UserMessage):
    # Get response from Gemini AI based on user input
    reply = ask_gemini(user_msg.message)
    return {"response": reply}
