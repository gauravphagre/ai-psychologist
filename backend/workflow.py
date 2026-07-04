import logging

from agents.emotion import EmotionAgent
from agents.response import ResponseAgent
from agents.resources import ResourceAgent
from agents.risk import RiskAgent
from agents.safety import SafetyAgent
from agents.therapy import TherapyAgent
from agents.wellness import WellnessAgent

from core.context import WorkflowContext
from core.workflow_engine import WorkflowEngine

from services.llm import LLMService
from services.memory import MemoryService

logger = logging.getLogger(__name__)


class PsychologistWorkflow:
    """
    Executes the AI Psychologist workflow.

        Emotion
            ↓
          Risk
        ↙      ↘
    Safety   Wellness
        ↘      ↙
         Therapy
            ↓
        Resources
            ↓
         Response
    """

    def __init__(self):

        self.engine = WorkflowEngine()

        self.engine.add_step(EmotionAgent())
        self.engine.add_step(RiskAgent())
        self.engine.add_step(SafetyAgent())
        self.engine.add_step(WellnessAgent())
        self.engine.add_step(TherapyAgent())
        self.engine.add_step(ResourceAgent())
        self.engine.add_step(ResponseAgent())

        self.llm = LLMService()
        self.memory = MemoryService()

    def execute(
        self,
        session_id: str,
        message: str,
    ):

        logger.info(
            "Starting workflow. session=%s",
            session_id,
        )

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

        logger.info(
            "Workflow completed. session=%s",
            session_id,
        )

        return context, results