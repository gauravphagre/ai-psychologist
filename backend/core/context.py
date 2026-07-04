from typing import Callable

from models import WorkflowState
from services.llm import LLMService
from services.memory import MemoryService


class WorkflowContext:
    """
    Shared context available to every workflow agent.

    Holds:
    - Session information
    - User input
    - Workflow state
    - Shared services
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

    # ----------------------------------------------------
    # Prompt Builder
    # ----------------------------------------------------

    def build_prompt(
        self,
        sections: list[str],
    ) -> str:
        """
        Dynamically constructs a prompt using
        registered section builders.
        """

        builders: dict[str, Callable[[], str]] = {
            "user": self._build_user,
            "history": self._build_history,
            "emotion": self._build_emotion,
            "risk": self._build_risk,
            "therapy": self._build_therapy,
        }

        prompt_sections = []

        for section in sections:

            builder = builders.get(section)

            if builder:

                text = builder()

                if text:

                    prompt_sections.append(text)

        return "\n\n".join(prompt_sections)

    # ----------------------------------------------------
    # Section Builders
    # ----------------------------------------------------

    def _build_user(self) -> str:

        return f"""User Message:
{self.user_message}"""

    def _build_history(self) -> str:

        history = self.memory_service.get_history(
            self.session_id
        )

        if not history:

            return ""

        conversation = []

        for message in history:

            ts = message.get("timestamp")
            prefix = f"[{ts}] " if ts else ""

            conversation.append(
                f"{prefix}{message['role']}: {message['content']}"
            )

        return (
            "Conversation History:\n"
            + "\n".join(conversation)
        )

    def _build_emotion(self) -> str:

        if self.state.emotion is None:

            return ""

        emotion = self.state.emotion

        return f"""Detected Emotion:
Emotion: {emotion.emotion}
Intensity: {emotion.score}/10"""

    def _build_risk(self) -> str:

        if self.state.risk is None:

            return ""

        risk = self.state.risk

        return f"""Risk Assessment:
Level: {risk.level}
Reason: {risk.reason}"""

    def _build_therapy(self) -> str:

        if self.state.therapy is None:

            return ""

        therapy = self.state.therapy

        return f"""Therapy Recommendation:
Technique: {therapy.technique}
Recommendation: {therapy.recommendation}"""