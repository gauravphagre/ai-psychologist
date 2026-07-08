export default function Header() {
  return (
    <header className="border-b border-slate-800 bg-slate-900 shadow-md">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">

        <div>
          <h1 className="text-2xl font-bold text-white">
            🧠 AI Psychologist
          </h1>

          <p className="text-sm text-slate-400">
            Multi-Agent Mental Health Assistant
          </p>
        </div>

        <div className="flex items-center gap-2 rounded-full border border-green-700 bg-green-900/40 px-4 py-2">
          <span className="h-2.5 w-2.5 rounded-full bg-green-500" />

          <span className="text-sm font-medium text-green-300">
            Backend Connected
          </span>
        </div>

      </div>
    </header>
  );
}