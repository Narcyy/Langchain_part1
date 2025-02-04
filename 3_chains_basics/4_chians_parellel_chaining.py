from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel

model = ChatOpenAI(model ="gpt-4o-mini")

# PRIMARY PROMPT 
prompt_template = ChatPromptTemplate(
    [
        ("system", "You are good movie critic"),
        ("human", "Give me a breif review of movie {movie_name}")
    ]
)

# PREPARING PROMPTS
def plot_analysis(plot):
    plot_template = ChatPromptTemplate(
    [
        ("system", "You are good movie critic"),
        ("human", "Give me a breif analysis about movie {plot}")
    ]
    )
    return plot_template.format_prompt(plot= plot)

def character_analysis(characters):
    character_template = ChatPromptTemplate(
    [
        ("system", "You are good movie critic"),
        ("human", "Give me a breif analysis about movie characters {characters}, stenght and weakness")
    ]
    )

    return character_template.format_prompt(characters = characters)

# COMBAINING BOTH RESULTS
def combine_verdicts(plot_analysis, character_analysis):
    return f"Plot analysis: {plot_analysis},\n\nCharacter analysis: {character_analysis}"

# CREATING CHAINS FOR PARELLEL EXECUTION
plot_branch_chain = RunnableLambda(lambda x: plot_analysis(x)) | model|StrOutputParser()
character_branch_chain = RunnableLambda(lambda x: character_analysis(x)) | model |StrOutputParser()

# MAIN CHAIN THAT HANLES THE BRANCHES
chain = (
    prompt_template
    | model
    | StrOutputParser()
    | RunnableParallel(branches ={"plot":plot_branch_chain, "characters": character_branch_chain})
    | RunnableLambda(lambda x: combine_verdicts(x["branches"]["plot"], x["branches"]["characters"]))

)

result = chain.invoke({"movie_name":"Jalsa 2008"})

print(result)