from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class AgentStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


class ChatRequest(BaseModel):
    session_id: str
    message: str


class EmotionResult(BaseModel):
    emotion: str
    score: int


class RiskResult(BaseModel):
    level: str
    reason: str


class TherapyResult(BaseModel):
    technique: str
    recommendation: str


class ResponseResult(BaseModel):
    response: str


class WorkflowState(BaseModel):
    emotion: EmotionResult | None = None
    risk: RiskResult | None = None
    therapy: TherapyResult | None = None
    response: ResponseResult | None = None


class AgentResult(BaseModel):
    name: str
    status: AgentStatus
    output: dict[str, Any] = Field(default_factory=dict)
    execution_time_ms: float


class ChatResponse(BaseModel):
    session_id: str
    workflow: list[AgentResult]
    final_response: str