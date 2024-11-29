from autogen import Agent, run_agents

# Define two agents with specific roles
assistant = Agent(name="Assistant", role="Answer questions and provide solutions.")
researcher = Agent(name="Researcher", role="Search and gather detailed information.")

# Deploy and start the agents
run_agents([assistant, researcher], task="Collaborate to write a summary about AI in healthcare.")
