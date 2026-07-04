import logging

from agents.base import BaseAgent
from core.context import WorkflowContext
from models import (
    AgentResult,
    AgentStatus,
    WorkflowEdge,
    WorkflowGraph,
    WorkflowNode,
)

logger = logging.getLogger(__name__)


class WorkflowEngine:
    """
    Generic workflow engine.

    Executes registered agents sequentially and
    provides workflow visualization metadata.
    """

    def __init__(self):
        self.steps: list[BaseAgent] = []

    # ---------------------------------------------------------
    # Register Step
    # ---------------------------------------------------------

    def add_step(
        self,
        agent: BaseAgent,
    ):
        self.steps.append(agent)

    # ---------------------------------------------------------
    # Execute Workflow
    # ---------------------------------------------------------

    def execute(
        self,
        context: WorkflowContext,
    ) -> list[AgentResult]:

        logger.info(
            "Workflow started with %d agents.",
            len(self.steps),
        )

        results: list[AgentResult] = []

        for agent in self.steps:

            logger.info(
                "Running %s...",
                agent.name,
            )

            result = agent.run(context)

            results.append(result)

            if result.status == AgentStatus.FAILED:

                logger.warning(
                    "%s failed. Continuing workflow.",
                    agent.name,
                )

            elif result.status == AgentStatus.SKIPPED:

                logger.info(
                    "%s skipped.",
                    agent.name,
                )

        logger.info("Workflow completed.")

        return results

    # ---------------------------------------------------------
    # Workflow Graph
    # ---------------------------------------------------------

    def get_workflow_graph(
        self,
        results: list[AgentResult],
    ) -> WorkflowGraph:
        """
        Builds a workflow graph suitable for frontend visualization.
        """

        # Map execution results by agent name
        result_map = {
            result.name: result.status
            for result in results
        }

        nodes: list[WorkflowNode] = []

        for agent in self.steps:

            label = agent.name.replace("Agent", "")

            nodes.append(
                WorkflowNode(
                    id=agent.name,
                    label=label,
                    status=result_map.get(
                        agent.name,
                        AgentStatus.SKIPPED,
                    ),
                )
            )

        # Workflow topology
        edges = [

            WorkflowEdge(
                source="EmotionAgent",
                target="RiskAgent",
            ),

            WorkflowEdge(
                source="RiskAgent",
                target="SafetyAgent",
            ),

            WorkflowEdge(
                source="RiskAgent",
                target="WellnessAgent",
            ),

            WorkflowEdge(
                source="SafetyAgent",
                target="TherapyAgent",
            ),

            WorkflowEdge(
                source="WellnessAgent",
                target="TherapyAgent",
            ),

            WorkflowEdge(
                source="TherapyAgent",
                target="ResourceAgent",
            ),

            WorkflowEdge(
                source="ResourceAgent",
                target="ResponseAgent",
            ),
        ]

        return WorkflowGraph(
            nodes=nodes,
            edges=edges,
        )