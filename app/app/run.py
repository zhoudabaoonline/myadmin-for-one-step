import os

# TO SUPPORT RUN python main.py in windows,but I use python "app/main.py" to start in liunx
print(os.path.join(os.path.dirname(__file__), "../.."))
os.sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


from app.extensions.logger import LOGGING_CONFIG
from app.middleware import register_middleware
from app.runapp.api import router
from app.core.config import settings
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# app
app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
# set middleware
register_middleware(app)
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# set router
app.include_router(router, prefix="", tags=['clientApi'])

if __name__ == '__main__':
    import uvicorn

    # Don't set debug/reload equals True,becauese TimedRotatingFileHandler can't support multi-prcoess
    # or dont't use my LOGGING_CONFIG in debug/reload
    # uvicorn.run(app='main:app', host="0.0.0.0", port=8080, log_config=LOGGING_CONFIG)
    uvicorn.run(app='run:app', host="0.0.0.0", port=8083)
