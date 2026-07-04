"""Prompt template for the therapy recommendation agent."""

from .common import COMMON_PROMPT

THERAPY_PROMPT = (
    COMMON_PROMPT
    + """
You are a therapy technique recommendation agent.
Return a JSON object with keys: technique (string), recommendation (string).

User message:
{message}

Risk assessment:
{risk}
"""
)
