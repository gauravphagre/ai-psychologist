import { AgentResult } from "../../types/api";

type Props = {
  agent: AgentResult | null;
};

function statusColor(status: string) {
  switch (status) {
    case "SUCCESS":
      return "bg-green-500/20 text-green-300 border-green-500";

    case "FAILED":
      return "bg-red-500/20 text-red-300 border-red-500";

    case "SKIPPED":
      return "bg-yellow-500/20 text-yellow-300 border-yellow-500";

    default:
      return "bg-slate-700 text-slate-300 border-slate-600";
  }
}

export default function AgentInspector({
  agent,
}: Props) {
  if (!agent) {
    return (
      <div className="flex h-full items-center justify-center text-slate-500">
        Select an agent from the workflow.
      </div>
    );
  }

  return (
    <div className="flex h-full flex-col text-slate-100">

      {/* Agent Name */}
      <h2 className="mb-5 text-xl font-bold">
        {agent.name}
      </h2>

      {/* Status */}
      <div className="mb-4">
        <p className="mb-2 text-sm text-slate-400">
          Status
        </p>

        <span
          className={`rounded-full border px-3 py-1 text-sm font-semibold ${statusColor(
            agent.status
          )}`}
        >
          {agent.status}
        </span>
      </div>

      {/* Execution Time */}
      <div className="mb-5">
        <p className="text-sm text-slate-400">
          Execution Time
        </p>

        <p className="mt-1 font-medium">
          {agent.execution_time_ms.toFixed(2)} ms
        </p>
      </div>

      {/* Error */}
      {agent.error && (
        <div className="mb-5 rounded-lg border border-red-500 bg-red-500/20 p-3 text-red-300">
          {agent.error}
        </div>
      )}

      {/* Output */}
      <div className="flex flex-1 flex-col">

        <h3 className="mb-3 font-semibold">
          Agent Output
        </h3>

        <pre className="flex-1 overflow-auto rounded-xl border border-slate-700 bg-slate-950 p-4 text-xs text-green-300">
{JSON.stringify(agent.output, null, 2)}
        </pre>

      </div>

    </div>
  );
}