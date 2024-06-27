from typing import Annotated
from enum import Enum
from os import remove

from fastapi import FastAPI, UploadFile, Query
from fastapi.responses import FileResponse
from typeParsers.txtParser import *
from typeParsers.docxParser import get_tossups_and_bonuses as get_from_docx
from typeParsers.formatter import format_tossups, format_bonuses
from generator.generator import generate

app = FastAPI()

class FileType(str, Enum):
    txt = "txt"
    docx = "docx"

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/presentation/{name}")
def get_presentation(name: str):
    filename = "../output/" + name + ".pptx"
    return FileResponse(filename)

@app.post("/create/{filetype}")
async def run_vpr(filetype: FileType, file: UploadFile, name: Annotated[str, Query(max_length=30)] = "expanded"):
    localname = "../input/" + name + "." + filetype
    with open(localname, "wb") as local:
        local.write(await file.read())
    tossups, bonuses = get_from_docx(localname)
    tossups, bonuses = format_tossups(tossups), format_bonuses(bonuses)
    generate(tossups, bonuses, "../output/" + name + ".pptx")
    remove(localname)