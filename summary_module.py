from gemini_client import generate_text


def summarize_text(text: str, max_words: int = 150) -> str:
    prompt = f"""
Summarize the following educational text
in no more than {max_words} words.

TEXT:
{text}
""".strip()

    return generate_text(
        prompt,
        system_instruction=(
            "You are EduGenie. Produce a faithful, easy-to-revise "
            "educational summary. Preserve important facts, definitions, "
            "relationships, and conclusions. Remove repetition and unnecessary wording."
        ),
        temperature=0.2,
        max_output_tokens=900,
    )