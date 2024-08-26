from typing import Annotated
import os

from fastapi import FastAPI, UploadFile, HTTPException, Query
from fastapi.responses import Response, FileResponse
from parsers.txtParser import *
from parsers.docxParser import get_tossups_and_bonuses as get_from_docx
from parsers.formatter import format_tossups, format_bonuses
from generator.generator import generate

app = FastAPI()
MOD_PATH = ""
if os.path.abspath(os.curdir)[-4:] == "/VPR":
    MOD_PATH = "src/"

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
async def get_presentation(name: str):
    filename = f'{MOD_PATH}output/{name}.pptx'
    headers = {
        'Content-Disposition': 'attachment',
        'Access-Control-Allow-Origin': 'http://localhost:3000'
    }
    try:
        with open(filename):
            pass
    except:
        raise HTTPException(404, "No presentation with that name exists", headers)
    return FileResponse(filename, headers=headers)

@app.delete("/presentation/{name}")
async def remove_presentation(name: str, response: Response):
    response.headers['Access-Control-Allow-Origin'] = "http://localhost:3000"
    filename = f'{MOD_PATH}output/{name}.pptx'
    try:
        os.remove(filename)
    except:
        raise HTTPException(404, "No presentation with that name exists")

@app.post("/create", status_code=201)
async def run_vpr(file: UploadFile, response: Response, name: Annotated[str, Query(max_length=30)] = "expanded"):
    response.headers['Access-Control-Allow-Origin'] = "http://localhost:3000"
    localname = f'{MOD_PATH}input/{file.filename}'
    if localname.split(".")[-1] != "txt" and localname.split(".")[-1] != "docx":
        raise HTTPException(400, "File must be a plain text file or Word document")
    with open(localname, "wb") as local:
        local.write(await file.read())
    tossups, bonuses = get_questions_by_file_type(localname)
    tossups, bonuses = format_tossups(tossups), format_bonuses(bonuses)
    generate(tossups, bonuses, name, MOD_PATH)
    os.remove(localname)

@app.options("/presentation/{name}")
def delete_preflight(name: str):
    headers = {
        'Access-Control-Allow-Origin': 'http://localhost:3000',
        'Access-Control-Allow-Methods': 'POST, GET, DELETE, OPTIONS'
    }
    return Response(status_code=204, headers=headers)