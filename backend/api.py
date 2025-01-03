from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.get_sentiments import get_sentiment, comment_score
from backend.get_emojis import get_emojis


class Video(BaseModel):
    id: str


class Comment(BaseModel):
    text: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
async def root(video: Video):
    sentiment = get_sentiment(video.id)
    if sentiment:
        score = round((((sentiment[0] - -1) * (10 - 1)) / (1 - -1)) + 1)
        return {
            "score": score,
            "comments": sentiment[1],
            "top_comment": {"comment": sentiment[2], "rating": sentiment[3]},
            "percentages": {
                "negative": sentiment[4][0],
                "neutral": sentiment[4][1],
                "positive": sentiment[4][2],
            },
            "emoji": get_emojis(score),
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_206_PARTIAL_CONTENT,
            detail="The video's comments are disabled or invalid video ID",
        )


@app.post("/getcomment")
async def get_comment(comment: Comment):
    return round((((comment_score(comment.text) - -1) * (10 - 1)) / (1 - -1)) + 1)
