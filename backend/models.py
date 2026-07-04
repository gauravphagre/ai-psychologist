from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


# ==========================================================
# Enums
# ==========================================================

class AgentStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


# ==========================================================
# Request Model
# ==========================================================

class ChatRequest(BaseModel):
    session_id: str
    message: str


# ==========================================================
# Agent Output Models
# ==========================================================

class EmotionResult(BaseModel):
    emotion: str
    score: int


class RiskResult(BaseModel):
    level: RiskLevel
    reason: str


class WellnessResult(BaseModel):
    activity: str
    duration: str
    instructions: str


class SafetyResult(BaseModel):
    emergency: bool
    priority: str
    recommendation: str


class TherapyResult(BaseModel):
    technique: str
    recommendation: str


class ResourceItem(BaseModel):
    title: str
    category: str
    description: str


class ResourceResult(BaseModel):
    resources: list[ResourceItem]


class ResponseResult(BaseModel):
    response: str


# ==========================================================
# Workflow State
# ==========================================================

class WorkflowState(BaseModel):
    emotion: EmotionResult | None = None
    risk: RiskResult | None = None
    wellness: WellnessResult | None = None
    safety: SafetyResult | None = None
    therapy: TherapyResult | None = None
    resources: ResourceResult | None = None
    response: ResponseResult | None = None


# ==========================================================
# Agent Execution Result
# ==========================================================

class AgentResult(BaseModel):
    name: str
    status: AgentStatus
    output: Any = Field(default_factory=dict)
    execution_time_ms: float
    error: str | None = None


# ==========================================================
# Workflow Graph
# ==========================================================

class WorkflowNode(BaseModel):
    id: str
    label: str
    status: AgentStatus


class WorkflowEdge(BaseModel):
    source: str
    target: str


class WorkflowGraph(BaseModel):
    nodes: list[WorkflowNode]
    edges: list[WorkflowEdge]


# ==========================================================
# API Response
# ==========================================================

class ChatResponse(BaseModel):
    session_id: str
    workflow: list[AgentResult]
    workflow_graph: WorkflowGraph
    final_response: str