from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import WebsiteSearchTool
from ai_value_investing.tools.pe_tool import StockInfoTools

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class AiValueInvesting():
    """AiValueInvesting crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @agent
    def stock_query_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_query'],
            tools=[StockInfoTools.get_stock_pe],
            verbose=True
        )
 
    @task
    def stock_query_analysis(self) -> Task: 
        return Task(
            config=self.tasks_config['stock_query'],
            agent=self.stock_query_agent(),
        )


    @agent
    def financial_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_analyst'],
            verbose=True
        )
    
    @task
    def financial_analysis(self) -> Task: 
        return Task(
            config=self.tasks_config['financial_analysis'],
            agent=self.financial_agent(),
        )

    @agent
    def ben_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['ben-graham-analyst'], # type: ignore[index]
            verbose=True
        )

    @task
    def ben_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['ben-graham-analyst'], # type: ignore[index]
            agent=self.ben_researcher(),
        )

    @agent
    def buffett_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['warren_buffett_analyst'], # type: ignore[index]
            verbose=True
        )

    @task
    def buffett_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['warren_buffett_analyst'], # type: ignore[index]
            agent=self.buffett_researcher(),
        )


    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['investment_advisor'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['recommend'], # type: ignore[index]
            agent=self.reporting_analyst(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AiValueInvesting crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            output_log_file=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
