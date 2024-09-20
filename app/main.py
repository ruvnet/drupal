from fastapi import FastAPI
from app.routers import users, content

app = FastAPI()

app.include_router(users.router)
app.include_router(content.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Python version of Drupal!"}
