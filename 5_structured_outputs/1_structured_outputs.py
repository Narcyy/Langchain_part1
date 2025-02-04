from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

model = ChatOpenAI(model="gpt-4o-mini")

# Define schema using Pydantic
class ResponseFormat(BaseModel):
    question: str = Field(description="User question goes here")
    answer: str = Field(description="Answer to the user question")

user_input = "What is the Square root of 25"

# Bind schema to model
model_with_structure = model.bind_tools([ResponseFormat])

# Invoke the model to produce structured output that matches the schema
structured_output = model_with_structure.invoke(user_input)
pydantic_object = ResponseFormat.model_validate(structured_output.tool_calls[0]["args"])
print(pydantic_object)

# Invoke the model to produce structured output that matches the schema using "with_structured_output"
structured_output2= model.with_structured_output(ResponseFormat)
result = structured_output2.invoke(user_input)
print(result)