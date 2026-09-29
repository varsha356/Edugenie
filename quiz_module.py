from config import settings
from gemini_client import generate_structured
from models import QuizResponse


def generate_quiz(text: str, count: int = 3) -> dict:
    prompt = f"""
Create exactly {count} multiple-choice questions
from the educational text below.

Rules:
- Each question must have exactly four distinct options.
- The correct_answer must exactly match one option.
- Include a short explanation for why the answer is correct.
- Questions must be answerable from the supplied text.
- Avoid trick questions.
- Return only the requested structured object.

TEXT:
{text[:settings.max_input_chars]}
""".strip()

    quiz = generate_structured(
        prompt,
        QuizResponse,
        system_instruction=(
            "You are EduGenie's quiz generator. "
            "Create clear educational MCQs appropriate for the supplied material."
        ),
        temperature=0.3,
        max_output_tokens=1800,
    )

    return quiz.model_dump()