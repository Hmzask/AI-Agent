from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from I_defined_tools import tools

# AI Model.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# AGENT
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="Your name is HamSum2026."
)

# Output Formatting.
def extract_text(message):
    content = message.content

    # Gemini block format
    if isinstance(content, list):
        return "".join(block.get("text", "") for block in content)

    # Plain text
    if isinstance(content, str):
        return content

    return str(content)

# ---------------- LOOP ---------------- #

while True:
    user_prompt = input("Prompt:-> ")

    if user_prompt.lower() == "exit":
        print("Goodbye 👋")
        break

    result = agent.invoke({
        "messages": [
            {"role": "user", "content": user_prompt}
        ]
    })

    ai_msg = result["messages"][-1]
    print(extract_text(ai_msg))
