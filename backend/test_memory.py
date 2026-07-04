from services.memory import memory_service

memory_service.add_message(
    "1",
    "user",
    "Hello"
)

memory_service.add_message(
    "1",
    "assistant",
    "Hi!"
)

print(memory_service.get_history("1"))