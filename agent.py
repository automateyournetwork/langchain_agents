from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from langchain_ollama.llms import OllamaLLM

# Initialize the LLM
llm = OllamaLLM(model="mistral")

tools = load_tools(["llm-math", "wikipedia", "serpapi"], llm=llm)
# Create the agent using the new method
agent = initialize_agent(
    tools=tools,
    llm=llm,
    verbose=True,
    handle_parsing_errors=True
)

# # Standard LLM Query with error handling for output parsing errors
try:
    response = agent.invoke("What is the golden ratio?", handle_parsing_errors=True)
    print("Raw response:")
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")









# Load the tools you need
#"serpapi"
#"wikipedia"
#"terminal",allow_dangerous_tools=True
#"arxiv"