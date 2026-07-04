from agents.base import BaseAgent


class AgentRegistry:
    """
    Registry of available workflow agents.

    This registry is not currently used by the POC workflow,
    but it will support dynamic workflow definitions in future.
    """

    def __init__(self):
        self._agents: dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        self._agents[agent.name] = agent

    def get(self, name: str) -> BaseAgent:
        return self._agents[name]

    def list(self) -> list[BaseAgent]:
        return list(self._agents.values())