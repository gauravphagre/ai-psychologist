"""Prompt template for the risk assessment agent."""

from .common import COMMON_PROMPT

RISK_PROMPT = (
    COMMON_PROMPT
    + """
You are a risk assessment agent.
Return a JSON object with keys: level (string), reason (string).

User message:
{message}

Detected emotion:
{emotion}
"""
)
