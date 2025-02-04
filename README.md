# ROADMAPPER.AI
RoadMapper.AI is an intelligent Gen-AI Agentic Platform that creates personalized, interactive learning roadmaps for professionals looking to master technical tools or transition into new roles.
Using a multi-agent AI system, it generates customized learning paths complete with project suggestions and detailed milestones.
<i>Note:- A Production Ready MVP Of the Project will be Served via a Python Flask API to a Web App Soon</i>

## Features
- Interactive goal clarification and refinement
- Dynamic tool and platform recommendations
- Customized project suggestions with pros and cons
- Detailed project task breakdowns
- Comprehensive stage-based learning roadmaps
- Multiple visualization options for roadmaps

## ROADMAPPER.AI Architecture
### Agentic Structure
The system uses three specialized AI agents:
#### 1. Clarifier Agent
- Role:-  Career Coach specializing in Professional Goals Clarification.
- Purpose:- Helps users clarify their goals and select appropriate tools & platforms.
#### 2. Project Generator Agent
- Role:- Creative Strategist & Innovations Consultant.
- Purpose:- Generating Relevant Project Ideas that when Complete will Demonstrate a a User's Expertise.
#### 3. RoadMapping Agent
- Role:- Learning Journey Architect
- Purpose:- Creation of Detailed, Stage-Based Learning RoadMaps.

## Pilot User Journey
- User inputs desired role/tool
- Clarifier Agent generates tool and platform options
- User selects preferred tools and platforms
- Project Generator suggests portfolio projects
- User selects projects
- Roadmapper creates detailed learning stages
- System presents interactive roadmap

## Tech Stack
1. Backend:- Python 3.x
2. AI Framework: CrewAI & AgentStack
3. LLM: Gemini 1.5 Flash
4. Agents Tracking & Evals: AgentOps
5. Environment Management: python-dotenv
6. Data Structures: Pydantic for Agent Output data validation
7. Configuration: YAML for agent configurations

## Installation
1. Clone the Repository
```bash
git clone https://github.com/DMMutua/roadmapper-ai.git
cd roadmapper-ai
```

2. Create and Activate a Virtual Environment:
```bash
python -m venv .venv
source .venv/Scripts/activate
```

3. Install Dependencies:
```bash
pip install -r requirements.txt
```

4. Set up Environment Variables:
- Create a ```.env``` file in the root directory.
- Add API Keys for AgentOps and LLM Providers.

## Usage
### Basic Usage
To Run the Main Application;
```bash
python src/main.py
```
or 
```bash
crewai run
```
### Training Mode
Training Crew for Specific Iterations:
```bash
python main.py train <n_iterations> <filename>
```

### Replay Mode
For Replaying Specific Task Execution;
```bash
python main.py replay <task_id>
```

### Reset Crew Memory
If you need to reset the memory of your crew before running it again, you can do so by calling the reset memory feature:  
```bash
crewai reset-memory
```

## Development Approach
- Modular Architecture: Separate agents for different aspects of the roadmap generation process.
- Interactive Design: User input and confirmation at key decision points.
- Structured Data Flow: JSON-based data structures for consistent information transfer.
- Error Handling: Comprehensive error checking and user feedback.
- Configurability: YAML-based agent configurations for easy modification.

## License
project is licensed under the MIT License - see the LICENSE file for details.
