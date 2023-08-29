import os
import json
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Chatbot API class to manage prompts and generate responses
class ChatbotAPI:

    # Initialize with API key and prompts file
    def __init__(self):
        self.prompts_file = 'prompts.json'
        self.api_key = os.environ.get('OPEN_AI_API_KEY', '')
        openai.api_key = self.api_key
        self.prompts = self.load_prompts()

    # Load prompts from JSON file    
    def load_prompts(self):
        if os.path.exists(self.prompts_file):
            with open(self.prompts_file, 'r') as f:
                return json.load(f)
        else:
            # If file doesn't exist, initialize empty prompts
            with open(self.prompts_file, 'w') as f:
                json.dump({"prompts": []}, f)
        return []

    # Save prompts to JSON file
    def save_prompts(self):
        with open(self.prompts_file, 'w') as f:
            json.dump(self.prompts, f, indent=4)

    # Get prompt text by ID
    def get_prompt_text(self, prompt_id):
        for prompt in self.prompts["prompts"]:
            if prompt['promptId'] == prompt_id:
                return prompt['prompt']
        return None

    # Create new prompt 
    def create_prompt(self, prompt_id, prompt_text):

        self.prompts["prompts"].append({"promptId": prompt_id, "prompt": prompt_text})
        self.save_prompts()

    # Update existing prompt
    def update_prompt(self, prompt_id, new_prompt):
        for prompt in self.prompts["prompts"]:
            if prompt["promptId"] == prompt_id:
                prompt["prompt"] = new_prompt
                self.save_prompts()
                return True
        return False

    # Delete prompt by ID
    def delete_prompt(self, prompt_id):
        for prompt in self.prompts["prompts"]:
            if prompt["promptId"] == prompt_id:
                self.prompts["prompts"].remove(prompt)
                self.save_prompts()
                return True
        return False

    # Generate response from OpenAI API
    def generate_response(self, prompt_text):
        if prompt_text:
            prompt = prompt_text + '\nBot:'
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=1000
            )
            return response.choices[0].text.strip()
        return False
