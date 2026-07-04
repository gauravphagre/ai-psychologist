import logging

from agents.emotion import EmotionAgent
from agents.response import ResponseAgent
from agents.risk import RiskAgent
from agents.therapy import TherapyAgent

from core.context import WorkflowContext
from core.workflow_engine import WorkflowEngine

from models import ChatResponse

from services.llm import LLMService
from services.memory import MemoryService

logger = logging.getLogger(__name__)


class PsychologistWorkflow:
    """
    Multi-agent psychologist workflow.

    Execution Order:

        Emotion
            ↓
        Risk
            ↓
        Therapy
            ↓
        Response
    """

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
    ) -> ChatResponse:

        logger.info(
            "Starting workflow. session=%s",
            session_id,
        )

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

        workflow_results = self.engine.execute(context)

        final_response = ""

        if context.state.response:
            final_response = context.state.response.response

        logger.info(
            "Workflow completed. session=%s",
            session_id,
        )

        return ChatResponse(
            session_id=session_id,
            workflow=workflow_results,
            final_response=final_response,
        )