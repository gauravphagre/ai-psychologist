"""
Emotion Agent

Responsibility:
- Analyze the user's message
- Detect the primary emotion
- Estimate emotional intensity (1-10)
- Store the result in the workflow state
"""

from agents.base import BaseAgent
from core.context import WorkflowContext
from models import EmotionResult
from prompts.emotion import SYSTEM_PROMPT


class EmotionAgent(BaseAgent):
    """
    Detects the user's primary emotion using the LLM.
    """

    def __init__(self):
        super().__init__("EmotionAgent")

    def execute(self, context: WorkflowContext) -> dict:
        """
        Analyze the user's message and update the workflow state.
        """

        emotion: EmotionResult = context.llm_service.chat_structured(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=context.user_message,
            response_model=EmotionResult,
        )

        # Save to workflow state
        context.state.emotion = emotion

        # Return output for workflow execution history
        return emotion.model_dump()