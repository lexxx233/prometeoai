from src.agent import PrometeoAgent
from src.config import Config

def main():
    # Initialize configuration
    config = Config()
    
    # Create and start the agent
    agent = PrometeoAgent(config)
    agent.start()

if __name__ == "__main__":
    main()
