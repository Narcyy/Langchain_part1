from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableLambda
from langchain.prompts import ChatPromptTemplate

model = ChatOpenAI(model="gpt-4o-mini")

