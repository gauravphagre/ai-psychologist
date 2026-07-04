"""
Risk Assessment Agent

Responsibility:
- Assess the user's message for potential mental health risk.
- Detect LOW, MEDIUM, or HIGH risk.
- Store the assessment in the workflow state.
"""

from agents.base import BaseAgent
from core.context import WorkflowContext
from models import RiskResult
from prompts.risk import SYSTEM_PROMPT


class RiskAgent(BaseAgent):
    """
    Uses the LLM to assess the user's message for
    potential self-harm or crisis indicators.
    """

    def __init__(self):
        super().__init__("RiskAgent")

    def execute(
        self,
        context: WorkflowContext,
    ) -> dict:
        """
        Analyze the user's message and determine
        the current mental health risk level.
        """

        risk: RiskResult = context.llm_service.chat_structured(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=context.user_message,
            response_model=RiskResult,
        )

        # Save the result in the shared workflow state
        context.state.risk = risk

        # Return output for workflow history
        return risk.model_dump()