"""Prompt template for the emotion detection agent."""

from .common import COMMON_PROMPT

EMOTION_PROMPT = (
    COMMON_PROMPT
    + """
You are an emotion detection agent.
Return a JSON object with keys: emotion (string), score (integer 0-100).

User message:
{message}
"""
)
