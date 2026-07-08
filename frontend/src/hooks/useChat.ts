import { useState } from "react";

import { sendMessage } from "../api/psychologist";
import {
  AgentResult,
  ChatMessage,
  WorkflowGraph,
} from "../types/api";

export function useChat() {
  // Keep one session for the lifetime of this chat
  const [sessionId] = useState(() => crypto.randomUUID());

  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      role: "assistant",
      content: "Hello! I'm your AI Psychologist. How are you feeling today?",
    },
  ]);

  const [loading, setLoading] = useState(false);

  const [workflow, setWorkflow] = useState<AgentResult[]>([]);

  const [workflowGraph, setWorkflowGraph] =
    useState<WorkflowGraph | null>(null);

  const [selectedAgent, setSelectedAgent] =
    useState<AgentResult | null>(null);

  async function send(message: string) {
    if (!message.trim()) return;

    // Show user message immediately
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: message,
      },
    ]);

    setLoading(true);

    try {
      const response = await sendMessage({
        session_id: sessionId,
        message,
      });

      // Add assistant response
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: response.final_response,
        },
      ]);

      // Update workflow
      setWorkflow(response.workflow);
      setWorkflowGraph(response.workflow_graph);

      // Automatically select first successful agent
      const firstSuccessfulAgent = response.workflow.find(
        (agent) => agent.status === "SUCCESS"
      );

      setSelectedAgent(
        firstSuccessfulAgent ??
          (response.workflow.length > 0
            ? response.workflow[0]
            : null)
      );
    } catch (error) {
      console.error("Chat request failed:", error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "Sorry, I couldn't reach the backend. Please check that the API is running.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return {
    messages,
    loading,
    workflow,
    workflowGraph,
    selectedAgent,
    setSelectedAgent,
    send,
  };
}