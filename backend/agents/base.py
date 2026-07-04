import logging
import time
from abc import ABC
from abc import abstractmethod

from core.context import WorkflowContext
from models import AgentResult
from models import AgentStatus

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """
    Base class for all workflow agents.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def execute(
        self,
        context: WorkflowContext,
    ) -> dict:
        """
        Execute the agent's business logic.
        """
        raise NotImplementedError

    def run(
        self,
        context: WorkflowContext,
    ) -> AgentResult:
        """
        Executes the agent safely.

        Any exception is converted into a FAILED AgentResult so the
        workflow can continue and report which step failed.
        """

        start = time.perf_counter()

        try:
            output = self.execute(context)

            status = AgentStatus.SUCCESS
            error = None

        except Exception as ex:
            logger.exception("%s failed.", self.name)

            output = {}

            status = AgentStatus.FAILED

            error = str(ex)

        end = time.perf_counter()

        return AgentResult(
            name=self.name,
            status=status,
            output=output,
            execution_time_ms=round((end - start) * 1000, 2),
            error=error,
        )