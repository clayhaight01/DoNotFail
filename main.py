from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from dotenv import load_dotenv
from ocr import OCR
from pdf2png import pdf2png
from readPDF import readPDF

load_dotenv()
anthropic = Anthropic()

assignment_txt = readPDF("assignment.pdf")
submitted_txt = readPDF("submitted.pdf")
pdf2png("marked.pdf", "marked_png")
marked_txt = OCR("marked_png")
print("assignment")
print(assignment_txt[:1000])
print("submitted")
print(submitted_txt[:1000])
print("submitted")
print(marked_txt)
print(type(marked_txt))

# completion = anthropic.completions.create(
#     model="claude-2",
#     max_tokens_to_sample=300,
#     prompt=f"{HUMAN_PROMPT} how does a court case get to the Supreme Court?{AI_PROMPT}",
# )
# print(completion.completion)