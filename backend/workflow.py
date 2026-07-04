from agents.emotion import EmotionAgent
from agents.response import ResponseAgent
from agents.risk import RiskAgent
from agents.therapy import TherapyAgent

from core.context import WorkflowContext
from core.workflow_engine import WorkflowEngine

from services.llm import LLMService
from services.memory import MemoryService


class PsychologistWorkflow:

    def __init__(self):

        self.engine = WorkflowEngine()

        self.engine.add_step(EmotionAgent())
        self.engine.add_step(RiskAgent())
        self.engine.add_step(TherapyAgent())
        self.engine.add_step(ResponseAgent())

        self.llm = LLMService()
        self.memory = MemoryService()

    def execute(
        self,
        session_id: str,
        message: str,
    ):

        # Store current user message
        self.memory.add_message(
            session_id=session_id,
            role="user",
            content=message,
        )

        context = WorkflowContext(
            session_id=session_id,
            user_message=message,
            llm_service=self.llm,
            memory_service=self.memory,
        )

        results = self.engine.execute(context)

        return context, results