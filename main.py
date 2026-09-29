from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from models import (
    ExplainRequest,
    QARequest,
    QuizRequest,
    SummaryRequest,
    LearningPathRequest,
)

from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0",
)


app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static",
)


@app.get("/", response_class=HTMLResponse)
async def home():
    html_file = BASE_DIR / "templates" / "index.html"

    if not html_file.exists():
        return HTMLResponse(
            "<h1>EduGenie</h1><p>index.html file not found.</p>",
            status_code=500,
        )

    return HTMLResponse(
        content=html_file.read_text(encoding="utf-8")
    )


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "EduGenie"
    }


@app.post("/qa")
async def qa(payload: QARequest):
    try:
        answer = answer_question(payload.question)
        return {"answer": answer}
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=str(exc)
        )


@app.post("/explain")
async def explain(payload: ExplainRequest):
    try:
        explanation = explain_topic(
            payload.topic,
            payload.level
        )
        return {"explanation": explanation}
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=str(exc)
        )


@app.post("/quiz")
async def quiz(payload: QuizRequest):
    try:
        return generate_quiz(
            payload.text,
            payload.count
        )
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=str(exc)
        )


@app.post("/summarize")
async def summarize(payload: SummaryRequest):
    try:
        summary = summarize_text(
            payload.text,
            payload.max_words
        )
        return {"summary": summary}
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=str(exc)
        )


@app.post("/learn/recommendations")
async def learning_recommendations(
    payload: LearningPathRequest
):
    try:
        return get_learning_recommendations(
            topic=payload.topic,
            level=payload.level,
            weeks=payload.weeks,
        )
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=str(exc)
        )