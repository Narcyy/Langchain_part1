from langchain_openai import ChatOpenAI
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field
from langchain.tools import tool

model =ChatOpenAI(model="gpt-4o-mini")

class CalculatorInput(BaseModel):
    a: int = Field(description="first number")
    b: int = Field(description="second number")

    result: int =Field(description="Result of the multiplication")

def multiply(a: int, b: int):
    """Multiply two numbers."""
    return a * b

@tool("multiplication-tool", args_schema=CalculatorInput, return_direct=True)
def multiply_using_tool_deco(a: int, b: int):
    """Multiply two numbers."""
    return a * b

query = "What is 2 mulitplied 4?"

# Response using "StructuredTool"
calculator = StructuredTool.from_function(func=multiply)
response = calculator.invoke({"a":2, "b":4})
print(response)

# Response using @tool Decorator
tools= [multiply_using_tool_deco]
model_with_tools = model.bind_tools(tools)
prompt = model_with_tools.invoke(query)
