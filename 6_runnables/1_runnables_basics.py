from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableLambda


model = ChatOpenAI(model="gpt-4o-mini")

runnable = RunnableLambda(lambda x: x**2)

response = runnable.invoke(5)
print(response)