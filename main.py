from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import uuid

app = FastAPI(title="Shamsart Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("uploads", exist_ok=True)

@app.get("/")
def root():
    return {"status": "ok", "service": "shamsart-backend"}

@app.post("/image-to-video")
async def image_to_video(image: UploadFile = File(...)):
    job_id = str(uuid.uuid4())
    image_path = f"uploads/{job_id}_{image.filename}"

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # ŞİMDİLİK DEMO RESPONSE
    return {
        "status": "processing",
        "job_id": job_id,
        "message": "Video üretimi başlatıldı (demo)"
    }
