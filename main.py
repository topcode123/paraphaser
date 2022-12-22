from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from bs4 import BeautifulSoup

from apis.paraphase_api import get_paraphase
from models.paragraph import Paragraph

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/paraphase-vi")
async def paraphase(paragraph_body: Paragraph):
    new_paragraph_response = get_paraphase(paragraph_body.paragraph)

    new_raw_paragraph = new_paragraph_response["result"]["paraphrase"]
    soup = BeautifulSoup(new_raw_paragraph, features="html.parser")
    return {"data": soup.get_text()}


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="0.0.0.0", port=6789, reload=False, forwarded_allow_ips="*"
    )
