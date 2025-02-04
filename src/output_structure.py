from pydantic import BaseModel
from typing import List, Optional

class Tool(BaseModel):
    NAME: str
    DESCRIPTION: str


class Platform(BaseModel):
    NAME: str
    DESCRIPTION: str

class Project(BaseModel):
    NAME: str
    DESCRIPTION: str
    ADVANTAGES: str
    DISADVANTAGES: str


class ToolWrapper(BaseModel):
    TOOL: Tool


class PlatformWrapper(BaseModel):
    PLATFORM: Platform

class ProjectWrapper(BaseModel):
    PROJECT: Project

class Tool_Structure(BaseModel):
    POSITION: str
    TOOLS_LIST: List[ToolWrapper]

    class Config:
        json_schema_extra = {
            "example": {
                "POSITION": "NLP Machine Learning Engineer",
                "TOOLS_LIST": [
                    {
                        "TOOL": {
                            "NAME": "TensorFlow",
                            "DESCRIPTION": "An open-source library developed by Google."
                        }
                    },
                    {
                        "TOOL": {
                            "NAME": "PyTorch",
                            "DESCRIPTION": "Another popular open-source library."
                        }
                    }
                ]
            }
        }


class Platform_Structure(BaseModel):
    POSITION: str
    TOOLS_SELECTED: List[str]
    PLATFORMS_LIST: List[PlatformWrapper]

    class Config:
        json_schema_extra = {
            "example": {
                "POSITION": "NLP Machine Learning Engineer",
                "TOOLS_SELECTED": ["TensorFlow", "spaCy"],
                "PLATFORMS_LIST": [
                    {
                        "PLATFORM": {
                            "NAME": "Google Cloud Platform (GCP)",
                            "DESCRIPTION": "Offers a suite of services ideal for deploying and scaling NLP models."
                        }
                    },
                    {
                        "PLATFORM": {
                            "NAME": "Amazon Web Services (AWS)",
                            "DESCRIPTION": "Provides a comprehensive cloud platform with various services relevant to NLP."
                        }
                    }
                ]
            }
        }

class Project_Structure(BaseModel):
    POSITION: str
    TOOLS_SELECTED: List[str]
    PLATFORMS_SELECTED: List[str]
    PROJECTS_LIST:List[ProjectWrapper]

    class Config:
        json_schema_extra = {
            "example": {
                "POSITION": "NLP Machine Learning Engineer",
                "TOOLS_SELECTED": ["TensorFlow", "spaCy"],
                "PLATFORMS_SELECTED": ["Google Cloud Platform (GCP)", "Hugging Face Hub"],
                "PROJECTS_LIST": [
                    {
                        "PROJECT": {
                            "NAME": "Multilingual Customer Support Chatbot",
                            "DESCRIPTION": "Build an advanced NLP-powered chatbot capable of understanding and responding to customer queries in multiple languages. The system will use TensorFlow for the core NLP model and deploy on GCP for scalability.",
                            "ADVANTAGES": "High scalability with GCP infrastructure, robust NLP capabilities with TensorFlow, support for multiple languages, reduced customer service costs, 24/7 availability, consistent service quality",
                            "DISADVANTAGES": "Initial development costs may be high, requires extensive training data in multiple languages, ongoing maintenance and updates needed, may not handle very complex queries effectively"
                        }
                    },
                    {
                        "PROJECT": {
                            "NAME": "Real-time Text Analytics Platform",
                            "DESCRIPTION": "Develop a real-time text analysis system that processes social media feeds and customer feedback to extract sentiment, trends, and key insights using spaCy for NLP processing and Hugging Face models for advanced analysis.",
                            "ADVANTAGES": "Real-time insights, scalable processing pipeline, pre-trained models availability, flexible integration with various data sources, comprehensive analytics capabilities",
                            "DISADVANTAGES": "Complex system architecture, potential high computing costs, requires regular model updates, needs robust error handling for real-time processing"
                        }
                    },
                    {
                        "PROJECT": {
                            "NAME": "Automated Document Classification System",
                            "DESCRIPTION": "Create an intelligent document classification system that automatically categorizes and routes documents based on their content, using TensorFlow for model training and GCP for deployment.",
                            "ADVANTAGES": "Automated workflow, reduced manual processing, scalable architecture, integration with existing systems, improved accuracy over time",
                            "DISADVANTAGES": "Requires extensive initial training data, may need frequent model retraining, potential for misclassification, requires fallback procedures"
                        }
                    }
                ]
            }
        }