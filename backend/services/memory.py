from collections import defaultdict
from datetime import datetime, timezone


class MemoryService:
    """
    Simple in-memory conversation store.

    Can later be replaced by:
        - Redis
        - PostgreSQL
        - Vector Database
    without changing the agent code.
    """

    def __init__(self):
        self.sessions = defaultdict(list)

    # ---------------------------------------------------------
    # Store Message
    # ---------------------------------------------------------

    def add_message(
        self,
        session_id: str,
        role: str,
        content: str,
    ):

        timestamp = (
            datetime.now(timezone.utc)
            .replace(microsecond=0)
            .isoformat()
            .replace("+00:00", "Z")
        )

        self.sessions[session_id].append(
            {
                "role": role,
                "content": content,
                "timestamp": timestamp,
            }
        )

    # ---------------------------------------------------------
    # Get Messages
    # ---------------------------------------------------------

    def get_messages(
        self,
        session_id: str,
    ):
        """
        Returns the full conversation.

        This is the primary API used by WorkflowContext.
        """

        return self.sessions.get(session_id, [])

    # ---------------------------------------------------------
    # Backward Compatibility
    # ---------------------------------------------------------

    def get_history(
        self,
        session_id: str,
    ):
        """
        Alias kept for backward compatibility.
        """

        return self.get_messages(session_id)

    # ---------------------------------------------------------
    # Clear Conversation
    # ---------------------------------------------------------

    def clear(
        self,
        session_id: str,
    ):
        self.sessions.pop(session_id, None)