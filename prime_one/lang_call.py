import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

def openai_invoke():
    # Load the .env file
    load_dotenv()

    # Access the OPENAI_API_KEY environment variable
    openai_api_key = os.getenv("OPENAI_API_KEY")

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        max_tokens = 20,
        api_key=openai_api_key)
    messages = [
    (
        "system",
        "You are a helpful translator. Translate the user sentence to French.",
    ),
    ("human", "I love programming."),
    ]
    print("local message: invoking llm open ai")
    print(llm.invoke(messages)) 
    print("local message: invoking llm open ai complete")
    print("---------------------------------------------------")

