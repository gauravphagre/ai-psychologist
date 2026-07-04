from agents.base import BaseAgent


class AgentRegistry:

    def __init__(self):
        self._agents: dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent):
        self._agents[agent.name] = agent

    def get(self, name: str):
        return self._agents[name]

    def list(self):
        return list(self._agents.values())