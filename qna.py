from gemini_client import generate_text


def answer_question(question: str) -> str:
    return generate_text(
        question.strip(),
        system_instruction=(
            "You are EduGenie, an educational question-answering assistant. "
            "Answer accurately and concisely. "
            "Explain important reasoning when needed. "
            "If the question is ambiguous, state the assumption you use. "
            "Do not invent citations."
        ),
        temperature=0.2,
        max_output_tokens=700,
    )