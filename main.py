from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

from dotenv import load_dotenv
import easyocr
reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
result = reader.readtext('marked.pdf')
load_dotenv()

anthropic = Anthropic()


completion = anthropic.completions.create(
    model="claude-2",
    max_tokens_to_sample=300,
    prompt=f"{HUMAN_PROMPT} how does a court case get to the Supreme Court?{AI_PROMPT}",
)
print(completion.completion)