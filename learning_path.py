from gemini_client import generate_structured
from models import LearningPathResponse


def get_learning_recommendations(
    topic: str,
    level: str = "beginner",
    weeks: int = 4
) -> dict:

    prompt = f"""
Create a {weeks}-week learning path
for "{topic}" at the {level} level.

For each week provide:
- a short title
- learning goals
- topics ordered from foundational to more advanced
- practical exercises
- useful resource types or search suggestions

Make the plan realistic for a student and include gradual progression.
Do not invent exact URLs.
Return only the requested structured object.
""".strip()

    result = generate_structured(
        prompt,
        LearningPathResponse,
        system_instruction=(
            "You are EduGenie, a learning-plan designer. "
            "Make plans structured, practical, progressive, and student-friendly."
        ),
        temperature=0.3,
        max_output_tokens=2200,
    )

    return result.model_dump()