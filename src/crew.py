from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from output_structure import Tool_Structure, Platform_Structure, Project_Structure
from task_callbacks import update_task_output, user_select_tools, user_select_platforms, user_select_projects
#import tools

@CrewBase
class RoadmapperaiCrew():
    """roadmapper_ai crew"""

    @agent
    def Clarifier(self) -> Agent:
        return Agent(
            config=self.agents_config['Clarifier'],
            tools=[], # add tools here or use `agentstack tools add <tool_name>
            verbose=True,
        )

    @agent
    def Project_Gen(self) -> Agent:
        return Agent(
            config=self.agents_config['Project_Gen'],
            tools=[],
            verbose=True,
        )

    @agent
    def Roadmapper(self) -> Agent:
        return Agent(
            config=self.agents_config['Roadmapper'],
            tools=[], 
        )

    # TASK DEFINITIONS

    @task
    def tool_options(self) -> Task:
        return Task(
            config=self.tasks_config['tool_options'],
            output_json=Tool_Structure,
            #human_input=True,
            callback=lambda output: update_task_output(
                task_output=output.raw,
                selection_function=user_select_tools,
                max_choices=2
            )
            )
    # TODO: Add function to support making tool choices for {role} after task complete

    @task
    def platform_options(self) -> Task:
        return Task(
            config=self.tasks_config['platform_options'],
            output_json=Platform_Structure,
            context=[self.tool_options()],
            callback=lambda output: update_task_output(
                task_output=output.raw,
                selection_function=user_select_platforms,
                max_choices=2
            )
        )
    # TODO: Add function to support making platform choices for {role} after task complete
    @task
    def project_options(self) -> Task:
        return Task(
            config=self.tasks_config['project_options'],
            context=[self.tool_options(),
                     self.platform_options()],
            output_json=Project_Structure,
            #human_input=True,
            callback=lambda output: update_task_output(
                task_output=output.raw,
                selection_function=user_select_projects,
                max_choices=2
            )
        )
    # TODO: Add function to support making project choices for portfolio of {role} after task complete

    @task
    def project_TODO(self) -> Task:
        return Task(
            config=self.tasks_config['project_TODO'],
            context=[self.project_options()]
        )

    @task
    def stage_gen(self) -> Task:
        return Task(
            config = self.tasks_config['stage_gen'],
            context = [self.tool_options(), self.platform_options(), self.project_TODO()]
        )

    @task
    def stage_expound(self) -> Task:
        return Task(
            config=self.tasks_config['stage_expound'],
            context = [self.stage_gen()]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Test crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=False,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )