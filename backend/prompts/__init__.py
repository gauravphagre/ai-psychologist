"""Prompt templates package.

This package contains prompt strings/templates used by backend agents.
"""

from .common import COMMON_PROMPT
from .emotion import EMOTION_PROMPT
from .risk import RISK_PROMPT
from .therapy import THERAPY_PROMPT
from .response import RESPONSE_PROMPT

__all__ = [
    "COMMON_PROMPT",
    "EMOTION_PROMPT",
    "RISK_PROMPT",
    "THERAPY_PROMPT",
    "RESPONSE_PROMPT",
]
