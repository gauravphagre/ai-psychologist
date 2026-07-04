from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config import settings

T = TypeVar("T", bound=BaseModel)


class LLMService:
    """
    Wrapper around the OpenAI client.

    Supports:
    - Plain text responses
    - Structured (Pydantic) responses
    """

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def chat(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        """
        Returns a plain text response.
        """

        response = self.client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        )

        return response.choices[0].message.content

    def chat_structured(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: type[T],
    ) -> T:
        """
        Returns a validated Pydantic model.
        """

        response = self.client.responses.parse(
            model=settings.MODEL_NAME,
            input=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            text_format=response_model,
        )

        return response.output_parsed