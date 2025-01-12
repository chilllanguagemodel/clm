
import unittest
from src.agent import ChillAgent

class TestChillAgent(unittest.TestCase):
    def test_response(self):
        agent = ChillAgent()
        response = agent.respond("What is a good stock to buy?")
        self.assertTrue(isinstance(response, str))

if __name__ == "__main__":
    unittest.main()
