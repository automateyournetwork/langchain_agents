from langchain_community.tools import ShellTool
from langchain.agents import initialize_agent
from langchain_ollama.llms import OllamaLLM
from langchain.agents import AgentType

# Initialize the LLM
llm = OllamaLLM(model="mistral")

# Initialize the ShellTool
shell_tool = ShellTool()

# Initialize the agent with the ShellTool and LLM_MathTool
agent_chain = initialize_agent(
    tools=[shell_tool], 
    llm=llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True, 
    handle_parsing_errors=True
)

# Define the SSH command to connect to your device
pyats_command = 'pyats parse "show interfaces" --testbed-file testbed.yaml'

# Run the SSH command and handle potential parsing errors
try:
    response = agent_chain.invoke(f"Run the following shell command: {pyats_command}. Then analyze the JSON response to determine if any interfaces have output drops and provide the names of those interfaces.")
    print("Response:")
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")
