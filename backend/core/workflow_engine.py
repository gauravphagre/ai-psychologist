from core.context import WorkflowContext
from models import AgentResult


class WorkflowEngine:

    def __init__(self):
        self.steps = []

    def add_step(self, agent):
        self.steps.append(agent)

    def execute(
        self,
        context: WorkflowContext,
    ) -> list[AgentResult]:

        results = []

        for step in self.steps:
            result = step.run(context)
            results.append(result)

        return results