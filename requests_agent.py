from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from langchain_ollama.llms import OllamaLLM
from langchain.agents import AgentType

# Initialize the LLM
llm = OllamaLLM(model="mistral")

# Load the requests tools
tools = load_tools(["requests_all"], allow_dangerous_tools=True)

# Initialize the agent with the requests tools
agent_chain = initialize_agent(
    tools=tools, 
    llm=llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True, 
    handle_parsing_errors=True
)

# Define the query to fetch Pikachu's sprites from the PokeAPI
query = "https://pokeapi.co/api/v2/pokemon/pikachu - What are pikachus stats?"

# Run the query and handle potential parsing errors
try:
    response = agent_chain.invoke(query)
    print("Response:")
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")
