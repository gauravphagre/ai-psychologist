from agents.base import BaseAgent
from core.context import WorkflowContext
from core.workflow_engine import WorkflowEngine


class DummyAgent(BaseAgent):
    def __init__(self):
        super().__init__("DummyAgent")

    def execute(self, context):
        return {
            "message": "Workflow Engine Works!"
        }


engine = WorkflowEngine()

engine.add_step(DummyAgent())

context = WorkflowContext(
    session_id="123",
    user_message="Hello"
)

results = engine.execute(context)

print(results)