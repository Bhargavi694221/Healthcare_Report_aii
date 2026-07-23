from utils.helpers import get_llm

llm = get_llm()

response = llm.call(
    "Say hello in one sentence."
)

print(response)