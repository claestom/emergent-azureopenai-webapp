import os
from openai import AzureOpenAI
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

class ChatBot():
    def __init__(self, api_key, azure_endpoint, system_prompt):
        # OPENAI authentication
        self.OPENAI_API_KEY = api_key
        self.AZURE_OPENAI_ENDPOINT = azure_endpoint

        # model parameter
        self.system_prompt = system_prompt

        # initialize the message to send each time
        self.message = [{"role": "system", "content": self.system_prompt}]
        
        # chat_history = [(user_msg, assist_msg), (user_msg, assist_msg), ...]
        self.chat_history = []
        
    def initialize(self):
        self.client = AzureOpenAI(
            azure_endpoint=self.AZURE_OPENAI_ENDPOINT,
            api_key=self.OPENAI_API_KEY,
            api_version="2024-02-01"
        )

    def request(self, new_query):
        # if the length of chat history >5, we only keep the the last 5 chat records 
        if len(self.chat_history) > 5:
            self.chat_history = self.chat_history[-5:]

        for human, assistant in self.chat_history:
            self.message.append({"role": "user", "content": human})
            self.message.append({"role": "assistant", "content": assistant})
        
        if new_query != '':
            self.message.append({"role": "user", "content": new_query})

        response = self.client.chat.completions.create(
            model="gpt-4",  # Replace with your model deployment name
            messages=self.message
        )

        # clean up the message list:
        self.message = [{"role": "system", "content": self.system_prompt}]

        # update the chat_history
        self.chat_history.append([new_query, response.choices[0].message.content])

        return response.choices[0].message.content

# # Initialize the ChatBot with the API key, endpoint, and system prompt
# api_key = os.getenv("AZURE_OPENAI_KEY")
# api_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
# bot = ChatBot(api_key, api_endpoint, "You are a helpful assistant.")
# bot.initialize()

# # Make a request to the ChatBot
# question = input("Ask a question: ")
# print(bot.request(question))