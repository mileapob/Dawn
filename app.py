import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from openai import OpenAI
from typing import List

BASE_DIR = Path(__file__).parent
SYSTEM_PROMPT = (BASE_DIR / "system_prompt_stage1.md").read_text(encoding="utf-8")

# ── 替换这两行 ──────────────────────────────────────────
ARK_API_KEY = os.getenv("ARK_API_KEY", "替换成你的API_KEY")
ARK_MODEL   = os.getenv("ARK_MODEL",   "替换成你的推理接入点ID")   # 形如 ep-xxxxxxxx-xxxxx
# ────────────────────────────────────────────────────────

client = OpenAI(
    api_key=ARK_API_KEY,
    base_url="https://ark.volcengine.com/api/v3",
)

app = FastAPI()

STAGE1_DONE = "恭喜你顺利走完破晓第一程"


class Message(BaseModel):
    role: str       # "user" | "assistant"
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.get("/", response_class=HTMLResponse)
def index():
    return (BASE_DIR / "demo.html").read_text(encoding="utf-8")


@app.post("/chat")
def chat(req: ChatRequest):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages += [{"role": m.role, "content": m.content} for m in req.messages]

    resp = client.chat.completions.create(
        model=ARK_MODEL,
        messages=messages,
    )

    reply = resp.choices[0].message.content
    return {
        "reply": reply,
        "stage_complete": STAGE1_DONE in reply,
    }
