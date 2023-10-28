from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from dotenv import load_dotenv

load_dotenv()

anthropic = Anthropic()


completion = anthropic.completions.create(
    model="claude-2",
    max_tokens_to_sample=300,
    prompt=f"{HUMAN_PROMPT} how does a court case get to the Supreme Court?{AI_PROMPT}",
)
print(completion.completion)