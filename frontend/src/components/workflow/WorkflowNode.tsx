import { memo } from "react";
import { Handle, Position } from "reactflow";

type Props = {
  data: {
    label: string;
    status: string;
    icon: React.ReactNode;
  };
};

function colors(status: string) {
  switch (status) {
    case "SUCCESS":
      return "border-green-500 bg-green-500/10 text-green-300";

    case "FAILED":
      return "border-red-500 bg-red-500/10 text-red-300";

    case "SKIPPED":
      return "border-yellow-500 bg-yellow-500/10 text-yellow-300";

    default:
      return "border-slate-700 bg-slate-800 text-slate-400";
  }
}

function WorkflowNode({ data }: Props) {
  return (
    <>
      <Handle
        type="target"
        position={Position.Top}
      />

      <div
        className={`min-w-[150px] rounded-xl border p-3 shadow-lg transition hover:scale-105 ${colors(
          data.status
        )}`}
      >
        <div className="mb-2 flex justify-center">
          {data.icon}
        </div>

        <div className="text-center font-semibold">
          {data.label}
        </div>

        <div className="mt-2 text-center text-xs">
          {data.status}
        </div>
      </div>

      <Handle
        type="source"
        position={Position.Bottom}
      />
    </>
  );
}

export default memo(WorkflowNode);