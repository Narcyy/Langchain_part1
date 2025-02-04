from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

response = model.invoke("Hello AI")
print(response.content)

# STREAM THE RESPONSE
stream_response = model.stream("Hello AI")
for token in stream_response:
    print(token.content, end="")


