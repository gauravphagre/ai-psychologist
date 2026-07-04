from models import WorkflowState
from services.llm import LLMService
from services.memory import MemoryService


class WorkflowContext:

    def __init__(
        self,
        session_id: str,
        user_message: str,
        llm_service: LLMService,
        memory_service: MemoryService,
    ):
        self.session_id = session_id
        self.user_message = user_message

        self.llm_service = llm_service
        self.memory_service = memory_service

        self.state = WorkflowState()