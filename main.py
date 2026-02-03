import sys
from src.crew import AutoResearchCrew


def main():
    print("Welcome to AutoResearch Crew")
    print("-------------------------------")

    if len(sys.argv) > 1:
        topic = sys.argv[1]
    else:
        topic = input("Please enter the topic you want to research: ")

    crew = AutoResearchCrew()
    result = crew.run(topic)

    print("\n\n########################")
    print("## HERE IS THE REPORT ##")
    print("########################\n")
    print(result)


if __name__ == "__main__":
    main()
