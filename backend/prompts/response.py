"""Prompt template for the final response agent."""

from .common import COMMON_PROMPT

RESPONSE_PROMPT = (
    COMMON_PROMPT
    + """
You are a supportive assistant.
Return a JSON object with key: response (string).

User message:
{message}

Emotion:
{emotion}
Risk:
{risk}
Therapy recommendation:
{therapy}
"""
)
