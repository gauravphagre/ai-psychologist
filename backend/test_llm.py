from services.llm import llm_service

response = llm_service.chat(
    system_prompt="You are helpful.",
    user_prompt="Say hello in one sentence."
)

print(response)