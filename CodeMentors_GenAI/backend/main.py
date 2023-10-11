import asyncio
import time
import uuid
from concurrent.futures import ProcessPoolExecutor
from functools import partial

import cv2
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image

import config
#import inference


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}

@app.post("/{codematurity}")
  #call method pdf/txt etc from utility to read best practice files
  #call method py/sql from utility to read code file
  #call prompt with those passing args
  #call completion and obtain response from this
  #pass this response to front end and show in text area with download option


@app.post("/{correctcodegeneration}")
async def get_file(style: str, file: UploadFile = File(...)):   
    asyncio.create_task(generate_remaining_models(models, image, name))
    return {"name": name, "time": time.time() - start}


@app.post("/{optimizecode}")
async def get_file(style: str, file: UploadFile = File(...)):   
    asyncio.create_task(generate_files(models, image, name))
    return {"name": name, "time": time.time() - start}

async def generate_files(models, image, name: str):
    print("get files")
    


def process_files(models, image, name: str):
    print("process files")


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080)