
from langchain.tools import tool
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from operator import attrgetter
from langchain.schema.runnable import RunnableLambda,RunnableBranch, RunnableParallel
import requests
model =ChatOpenAI(model="gpt-4o-mini")

# Defining function for tool calling
@tool
def get_weather(latitude, longitude):
    """
    This function fetch the current weather in defined location.
    """
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

@tool
def multiply(a,b):
    """
    This function returns the mutiplications given two numbers.
    """
    return a*b
# Register tools
tools= [get_weather, multiply]

# Storing message for conversation history
messages = []

# Binding tool with model
llm = model.bind_tools(tools)


# Query
query = "what is 4 multiplies 6 and what is the temparature in hyderabad??"
messages.append(query)

# Invoking the model with tools
response = llm.invoke(query)
tool_calls = response.tool_calls

# Retrieving the output
for tool_call in tool_calls:
    selected_tool = {"get_weather": get_weather, "multiply": multiply}[tool_call["name"].lower()]
    tool_msg = selected_tool.invoke(tool_call)  # Invoke the model with the tool results
    print(tool_msg)




