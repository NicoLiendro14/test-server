import json
import os
import time
from typing import Optional

import uvicorn


from fastapi import FastAPI, Response, Request, status, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse


app = FastAPI()

origins = [
    "*",
    "http://localhost",
    "http://localhost:5049",
    "https://localhost",
    "https://localhost:5049",
    "http://localhost:5049/"
    "http://localhost:5049/*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/whatsapp/login")
async def root(response: Response):
    root_path = os.path.dirname(os.path.abspath(__file__))
    images_path = os.path.join(root_path, "images")
    if not os.path.exists(images_path):
        os.makedirs(images_path)
    image_qr_name = "qr_pic.png"
    path_qr = os.path.join(images_path, image_qr_name)
    return FileResponse(path_qr)


@app.post("/message/add")
async def add_message(request: Request, response: Response, file: Optional[UploadFile] = None):
    response.status_code = status.HTTP_200_OK
    return {
        "message": f"Mensaje programado con exito:",
        "file_path": "file_path",
        "job_id": "job_.id"
    }


@app.put("/message/edit/{job_id}")
async def edit_message(request: Request, response: Response, file: Optional[UploadFile], job_id: str):
    response.status_code = status.HTTP_200_OK
    return {"message": "Mensaje editado con éxito {job_id}".format(job_id=job_id)}


@app.delete("/message/delete/{job_id}")
async def delete_message(job_id: str, response: Response):
    response.status_code = status.HTTP_200_OK
    return {"message": f"Mensaje eliminado correctamente. job_id: {job_id}"}


@app.get("/messages/{group_name}")
async def get_all_messages(group_name: str):
    try:
        return {
            "week": {
                "tue": [
                    {
                        "message": "Hola",
                        "type": "image",
                        "file_path": "C:\\Users\\Nicolas\\Desktop\\UpWork Projects\\WhatsappCloudBased\\images\\daniel-jensen-88Kt5KHUe_8-unsplash.jpg",
                        "hour": "1:00 AM",
                        "job_id": "3bc7ccfa51194de089143b71e269f8e5"
                    },
                    {
                        "message": "Hola",
                        "type": "image",
                        "file_path": "C:\\Users\\Nicolas\\Desktop\\UpWork Projects\\WhatsappCloudBased\\images\\daniel-jensen-88Kt5KHUe_8-unsplash.jpg",
                        "hour": "1:05 AM",
                        "job_id": "0f0cc85ee87d4345abdb80236cbfd739"
                    },
                ],
                "mon": [
                    {
                        "message": "Chau",
                        "type": "image",
                        "file_path": "C:\\Users\\Nicolas\\Desktop\\UpWork Projects\\WhatsappCloudBased\\images\\daniel-jensen-88Kt5KHUe_8-unsplash.jpg",
                        "hour": "1:00 AM",
                        "job_id": "3bc7ccfa51194de089143b71e269f8e5"
                    },
                    {
                        "message": "Chau",
                        "type": "image",
                        "file_path": "C:\\Users\\Nicolas\\Desktop\\UpWork Projects\\WhatsappCloudBased\\images\\daniel-jensen-88Kt5KHUe_8-unsplash.jpg",
                        "hour": "1:05 AM",
                        "job_id": "0f0cc85ee87d4345abdb80236cbfd739"
                    },
                ]
            },
            "group_name": "Richard Pobre"
        }
    except Exception as e:
        print(e)


async def save_upload_file(file: UploadFile) -> str:
    file_path = f"images/{file.filename}"
    absolute_file_path = os.path.abspath(file_path)
    with open(absolute_file_path, "wb") as f:
        f.write(await file.read())
    return absolute_file_path


@app.get("/message/group")
async def group_exist(request: Request, response: Response):
    response.status_code = status.HTTP_200_OK
    return {"message": "Grupo encontrado"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5049)
