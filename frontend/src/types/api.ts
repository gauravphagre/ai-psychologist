export type AgentStatus =
  | "SUCCESS"
  | "FAILED"
  | "SKIPPED";

export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

export interface AgentResult {
  name: string;
  status: AgentStatus;
  output: Record<string, any>;
  execution_time_ms: number;
  error: string | null;
}

export interface WorkflowNode {
  id: string;
  label: string;
  status: AgentStatus;
}

export interface WorkflowEdge {
  source: string;
  target: string;
}

export interface WorkflowGraph {
  nodes: WorkflowNode[];
  edges: WorkflowEdge[];
}

export interface ChatRequest {
  session_id: string;
  message: string;
}

export interface ChatResponse {
  session_id: string;
  workflow: AgentResult[];
  workflow_graph: WorkflowGraph;
  final_response: string;
}