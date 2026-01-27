from sqlalchemy import Session
from core.config import settings

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplatePromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from core.prompts import STORY_PROMPT
from models.story import Story
from core.models import StoryLLMResponse, StoryNodeLLM


class StoryGenerator:

    @classmethod
    def _get_llm(cls):
        return ChatOpenAI(model="gpt-4-turbo")

    @classmethod
    def generate_story(cls, db: Session, session_id: str, theme: str = "fantasy") -> Story:
        llm = cls._get_llm()
        story_parser = PydanticOutputParser(pydantic_object=StoryLLMResponse)
        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                STORY_PROMPT
            ),
            (
                "human",
                f"Create story with this theme: {theme}"
            )
        ]).partial(format_instructions=story_parser.get_format_instructions())