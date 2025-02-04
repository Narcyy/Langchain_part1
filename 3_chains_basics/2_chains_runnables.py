from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence

model = ChatOpenAI(model= "gpt-4o-mini")

# DEFINING PROMPT TEMPLATE
prompt_message = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an facts expert that tell facts about {animal}. Keep them 1 liners."),
        ("human", "Tell me {facts_count} facts."), 
    ]
)

# PREPARING RUNNABLE FOR MESSAGE PROMPTING 
prompt_format = RunnableLambda(lambda x: prompt_message.format_prompt(**x))

# CREATING RUNNABLE FOR CONVERING PROMPT WITH GIVEN VALUES
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))

# PARSING THE OUTPUT
parse_output = RunnableLambda(lambda output: output.content)

# CREATING A RUNNABLE SEQUENCE FOR AVOBE OPERATIONS
chain = RunnableSequence(first=prompt_format, middle=[invoke_model], last= parse_output)

# CREATING AND COMBINING CHAIN
# chain = prompt_message | model | StrOutputParser()

# RUN THE CHAIN
result = chain.invoke({"animal":"dog",
                       "facts_count":1})

print(result)