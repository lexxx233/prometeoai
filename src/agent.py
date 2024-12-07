from src.core.model_management.model_orchestrator import ModelManager
from src.core.memory_management.memory_orchestrator import MemoryManager
from src.core.personality_management.personality_orchestrator import PersonalityManager
from src.interfaces.user_interface import UserInterface
from src.interfaces.model_interface import ModelInterface
from src.interfaces.system_interface import SystemInterface
from src.io.input.input_processor import InputProcessor
from src.io.output.output_processor import OutputProcessor

class PrometeoAgent:
    def __init__(self, config):
        # Initialize core components
        self.model_manager = ModelManager(config)
        self.memory_manager = MemoryManager(config)
        self.personality_manager = PersonalityManager(config)
        
        # Initialize interfaces
        self.user_interface = UserInterface(config)
        self.model_interface = ModelInterface(config)
        self.system_interface = SystemInterface(config)
        
        # Initialize I/O processors
        self.input_processor = InputProcessor(config)
        self.output_processor = OutputProcessor(config)

    def start(self):
        """Main loop of the agent"""
        try:
            self.user_interface.initialize()
            while True:
                # Get input from user
                user_input = self.user_interface.get_input()
                
                # Process input
                processed_input = self.input_processor.process(user_input)
                
                # Get response from model
                response = self.model_interface.get_response(processed_input)
                
                # Update memory
                self.memory_manager.update(user_input, response)
                
                # Generate output
                output = self.output_processor.generate(response)
                
                # Send to user
                self.user_interface.send_output(output)
                
        except KeyboardInterrupt:
            self.cleanup()

    def cleanup(self):
        """Cleanup resources before shutting down"""
        self.memory_manager.save()
        self.user_interface.cleanup()
