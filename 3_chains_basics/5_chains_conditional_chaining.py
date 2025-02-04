from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel, RunnableBranch

model = ChatOpenAI(model ="gpt-4o-mini")

# PRIMARY PROMPT 
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an helpful AI assistant!"),
        ("human", "Classify the sentiment as positve, negative or neutral: {feedback}")
    ]
)

postive_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an helpful AI assistant!"),
        ("human", "Create a postive response for the user feedback: {feedback}")
    ]
)

negative_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an helpful AI assistant!"),
        ("human", "Create a negative response for the user feedback: {feedback}")
    ]
)

neutral_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an helpful AI assistant!"),
        ("human", "Create a nreutral response for the user feedback: {feedback}")
    ]
)

branches = RunnableBranch(
    (
        lambda x: "positive" in x,
        postive_feedback_template | model | StrOutputParser()
    ),
    (
        lambda x: "negative" in x,
        negative_feedback_template | model | StrOutputParser()
    ),
   
    neutral_feedback_template | model | StrOutputParser()

)

feedback_chain = prompt_template | model | StrOutputParser()


chain = feedback_chain | branches
response = chain.invoke({"feedback", "The product is very bad, i don't know how there are selling this."})

print(response)