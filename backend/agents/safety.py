from core.context import WorkflowContext
from models import RiskLevel, SafetyResult

from .base import BaseAgent


class SafetyAgent(BaseAgent):
    """
    Executes only for HIGH risk situations.

    Produces structured safety guidance that will later
    be incorporated by the ResponseAgent.
    """

    def __init__(self):
        super().__init__("SafetyAgent")

    def should_execute(
        self,
        context: WorkflowContext,
    ) -> bool:

        if context.state.risk is None:
            return False

        return context.state.risk.level == RiskLevel.HIGH

    def execute(
        self,
        context: WorkflowContext,
    ) -> SafetyResult:

        result = SafetyResult(
            emergency=True,
            priority="HIGH",
            recommendation=(
                "The user may be experiencing a mental health crisis. "
                "Encourage them to immediately contact a trusted family member, "
                "friend, licensed mental health professional, or local emergency "
                "services if they believe they are in immediate danger. "
                "Respond with empathy and avoid judgment."
            ),
        )

        context.state.safety = result

        return result