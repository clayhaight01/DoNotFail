from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from dotenv import load_dotenv
from ocr import OCR
from pdf2png import pdf2png
from readPDF import readPDF

load_dotenv()
anthropic = Anthropic()

def main():
    assignment_txt = readPDF("assignment.pdf")
    submitted_txt = readPDF("submitted.pdf")
    # pdf2png("marked.pdf", "marked_png")
    # marked_txt = OCR("marked_png") # replace with GPT4V

    preprompt = HUMAN_PROMPT + "You are in a play where a student at a university gets unfairly marked - it appears that the professor has a vendetta against the student. You are playing the role of the students tutor who has been hired to help negotiate with the TA of the course, you have years of experience. I will play the role of the student in university, I have just submitted an assignment. I have received the marked assignment back from my TA and as expected it is marked very harshly and unfairly. I will give you the assignment, what I submitted, and what I received back. Please help me negotiate with my TA to get a better grade." + AI_PROMPT
    
    content = f"Assignment:\n{assignment_txt}\n\nSubmitted:\n{submitted_txt}\n\nMarked:\n{marked_txt}\n\n"

    plan_prompt = HUMAN_PROMPT + preprompt + "First:\nPlease start by reading the assignment, what I submitted, and what I received back. Then, make a plan for where there might be potential to get marks back. This includes things like where I followed the assignment, but got marks off anyway." + AI_PROMPT

    completion = anthropic.completions.create(model="claude-2", max_tokens_to_sample=100000, prompt=preprompt)
    print("preprompt:")
    print(completion.completion)
    plan = anthropic.completions.create(model="claude-2", max_tokens_to_sample=100000, prompt=completion.completion + plan_prompt)
    print("plan:")
    print(plan.completion)

if __name__ == "__main__":
    main()