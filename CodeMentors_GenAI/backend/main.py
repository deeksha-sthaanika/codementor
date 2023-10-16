import asyncio
import time
import uuid
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from utilities import Utility as fn
from completition import getResponseLlm
import prompt
import os
import io


# import cv2
import uvicorn
from fastapi import File,FastAPI,UploadFile,Form
import numpy as np
from PIL import Image

import config
#import inference


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


@app.post("/Optimize_Code/")#lang: str,type: str,
async def create_upload_file(lang: str = Form(...),type: str = Form(...),file_code: UploadFile = File(...)):#files: UploadFile = File(...)
    contents_code=await file_code.read() 
    ready_prompt = prompt.optimizeCode(lang, contents_code)
    completition = getResponseLlm(ready_prompt)
    
    return {"prompt":ready_prompt,"result":completition}

@app.post("/Format_Code/")#lang: str,type: str,
async def create_upload_file(lang: str = Form(...),type: str = Form(...),file_std: UploadFile = File(...),file_code: UploadFile = File(...)):#files: UploadFile = File(...)
    contents_code=await file_code.read()
    file_std1=io.BytesIO(await file_std.read())

    if type=='text':
        contents_std=fn.readTxt(file_std1)
    elif type=='pdf':
        contents_std=fn.readPdf(file_std1)
    elif type=='docx':
        contents_std=fn.readDoc(file_std1)
    elif type=='csv':
        contents_std=fn.readCsv(file_std1)
    elif type=='excel':
        contents_std=fn.readExcel(file_std1)
    
    ready_prompt = prompt.constructCode(lang, contents_std, contents_code)
    completition = getResponseLlm(ready_prompt)
  
    return {"prompt":ready_prompt,"result":completition}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080)