from langchain_openai import ChatOpenAI
import json

model = ChatOpenAI(model="gpt-4o", model_kwargs={ "response_format": { "type": "json_object" } })

# Define schema using JsonSchema
# We should mention json key word and detailed description
query = "What is the Square root of 25, return in json schema with key as answer?"
response = model.invoke(query)
data = json.loads(response.content)
print(data)