from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda

model = ChatOpenAI(model= "gpt-4o-mini")

# DEFINING PROMPT TEMPLATE
prompt_message = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an facts expert that tell facts about {animal}. Keep them 1 liners."),
        ("human", "Tell me {facts_count} facts."), 
    ]
)
# DEFINING ANOTHER PROMPT
translation_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "translate the text into {language}, {text}")
    ]
)
# CREATING A RUNNABLE FOR PROMT COMPLETING

translate = RunnableLambda(lambda output: {"language":"telugu", "text": output})


chain = prompt_message | model | StrOutputParser() | translate | translation_prompt | model | StrOutputParser()

response = chain.invoke({"animal":"dog", "facts_count": 1})

print(response)
