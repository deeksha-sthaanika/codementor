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
from PyPDF2 import PdfReader
import pandas as pd

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


@app.post("/Code_Maturity/")#lang: str,type: str,
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
    
    ready_prompt = prompt.suggestChange(lang, contents_std, contents_code)
    completition = getResponseLlm(ready_prompt)
    # print(completition)

    # return {"prompt":ready_prompt,"language_selected":lang,"type of the doc":type,"content_std": contents_std,"content_code":contents_code}
    return {"prompt":ready_prompt,"result":completition}


# @app.post("/{correctcodegeneration}")
# async def get_file(style: str, file: UploadFile = File(...)):
#     image = np.array(Image.open(file.file))
#     model = config.STYLES[style]
#     start = time.time()
#     output, resized = inference.inference(model, image)
#     name = f"/storage/{str(uuid.uuid4())}.jpg"
#     print(f"name: {name}")
#     # name = file.file.filename
#     cv2.imwrite(name, output)
#     models = config.STYLES.copy()
#     del models[style]
#     asyncio.create_task(generate_remaining_models(models, image, name))
#     return {"name": name, "time": time.time() - start}


# @app.post("/{optimizecode}")
# async def get_file(style: str, file: UploadFile = File(...)):
#     image = np.array(Image.open(file.file))
#     model = config.STYLES[style]
#     start = time.time()
#     output, resized = inference.inference(model, image)
#     name = f"/storage/{str(uuid.uuid4())}.jpg"
#     print(f"name: {name}")
#     # name = file.file.filename
#     cv2.imwrite(name, output)
#     models = config.STYLES.copy()
#     del models[style]
#     asyncio.create_task(generate_files(models, image, name))
#     return {"name": name, "time": time.time() - start}

# async def generate_files(models, image, name: str):
#     executor = ProcessPoolExecutor()
#     event_loop = asyncio.get_event_loop()
#     await event_loop.run_in_executor(
#         executor, partial(process_files, models, image, name)
#     )


# def process_files(models, image, name: str):
#     for model in models:
#         output, resized = inference.inference(models[model], image)
#         name = name.split(".")[0]
#         name = f"{name.split('_')[0]}_{models[model]}.jpg"
#         cv2.imwrite(name, output)


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="localhost", port=8080)