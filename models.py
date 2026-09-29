from typing import Literal

from pydantic import BaseModel, Field, field_validator


class TextRequest(BaseModel):
    text: str = Field(min_length=1)

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Text cannot be empty.")
        return value


class QARequest(BaseModel):
    question: str = Field(min_length=2, max_length=10000)


class ExplainRequest(BaseModel):
    topic: str = Field(min_length=2, max_length=5000)
    level: Literal["beginner", "intermediate", "advanced"] = "beginner"


class QuizRequest(TextRequest):
    count: int = Field(default=3, ge=1, le=10)


class SummaryRequest(TextRequest):
    max_words: int = Field(default=150, ge=30, le=500)


class LearningPathRequest(BaseModel):
    topic: str = Field(min_length=2, max_length=5000)
    level: Literal["beginner", "intermediate", "advanced"] = "beginner"
    weeks: int = Field(default=4, ge=1, le=12)


class QuizQuestion(BaseModel):
    question: str
    options: list[str] = Field(min_length=4, max_length=4)
    correct_answer: str
    explanation: str


class QuizResponse(BaseModel):
    questions: list[QuizQuestion]


class LearningStep(BaseModel):
    week: int
    title: str
    goals: list[str]
    topics: list[str]
    practice: list[str]
    resources: list[str]


class LearningPathResponse(BaseModel):
    topic: str
    level: str
    duration_weeks: int
    steps: list[LearningStep]