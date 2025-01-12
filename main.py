
import argparse
from src.agent import ChillAgent

def main():
    parser = argparse.ArgumentParser(description="Chill Language Model Agent")
    parser.add_argument("--query", type=str, required=True, help="Your query for the Chill Agent")
    args = parser.parse_args()

    # Initialize the ChillAgent and process the query
    agent = ChillAgent()
    response = agent.respond(args.query)
    print(response)

if __name__ == "__main__":
    main()
