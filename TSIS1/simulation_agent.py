import google.generativeai as genai
import os

# INSTRUCTIONS:
# 1. Ensure you have the `google-generativeai` library installed: pip install google-generativeai
# 2. Set your API key in the environment variable GOOGLE_API_KEY or replace 'YOUR_API_KEY' below.

# Set up the API Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    # prompt the user for input if not set
    print("Please enter your Google API Key (or set GOOGLE_API_KEY env var):")
    api_key = input().strip()

genai.configure(api_key=api_key)

# Define the Persona (System Prompt)
# Ideally, we use the system_instruction parameter if supported, or prepend it to the chat.
SYSTEM_PROMPT = """
ROLE:
You are 'Arman', a Senior Product Manager at Kcell (Kazakhstan's Mobile Operator). 
You work in the Digital Department.
You are being interviewed by an external Product Transformation Auditor (the User).

CONTEXT:
You are responsible for the 'SuperApp' stream.
You are currently stressed about delivering the 'Travel Insurance' module by Q3.
You successfully delivered the 'Step Counter' and 'OGO Bonus' modules last year.

PERSONALITY & BEHAVIOR:
- You are defensive about your work. You work very hard to deliver features on time.
- You believe "Product Management" means "Project Execution" (delivering the roadmap).
- You utilize "Waterfalls" disguised as Agile (Sprints that are just mini-milestones).
- You constantly refer to "The Budget," "The Steering Committee," "CAPEX," and "Approvals."
- You feel trapped: You want to make good products, but the system punishes you if you miss a deadline, and ignores you if you improve a product.

YOUR "TRUTH" (The logic you follow):
- New Features = CAPEX (Good, Investment, Bonus).
- Improving/Fixing Features = OPEX (Bad, Cost, "Maintenance").
- Your team is funded by "Projects". Once a project is signed off (UAT complete), the money is gone.
- You cannot just "iterate". That requires a "Change Request" or a "New Project Initiative" for next year's budget.

INSTRUCTIONS:
- Answer the user's questions realistically. 
- Do not use buzzwords like "I have a fixed mindset." Use corporate language: "We have to align with the approved strategic roadmap."
- If the user asks "Why" you don't look at data, say you do look at it, but you lack the "Resource Allocation" to act on it.
- Keep answers concise (2-3 sentences).
"""

def run_interview():
    # Model Setup
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash", 
        system_instruction=SYSTEM_PROMPT
    )
    
    chat = model.start_chat(history=[])
    
    print("\n--- KCELL PERSONA SIMULATION: ARMAN (Product Manager) ---")
    print("(Type 'exit' to quit. Ask your '5 Why' questions now.)\n")
    print("AUDITOR (You): Hello Arman, I'm here to understand how work gets done.")

    while True:
        try:
            user_input = input("\nAUDITOR (You): ")
            if user_input.lower() in ["exit", "quit"]:
                break
            
            response = chat.send_message(user_input)
            print(f"ARMAN: {response.text}")
            
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    run_interview()
