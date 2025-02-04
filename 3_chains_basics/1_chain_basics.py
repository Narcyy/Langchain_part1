from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

model = ChatOpenAI(model= "gpt-4o-mini")

# DEFINING PROMPT TEMPLATE
prompt_message = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an facts expert that tell facts about {animal}. Keep them 1 liners."),
        ("human", "Tell me {facts_count} facts."), 
    ]
)

# CREATING AND COMBINING CHAIN
chain = prompt_message | model | StrOutputParser()

# RUN THE CHAIN
result = chain.invoke({"animal":"dog",
                       "facts_count":1})

print(result)
