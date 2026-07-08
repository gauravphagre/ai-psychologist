import { Send } from "lucide-react";
import { useState } from "react";

type ChatInputProps = {
  onSend: (message: string) => void;
  disabled?: boolean;
};

export default function ChatInput({
  onSend,
  disabled = false,
}: ChatInputProps) {
  const [message, setMessage] = useState("");

  const handleSend = () => {
    const text = message.trim();

    if (!text) return;

    onSend(text);
    setMessage("");
  };

  return (
    <div className="flex gap-3">
      <input
        className="flex-1 rounded-xl border border-slate-700 bg-card px-4 py-3 text-white outline-none focus:border-primary"
        placeholder="How are you feeling today?"
        value={message}
        disabled={disabled}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            handleSend();
          }
        }}
      />

      <button
        onClick={handleSend}
        disabled={disabled}
        className="rounded-xl bg-primary px-5 text-white transition hover:opacity-90 disabled:opacity-50"
      >
        <Send size={18} />
      </button>
    </div>
  );
}