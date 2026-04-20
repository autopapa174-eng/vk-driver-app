from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

markers = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return FileResponse("../index.html")

@app.get("/markers")
def get_markers():
    return markers

@app.post("/add")
def add_marker(marker: dict):
    markers.append(marker)
    return {"status": "ok"}
