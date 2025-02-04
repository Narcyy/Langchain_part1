from langchain.schema.runnable import RunnableLambda
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_messages(
    [
    ("system", "You are an helpfull AI asisstant"),
    ("user", "What is the Squareroot of {number}?")
]
)

runnable = RunnableLambda(lambda x: prompt.format_prompt(**x))

runnable2 = RunnableLambda(lambda x: model.invoke(x.to_messages()))

chain = runnable| runnable2
response = chain.invoke({"number":49})

print(response.content)