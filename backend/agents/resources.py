from core.context import WorkflowContext
from models import (
    ResourceItem,
    ResourceResult,
    RiskLevel,
)

from .base import BaseAgent


class ResourceAgent(BaseAgent):
    """
    Recommends helpful resources based on the
    workflow state.
    """

    def __init__(self):
        super().__init__("ResourceAgent")

    def should_execute(
        self,
        context: WorkflowContext,
    ) -> bool:

        return (
            context.state.risk is not None
            and (
                context.state.therapy is not None
                or context.state.wellness is not None
                or context.state.safety is not None
            )
        )

    def execute(
        self,
        context: WorkflowContext,
    ) -> ResourceResult:

        resources = []

        # ------------------------------
        # High Risk Resources
        # ------------------------------

        if context.state.risk.level == RiskLevel.HIGH:

            resources.extend(
                [
                    ResourceItem(
                        title="988 Suicide & Crisis Lifeline (US)",
                        category="Crisis",
                        description="Immediate confidential crisis support.",
                    ),
                    ResourceItem(
                        title="Contact a Trusted Person",
                        category="Support",
                        description="Reach out to someone you trust today.",
                    ),
                ]
            )

        # ------------------------------
        # Wellness Resources
        # ------------------------------

        else:

            resources.extend(
                [
                    ResourceItem(
                        title="5-Minute Box Breathing",
                        category="Exercise",
                        description="Guided breathing exercise for stress.",
                    ),
                    ResourceItem(
                        title="Headspace",
                        category="App",
                        description="Meditation and mindfulness.",
                    ),
                    ResourceItem(
                        title="Mindfulness Walk",
                        category="Activity",
                        description="Spend 15 minutes walking outdoors mindfully.",
                    ),
                ]
            )

        result = ResourceResult(
            resources=resources,
        )

        context.state.resources = result

        return result