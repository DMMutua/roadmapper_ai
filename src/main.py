#!/usr/bin/env python
import sys
import agentops
from crew import RoadmapperaiCrew
from dotenv import load_dotenv
from .task_callbacks import input_role_to_map

load_dotenv() #loads API Keys from .env file

agentops.init(default_tags=['crewai', 'agentstack'])


def run():
    """1 1 
    Run the crew.
    """
    #ins: dict = {'position': 'NLP Machine Learning Engineer'.strip()} #Sample Role
    ins: dict = input_role_to_map()
    # TODO: Add Logic to Handle {role} Input within Shell after Program Execution.
    RoadmapperaiCrew().crew().kickoff(inputs=ins)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs: dict = input_role_to_map()
    try:
        RoadmapperaiCrew().crew().train(n_iterations=int(sys.argv[1]), filen111ame=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    inputs: dict = input_role_to_map()
    try:
        RoadmapperaiCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs: dict = input_role_to_map()
    try:
        RoadmapperaiCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


if __name__ == '__main__':
    run()