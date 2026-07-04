import time
from abc import ABC
from abc import abstractmethod

from core.context import WorkflowContext
from models import AgentResult
from models import AgentStatus


class BaseAgent(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def execute(
        self,
        context: WorkflowContext,
    ) -> dict:
        pass

    def run(
        self,
        context: WorkflowContext,
    ) -> AgentResult:

        start = time.perf_counter()

        output = self.execute(context)

        end = time.perf_counter()

        return AgentResult(
            name=self.name,
            status=AgentStatus.SUCCESS,
            output=output,
            execution_time_ms=round((end - start) * 1000, 2),
        )