import ChatInput from "../components/chat/ChatInput";
import ChatWindow from "../components/chat/ChatWindow";
import Header from "../components/layout/Header";
import PageLayout from "../components/layout/PageLayout";
import AgentInspector from "../components/inspector/AgentInspector";
import WorkflowGraph from "../components/workflow/WorkflowGraph";
import { useChat } from "../hooks/useChat";

export default function Home() {
  const {
    messages,
    loading,
    workflow,
    workflowGraph,
    selectedAgent,
    setSelectedAgent,
    send,
  } = useChat();

  return (
    <>
      <Header />

      <PageLayout
        chat={
          <div className="flex h-[520px] flex-col gap-4">
            <ChatWindow messages={messages} />

            <ChatInput
              onSend={send}
              disabled={loading}
            />
          </div>
        }
        workflow={
          <div className="h-[520px]">
            <WorkflowGraph
              graph={workflowGraph}
              workflow={workflow}
              onNodeClick={setSelectedAgent}
            />
          </div>
        }
        inspector={
          <AgentInspector agent={selectedAgent} />
        }
      />
    </>
  );
}