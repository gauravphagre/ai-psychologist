type ChatBubbleProps = {
  role: "user" | "assistant";
  message: string;
};

export default function ChatBubble({
  role,
  message,
}: ChatBubbleProps) {
  const isUser = role === "user";

  return (
    <div
      className={`flex ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <div
        className={`max-w-[80%] rounded-2xl px-4 py-3 shadow-md ${
          isUser
            ? "bg-primary text-white"
            : "bg-card text-slate-100"
        }`}
      >
        <p className="whitespace-pre-wrap leading-relaxed">
          {message}
        </p>
      </div>
    </div>
  );
}