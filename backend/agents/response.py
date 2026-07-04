"""
Response Agent

Responsibility:
- Generate the final empathetic response
- Use outputs from Emotion, Risk, and Therapy agents
- Use conversation history for context
- Save assistant response to memory
"""

from agents.base import BaseAgent
from core.context import WorkflowContext
from models import ResponseResult
from prompts.response import SYSTEM_PROMPT


class ResponseAgent(BaseAgent):
    """
    Final agent in the workflow.

    Produces the user-facing psychological response.
    """

    def __init__(self):
        super().__init__("ResponseAgent")

    def execute(self, context: WorkflowContext) -> dict:
        """
        Generate final empathetic response using full context.
        """

        response: ResponseResult = context.llm_service.chat_structured(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=context.build_prompt(
                [
                    "history",
                    "user",
                    "emotion",
                    "risk",
                    "wellness",
                    "safety",
                    "therapy",
                    "resources",
                ]
            ),
            response_model=ResponseResult,
        )

        # Save to workflow state
        context.state.response = response

        # Persist assistant message in memory
        self._save_to_memory(context, response.response)

        return response.model_dump()

    def _save_to_memory(self, context: WorkflowContext, text: str):
        """
        Store assistant response in conversation memory.
        """

        context.memory_service.add_message(
            session_id=context.session_id,
            role="assistant",
            content=text,
        )