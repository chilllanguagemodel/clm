
import openai
import yaml
from src.financial_data import FinancialDataFetcher
from src.recommendations import RecommendationEngine

class ChillAgent:
    def __init__(self, config_path="configs/config.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)
        self.personality = self.config['agent']['personality']
        self.api_key = self.config['api']['openai_key']
        openai.api_key = self.api_key
        self.data_fetcher = FinancialDataFetcher(self.config['api']['financial_api_key'])
        self.recommender = RecommendationEngine()

    def respond(self, query):
        try:
            if "hidden gem" in query:
                recommendations = self.recommender.find_hidden_gems(self.data_fetcher)
                return f"As your chill guide, here are some hidden gems: {', '.join(recommendations)}"
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"You are a chill AI agent. Respond in a relaxed and helpful way.
Query: {query}
Response:",
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"An error occurred: {e}"
