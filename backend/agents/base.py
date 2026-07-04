import logging
import time
from abc import ABC, abstractmethod
from typing import Any

from core.context import WorkflowContext
from models import AgentResult, AgentStatus

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """
    Base class for all workflow agents.
    """

    def __init__(self, name: str):
        self.name = name

    # ---------------------------------------------------------
    # Conditional execution
    # ---------------------------------------------------------

    def should_execute(
        self,
        context: WorkflowContext,
    ) -> bool:
        return True

    # ---------------------------------------------------------
    # Serialize Output
    # ---------------------------------------------------------

    def _serialize_output(
        self,
        output: Any,
    ) -> dict:

        if output is None:
            return {}

        # Pydantic v2
        if hasattr(output, "model_dump"):
            return output.model_dump()

        # Pydantic v1
        if hasattr(output, "dict"):
            return output.dict()

        if isinstance(output, dict):
            return output

        if isinstance(output, list):
            return {"items": output}

        return {
            "value": str(output),
        }

    # ---------------------------------------------------------
    # Execute Wrapper
    # ---------------------------------------------------------

    def run(
        self,
        context: WorkflowContext,
    ) -> AgentResult:

        if not self.should_execute(context):

            logger.info("%s skipped.", self.name)

            return AgentResult(
                name=self.name,
                status=AgentStatus.SKIPPED,
                output={},
                execution_time_ms=0,
                error=None,
            )

        logger.info("%s started.", self.name)

        start = time.perf_counter()

        try:

            output = self.execute(context)

            execution_time = round(
                (time.perf_counter() - start) * 1000,
                2,
            )

            logger.info(
                "%s completed in %.2f ms.",
                self.name,
                execution_time,
            )

            return AgentResult(
                name=self.name,
                status=AgentStatus.SUCCESS,
                output=self._serialize_output(output),
                execution_time_ms=execution_time,
                error=None,
            )

        except Exception as ex:

            execution_time = round(
                (time.perf_counter() - start) * 1000,
                2,
            )

            logger.exception("%s failed.", self.name)

            return AgentResult(
                name=self.name,
                status=AgentStatus.FAILED,
                output={},
                execution_time_ms=execution_time,
                error=str(ex),
            )

    # ---------------------------------------------------------
    # Agent Implementation
    # ---------------------------------------------------------

    @abstractmethod
    def execute(
        self,
        context: WorkflowContext,
    ):
        pass