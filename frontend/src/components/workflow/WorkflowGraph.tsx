import {
  useMemo,
  useCallback,
} from "react";

import ReactFlow, {
  Background,
  Controls,
  MarkerType,
} from "reactflow";

import "reactflow/dist/style.css";

import {
  AlertTriangle,
  BookOpen,
  Brain,
  Heart,
  MessageCircle,
  ShieldAlert,
  Sparkles,
} from "lucide-react";

import WorkflowNode from "./WorkflowNode";

import {
  AgentResult,
  WorkflowGraph as Graph,
} from "../../types/api";

type Props = {
  graph: Graph | null;
  workflow: AgentResult[];
  onNodeClick: (agent: AgentResult) => void;
};

const nodeTypes = {
  workflow: WorkflowNode,
};

export default function WorkflowGraph({
  graph,
  workflow,
  onNodeClick,
}: Props) {

  if (!graph) {
    return (
      <div className="flex h-full items-center justify-center text-slate-500">
        Run a conversation first.
      </div>
    );
  }

  const statusMap = Object.fromEntries(
    graph.nodes.map((n) => [
      n.id,
      n.status,
    ])
  );

  const icons: Record<string, React.ReactNode> = {
    EmotionAgent: <Brain size={22} />,
    RiskAgent: <AlertTriangle size={22} />,
    SafetyAgent: <ShieldAlert size={22} />,
    WellnessAgent: <Heart size={22} />,
    TherapyAgent: <Sparkles size={22} />,
    ResourceAgent: <BookOpen size={22} />,
    ResponseAgent: <MessageCircle size={22} />,
  };

  const positions = {
    EmotionAgent: { x: 180, y: 0 },

    RiskAgent: { x: 180, y: 120 },

    SafetyAgent: { x: 20, y: 260 },

    WellnessAgent: { x: 340, y: 260 },

    TherapyAgent: { x: 180, y: 430 },

    ResourceAgent: { x: 180, y: 580 },

    ResponseAgent: { x: 180, y: 730 },
  };

  const nodes = useMemo(() => {
    return graph.nodes.map((node) => ({
      id: node.id,

      type: "workflow",

      position:
        positions[
          node.id as keyof typeof positions
        ],

      data: {
        label: node.label,
        status: node.status,
        icon: icons[node.id],
      },
    }));
  }, [graph]);

  const edges = useMemo(() => {
    return graph.edges.map((edge, index) => ({
      id: `${index}`,

      source: edge.source,

      target: edge.target,

      animated: true,

      markerEnd: {
        type: MarkerType.ArrowClosed,
      },
    }));
  }, [graph]);

  const onNodeClickInternal = useCallback(
    (_: any, node: any) => {
      const agent = workflow.find(
        (a) => a.name === node.id
      );

      if (agent) {
        onNodeClick(agent);
      }
    },
    [workflow]
  );

  return (
    <div className="h-full rounded-xl border border-slate-800 bg-slate-950">

      <ReactFlow
        fitView
        nodes={nodes}
        edges={edges}
        nodeTypes={nodeTypes}
        nodesDraggable={false}
        nodesConnectable={false}
        elementsSelectable={true}
        onNodeClick={onNodeClickInternal}
      >

        <Background />

        <Controls showInteractive={false} />

      </ReactFlow>

    </div>
  );
}