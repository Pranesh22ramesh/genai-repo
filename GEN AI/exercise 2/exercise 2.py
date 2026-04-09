import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.tools import tool

load_dotenv()
model = ChatGroq(
    model_name=os.getenv("APIKEY"),
    temperature=0.1,
    groq_api_key=os.getenv("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"),
)

@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)

tools = [get_word_length]

agent = create_agent(
    model, 
    tools=tools, 
    system_prompt="You are a helpful assistant."
)

inputs = {"messages": [{"role": "user", "content": "How many letters are in the word 'GENAI'?"}]}
response = agent.invoke(inputs)

final_message = response["messages"][-1]
print(f"\nFinal Answer: {final_message.content}")