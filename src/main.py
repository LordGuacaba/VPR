from typing import Annotated
from os import remove

from fastapi import FastAPI, UploadFile, HTTPException, Query
from fastapi.responses import FileResponse
from typeParsers.txtParser import *
from typeParsers.docxParser import get_tossups_and_bonuses as get_from_docx
from typeParsers.formatter import format_tossups, format_bonuses
from generator.generator import generate

app = FastAPI()


def get_questions_by_file_type(filename: str) -> tuple:
    """
    Returns a (tossups, bonuses) tuple of question sets based on the packet's file type.
    """
    extension = filename.split(".")[-1]
    if extension == "txt":
        return get_tossups_and_bonuses(filename)
    elif extension == "docx":
        return get_from_docx(filename)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/presentation/{name}")
def get_presentation(name: str):
    filename = "../output/" + name + ".pptx"
    try:
        with open(filename):
            pass
    except:
        raise HTTPException(404, "No presentation with that name exists")
    return FileResponse(filename)

@app.delete("/presentation/{name}")
def remove_presentation(name: str):
    filename = "../output/" + name + ".pptx"
    try:
        remove(filename)
    except:
        raise HTTPException(404, "No presentation with that name exists")

@app.post("/create")
async def run_vpr(file: UploadFile, name: Annotated[str, Query(max_length=30)] = "expanded"):
    localname = "../input/" + file.filename
    if localname.split(".")[-1] != "txt" and localname.split(".")[-1] != "docx":
        raise HTTPException(400, "File must be a plain text file or Word document")
    with open(localname, "wb") as local:
        local.write(await file.read())
    tossups, bonuses = get_questions_by_file_type(localname)
    tossups, bonuses = format_tossups(tossups), format_bonuses(bonuses)
    generate(tossups, bonuses, "../output/" + name + ".pptx")
    remove(localname)