from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#routers

app = FastAPI()
def root():
    return {"message": "Hello World"}
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.include_router(root)