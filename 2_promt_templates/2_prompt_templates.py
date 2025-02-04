from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

# OPENAI MESSAGE FORMAT
openai_messages = [
    ("system", "You are an helpful AI that tells jokes on {type}. keep them 1 line."),
    ("human", "Tell me {count} jokes")
]
# LANGCHAIN MESSAGE FORMAT
langchain_messages = [
    SystemMessage("You are an helpful AI that tells jokes on {type}. Keep them 1 line."),
    HumanMessage("Tell me {count} jokes")
]
# CREATE LANGCHAIN SUPPORTED PROMPT
prompt_messages = ChatPromptTemplate.from_messages(langchain_messages)
prompt = prompt_messages.invoke({
    "type":"life",
    "count":2
})


response  = model.invoke(prompt)

print(response.content)

