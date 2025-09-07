from fastapi import FastAPI
from app.api.routes import router as api_router
from app.core.config import get_settings

settings = get_settings()
app = FastAPI(title=settings.app_name)

app.include_router(api_router)

@app.get("/", tags=["root"])
async def root():
    return {"app": settings.app_name, "env": settings.env}
