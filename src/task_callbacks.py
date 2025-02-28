import json
from typing import List, Dict, Callable
import sys
from pydantic import BaseModel
from .output_structure import Tool_Structure, Platform_Structure, Project_Structure


def update_task_output(task_output: str,
                       selection_function: Callable,
                       max_choices: int = 2
                       ) -> str:
    """
    Updates task output based on user selections using provided selection function.
    
    Args:
        task_output (str): The original task output as a JSON string
        selection_function (Callable): Function to handle user selections (one of: user_select_tools, 
                                     user_select_platforms, or user_select_projects)
        max_choices (int): Maximum number of items that can be selected
    
    Returns:
        str: Updated task output based on user selections
    """
    try:
        selected_list = selection_function(task_output, max_choices)
        current_output = load_task_output(task_output)

        if selection_function == user_select_tools:
            current_output["TOOLS_SELECTED"] = selected_list
        elif selection_function == user_select_platforms:
            current_output["PLATFORMS_SELECTED"] = selected_list
        elif selection_function == user_select_projects:
            current_output["PROJECTS_SELECTED"] = selected_list
        else:
            raise ValueError("Invalid Selection Function Provided")
        
        updated_task_output = json.dumps(current_output)
        return updated_task_output
    except Exception as q:
        print(f"Error Updating Task Output: {q}")
        sys.exit(1)


def clean_json_string(json_str: str) -> str:
    try:
        # Find the JSON content
        start_ind = json_str.find('{')
        end_ind = json_str.rfind('}') + 1

        if start_ind == -1 or end_ind == 0:
            raise ValueError("No valid JSON object markers found")
            
        # Extract just the JSON part
        json_content = json_str[start_ind:end_ind]
        
        # Normalize all whitespace within the string
        # This preserves spaces in descriptions while removing problematic whitespace
        lines = json_content.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Remove leading/trailing whitespace from each line
            cleaned_line = line.strip()
            if cleaned_line:  # Only add non-empty lines
                cleaned_lines.append(cleaned_line)
                
        # Rejoin with single spaces
        cleaned_json = ' '.join(cleaned_lines)
        
        # Make sure we haven't broken any valid JSON strings
        # Replace multiple spaces with single space, except within quotes
        in_quotes = False
        result = []
        last_char = ' '
        
        for char in cleaned_json:
            if char == '"' and last_char != '\\':
                in_quotes = not in_quotes
            
            if char == ' ' and not in_quotes and last_char == ' ':
                continue
                
            result.append(char)
            last_char = char
            
        return ''.join(result)
        
    except Exception as q:
        print(f"Error Cleaning JSON String: {q}")
        return json_str


def load_task_output(task_output: str, Structure: BaseModel | None = None) -> Dict:
    """
    Loads and validates task output data.
    
    Args:
        task_output (str | dict): Task output as either a JSON string or dictionary
        Structure (BaseModel): Optional Pydantic model for validation
    
    Returns:
        Dict: Validated data dictionary
    """
    try:
        # First clean the JSON string
        cleaned_output = clean_json_string(task_output)
        
        try:
            # Attempt to parse the cleaned JSON
            data = json.loads(cleaned_output)
        except json.JSONDecodeError as e:
            print("Initial JSON parsing failed, attempting to debug...")
            print(f"Cleaned output preview: {cleaned_output[:200]}...")
            raise e
        
        # Validate against structure if provided
        if Structure is not None:
            validated_data = Structure(**data)
            return validated_data.model_dump()
        return data
        
    except json.JSONDecodeError as q:
        print(f"Error decoding JSON Task Output: {q}")
        print(f"Problem might be near: {cleaned_output[max(0, q.pos-50):min(len(cleaned_output), q.pos+50)]}")
        sys.exit(1)
    except Exception as y:
        print(f"Error validating Task Output data structure: {y}")
        sys.exit(1)

def user_select_tools(tool_options_output: str, max_choices: int = 2) -> List:
    """---"""
    data = load_task_output(tool_options_output, Tool_Structure)
    tools_list = data["TOOLS_LIST"]

    print(f"\nAvailable tools for {data['POSITION']} Role:")
    print("-" * 50)
    for i, tool in enumerate(tools_list, 1):
        tool_info = tool["TOOL"]
        print(f"\n{i}. {tool_info['NAME']}")
        print(f"   Description: {tool_info['DESCRIPTION']}")
    print("\n" + "-" * 50)

    print(f"\nChoose up to {max_choices} tools by entering their numbers.")
    print("Enter numbers separated by spaces (e.g., '1 3')")

    selected_tools = []
    while not selected_tools:
        try:
            tool_choices = []
            tool_choices: list = input("\nYour Selection: ").strip().split()
            if not tool_choices:
                print("Please Enter Atleast one Selection")
            if len(tool_choices) > max_choices:
                print(f"Please select no more than {max_choices} tools.")
                continue

            indices = [int(x) for x in tool_choices]
            for idc in indices:
                if idc < 1 or idc > len(tools_list):
                    raise ValueError(f"Invalid Selection: {idc}")
            selected_tools = [tools_list[idc-1]["TOOL"] for idc in indices]

            print("\nYou selected:")
            for tool in selected_tools:
                print(f"-{tool['NAME']}")
            
            confirm = input("\nConfirm selection? (y/n): ").lower().strip()
            if confirm != 'y':
                selected_tools = []
                print("\nLet's try again.")
                continue

        except ValueError as e:
            print(f"Invalid input. Please enter numbers between 1 and {len(tools_list)}.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
    return selected_tools


def user_select_platforms(platform_options_output: str, max_choices: int = 2) -> List:
    """---"""
    data = load_task_output(platform_options_output, Platform_Structure)
    platform_list = data["PLATFORMS_LIST"]

    print(f"\nAvailable Platforms for {data['POSITION']}:")
    print("-" * 50)
    for i, platform in enumerate(platform_list, 1):
        platform_info = platform["PLATFORM"]
        print(f"\n{i}. {platform_info['NAME']}")
        print(f"   Description: {platform_info['DESCRIPTION']}")
    print("\n" + "-" * 50)

    print(f"\nChoose up to {max_choices} Platforms by entering their numbers.")
    print("Enter numbers separated by spaces (e.g., '1 3')")

    selected_platforms = []
    while not selected_platforms:
        try:
            platform_choices: List[int] = []
            platform_choices = input("\nYour Selection: ").strip().split()
            if not platform_choices:
                print("Please enter at least one selection.")
                continue
            if len(platform_choices) > max_choices:
                print(f"Please select no more than {max_choices} Platforms.")
                continue
            indices = [int(x) for x in platform_choices]
            for idc in indices:
                if idc < 1 or idc > len(platform_list):
                    raise ValueError(f"Invalid Selection: {idc}")
            selected_platforms = [platform_list[idc-1]["PLATFORM"] for idc in indices]

            print("\nYou selected:")
            for platform in selected_platforms:
                print(f"-{platform['NAME']}")
            
            confirm = input("\nConfirm selection? (y/n): ").lower().strip()
            if confirm != 'y':
                selected_platforms = []
                print("\nLet's try again.")
                continue

        except ValueError as e:
            print(f"Invalid input. Please enter numbers between 1 and {len(platform_list)} Separated by Spaces.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    return selected_platforms


def user_select_projects(project_options_output: str, max_choices: int = 2) -> List:
    """---"""
    data = load_task_output(project_options_output, Project_Structure)
    project_list = data["PROJECTS_LIST"]

    print(f"\nAvailable Projects for {data['POSITION']}:")
    print("-" * 50)
    for i, project in enumerate(project_list, 1):
        project_info = project["PROJECT"]
        print(f"\n{i}. {project_info['NAME']}")
        print(f"   Description: {project_info['DESCRIPTION']}")
        print(f"   Pros: {project_info['ADVANTAGES']}")
        print(f"   Cons: {project_info['DISADVANTAGES']}")
    print("\n" + "-" * 50)

    print(f"\nChoose up to {max_choices} Projects by entering their numbers.")
    print("Enter numbers separated by spaces (e.g., '1 3')")

    selected_projects = []
    while not selected_projects:
        try:
            project_choices = []
            project_choices = input("\nYour Selection: ").strip().split()
            if not project_choices:
                print("Please enter at least one selection.")
                continue
            if len(project_choices) > max_choices:
                print(f"Please select no more than {max_choices} tools.")
                continue
            indices = [int(x) for x in project_choices]
            for idc in indices:
                if idc < 1 or idc > len(project_list):
                    raise ValueError(f"Invalid Selection: {idc}")
            selected_projects = [project_list[idc-1]["PROJECT"] for idc in indices]

            print("\nYou selected:")
            for project in selected_projects:
                print(f"-{project['NAME']}")
            
            confirm = input("\nConfirm selection? (y/n): ").lower().strip()
            if confirm != 'y':
                selected_projects = []
                print("\nLet's try again.")
                continue

        except ValueError as e:
            print(f"Invalid input. Please enter numbers between 1 and {len(project_list)} Separated by Spaces.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    return selected_projects


def input_role_to_map() -> Dict:
    """Promps A User on the CLI to Input a Role to Map"""
    print("ROADMAPPER AI:- Planning Your Professional Upskilling Journey...")
    print(print("\n" + "-" * 50))
    position: str = input("Enter A Professional Role You'd Like to Master\nBe As Specific as You Can (e.g Python Backend Web Developer, AWS/GCP Cloud Engineer):- ").strip()
    inputs: dict = {"position": position}
    return inputs