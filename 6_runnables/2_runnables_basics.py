from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableLambda

model = ChatOpenAI(model = "gpt-4o-mini")

def square(x: int):
    return x**2

runnable = RunnableLambda(lambda x: square(x))

response = runnable.invoke(5)
print(response)