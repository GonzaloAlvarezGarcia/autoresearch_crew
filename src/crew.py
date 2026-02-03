import os
import yaml
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


class AutoResearchCrew:
    """AutoResearch Crew"""

    def __init__(self):
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.model_name = os.getenv("MODEL_NAME", "groq/llama-3.3-70b-versatile")

        # Initialize LLM
        self.llm = ChatGroq(
            temperature=0, groq_api_key=self.groq_api_key, model_name=self.model_name
        )

        # Load Configurations
        self.agents_config = self._load_yaml("src/config/agents.yaml")
        self.tasks_config = self._load_yaml("src/config/tasks.yaml")

        # Initialize Tools
        self.search_tool = SerperDevTool()
        self.scrape_tool = ScrapeWebsiteTool()

    def _load_yaml(self, file_path):
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    def researcher(self):
        config = self.agents_config["senior_researcher"]
        return Agent(
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[self.search_tool, self.scrape_tool],
            max_rpm=10,
        )

    def writer(self):
        config = self.agents_config["technical_writer"]
        return Agent(
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            max_rpm=10,
        )

    def research_task(self, agent, topic):
        config = self.tasks_config["research_task"]
        return Task(
            description=config["description"].format(topic=topic),
            expected_output=config["expected_output"],
            agent=agent,
        )

    def writing_task(self, agent, topic):
        config = self.tasks_config["writing_task"]
        return Task(
            description=config["description"].format(topic=topic),
            expected_output=config["expected_output"],
            agent=agent,
        )

    def run(self, topic: str):
        # 1. Create Agents
        researcher_agent = self.researcher()
        writer_agent = self.writer()

        # 2. Create Tasks
        task1 = self.research_task(researcher_agent, topic)
        task2 = self.writing_task(writer_agent, topic)

        # 3. Create Crew
        crew = Crew(
            agents=[researcher_agent, writer_agent],
            tasks=[task1, task2],
            process=Process.sequential,
            verbose=True,
        )

        # 4. Kickoff
        result = crew.kickoff()
        return result
