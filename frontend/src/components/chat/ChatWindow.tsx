import ChatBubble from "./ChatBubble";
import { ChatMessage } from "../../types/api";

type ChatWindowProps = {
  messages: ChatMessage[];
};

export default function ChatWindow({
  messages,
}: ChatWindowProps) {
  return (
    <div className="flex h-[450px] flex-col gap-4 overflow-y-auto rounded-xl bg-background p-4">
      {messages.length === 0 ? (
        <div className="flex h-full items-center justify-center text-slate-500">
          Start a conversation...
        </div>
      ) : (
        messages.map((msg, index) => (
          <ChatBubble
            key={index}
            role={msg.role}
            message={msg.content}
          />
        ))
      )}
    </div>
  );
}