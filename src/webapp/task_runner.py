from crewai import Task
from ..crew import RoadmapperaiCrew

def run_single_task(task_name: str, inputs: dict = None) -> str:
    """
    Runs a single task from the RoadmapperaiCrew independently
    
    Args:
        task_name (str): Name of the task to run
        inputs (dict): Input parameters for the task
    
    Returns:
        str: Task output
    """
    crew = RoadmapperaiCrew()

    task_method = getattr(crew, task_name)
    task_instance: Task = task_method()
    result = task_instance.run(inputs=inputs)

    return result