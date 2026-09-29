from functools import lru_cache

from config import settings
from gemini_client import generate_text


@lru_cache(maxsize=1)
def _local_pipeline():
    from transformers import pipeline

    return pipeline(
        "text2text-generation",
        model=settings.local_explainer_model,
        device=-1,
    )


def _local_explain(topic: str, level: str) -> str:
    prompt = (
        f"Explain {topic} to a {level} learner in simple language. "
        "Use a short definition, key points, and one simple example."
    )

    result = _local_pipeline()(
        prompt,
        max_new_tokens=220,
        do_sample=False,
    )

    return result[0]["generated_text"].strip()


def explain_topic(topic: str, level: str = "beginner") -> str:
    if settings.enable_local_explainer:
        try:
            return _local_explain(topic, level)
        except Exception:
            pass

    return generate_text(
        f"Explain the topic '{topic}' for a {level} learner.",
        system_instruction=(
            "You are EduGenie, a patient educational tutor. "
            "Use simple language, short sections, bullet points where useful, "
            "and one clear example. Do not assume advanced background knowledge."
        ),
        temperature=0.2,
        max_output_tokens=600,
    )