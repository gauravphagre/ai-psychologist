from core.context import WorkflowContext
from models import RiskLevel, WellnessResult
from prompts.wellness import SYSTEM_PROMPT

from .base import BaseAgent


class WellnessAgent(BaseAgent):
    """
    Provides wellness recommendations for users experiencing
    stress, anxiety, burnout, or similar emotions.
    """

    def __init__(self):
        super().__init__("WellnessAgent")

    def should_execute(
        self,
        context: WorkflowContext,
    ) -> bool:

        # Emotion and risk analysis must exist
        if context.state.emotion is None:
            return False

        if context.state.risk is None:
            return False

        emotion = context.state.emotion.emotion.lower()
        risk = context.state.risk.level

        supported_emotions = {
            "stress",
            "stressed",
            "anxiety",
            "anxious",
            "burnout",
            "overwhelmed",
            "worried",
            "fear",
            "frustrated",
        }

        return (
            risk in (RiskLevel.LOW, RiskLevel.MEDIUM)
            and emotion in supported_emotions
        )

    def execute(
        self,
        context: WorkflowContext,
    ) -> WellnessResult:

        prompt = context.build_prompt(
            [
                "user",
                "emotion",
                "risk",
            ]
        )

        result: WellnessResult = context.llm_service.chat_structured(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=prompt,
            response_model=WellnessResult,
        )

        context.state.wellness = result

        return result