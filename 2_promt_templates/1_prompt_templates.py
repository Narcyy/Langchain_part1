from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

template = "Create a {tone} mail for the {company} to the {position} with {skills}. keep it for max 4 lines"

prompt_message = ChatPromptTemplate.from_template(template)
prompt = prompt_message.invoke({
    "tone" : "energetic",
    "company" : "microsoft",
    "position" : "AI Engineer",
    "skills" : "Python, Agent Frameworks"

})

response = model.invoke(prompt)

print(response.content)