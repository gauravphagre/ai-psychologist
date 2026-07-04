"""
Therapy Agent

Responsibility:
- Recommend an appropriate therapeutic technique
- Use Emotion + Risk assessment
- Update the workflow state
"""

from agents.base import BaseAgent
from core.context import WorkflowContext
from models import TherapyResult
from prompts.therapy import SYSTEM_PROMPT


class TherapyAgent(BaseAgent):
    """
    Therapy recommendation agent.

    Uses previous workflow outputs to recommend
    an appropriate therapeutic technique.
    """

    def __init__(self):
        super().__init__("TherapyAgent")

    def execute(
        self,
        context: WorkflowContext,
    ) -> dict:
        """
        Generate a therapy recommendation using
        the user's message, detected emotion,
        and assessed risk level.
        """

        therapy: TherapyResult = context.llm_service.chat_structured(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=context.build_prompt(
                [
                    "user",
                    "emotion",
                    "risk",
                ]
            ),
            response_model=TherapyResult,
        )

        # Save into workflow state
        context.state.therapy = therapy

        # Return output for workflow history
        return therapy.model_dump()