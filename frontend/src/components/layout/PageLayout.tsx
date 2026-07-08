type Props = {
  chat: React.ReactNode;
  workflow: React.ReactNode;
  inspector: React.ReactNode;
};

export default function PageLayout({
  chat,
  workflow,
  inspector,
}: Props) {
  return (
    <main className="mx-auto flex max-w-7xl flex-col gap-6 p-6">

      {/* Top Row */}

      <div className="grid grid-cols-2 gap-6">

        <section className="rounded-xl border border-slate-800 bg-slate-900 p-4 shadow">
          <h2 className="mb-4 text-lg font-semibold text-white">
            Chat
          </h2>

          {chat}
        </section>

        <section className="rounded-xl border border-slate-800 bg-slate-900 p-4 shadow">
          <h2 className="mb-4 text-lg font-semibold text-white">
            Workflow
          </h2>

          {workflow}
        </section>

      </div>

      {/* Bottom Row */}

      <section className="rounded-xl border border-slate-800 bg-slate-900 p-4 shadow">

        <h2 className="mb-4 text-lg font-semibold text-white">
          🔍 Agent Inspector
        </h2>

        <div className="min-h-[320px]">
          {inspector}
        </div>

      </section>

    </main>
  );
}