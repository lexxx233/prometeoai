import argparse
from src.agent import PrometeoAgent
from src.config import Config

def parse_args():
    parser = argparse.ArgumentParser(description='Prometeo Personal AI Companion')
    parser.add_argument('--config', type=str, help='Path to config file')
    parser.add_argument('--model', type=str, help='Model to use')
    parser.add_argument('--personality', type=str, help='Personality profile to use')
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Initialize configuration with CLI arguments
    config = Config()
    if args.config:
        config.load_from_file(args.config)
    if args.model:
        config.set_model(args.model)
    if args.personality:
        config.set_personality(args.personality)
    
    # Create and start the agent
    agent = PrometeoAgent(config)
    agent.start()

if __name__ == "__main__":
    main()
