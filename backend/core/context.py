from models import WorkflowState
from services.llm import LLMService
from services.memory import MemoryService


class WorkflowContext:
    """
    Shared context passed to every agent.

    Contains:
    - User message
    - Conversation memory
    - Shared workflow state
    - LLM service
    """

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

    # ---------------------------------------------------------
    # Conversation History
    # ---------------------------------------------------------

    @property
    def history(self) -> str:
        """
        Returns the conversation history as text.
        """

        messages = self.memory_service.get_messages(
            self.session_id
        )

        if not messages:
            return ""

        lines = []

        for message in messages:
            role = message["role"].capitalize()
            content = message["content"]

            lines.append(f"{role}: {content}")

        return "\n".join(lines)

    # ---------------------------------------------------------
    # Prompt Builder
    # ---------------------------------------------------------

    def build_prompt(
        self,
        sections: list[str],
    ) -> str:
        """
        Dynamically build an LLM prompt using the requested sections.
        """

        prompt = []

        if "history" in sections and self.history:
            prompt.append(
                "Conversation History:\n"
                f"{self.history}"
            )

        if "user" in sections:
            prompt.append(
                "User Message:\n"
                f"{self.user_message}"
            )

        if (
            "emotion" in sections
            and self.state.emotion
        ):
            prompt.append(
                "Emotion Analysis:\n"
                f"{self.state.emotion.model_dump_json(indent=2)}"
            )

        if (
            "risk" in sections
            and self.state.risk
        ):
            prompt.append(
                "Risk Assessment:\n"
                f"{self.state.risk.model_dump_json(indent=2)}"
            )

        if (
            "wellness" in sections
            and self.state.wellness
        ):
            prompt.append(
                "Wellness Recommendation:\n"
                f"{self.state.wellness.model_dump_json(indent=2)}"
            )

        if (
            "safety" in sections
            and self.state.safety
        ):
            prompt.append(
                "Safety Recommendation:\n"
                f"{self.state.safety.model_dump_json(indent=2)}"
            )

        if (
            "therapy" in sections
            and self.state.therapy
        ):
            prompt.append(
                "Therapy Recommendation:\n"
                f"{self.state.therapy.model_dump_json(indent=2)}"
            )

        if (
            "resources" in sections
            and self.state.resources
        ):
            prompt.append(
                "Helpful Resources:\n"
                f"{self.state.resources.model_dump_json(indent=2)}"
            )

        return "\n\n".join(prompt)