from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatOpenAI(model="gpt-4o-mini")

chat_history= []

# ADDING THE SYSTEM MESSAGES TO HISTORY
system_prompt = SystemMessage("You are an helpful AI Assistant!")
chat_history.append(system_prompt)

#ADDING USER MESSAGE TO HISTORY, RETRIVE RESPONSE FROM THE ASSISTANT AND APPEND TO HISTORY
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(query))
    prompt = model.invoke(chat_history)
    chat_history.append(prompt.content)
    print(f"AI: {prompt.content}")

print("### Chat History ###")
print(chat_history)