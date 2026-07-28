from fastapi import APIRouter

router = APIRouter(tags=["System"])


@router.get("/")
def root():
    return {
        "message": "Douane AI Platform API",
        "version": "1.0.0",
        "status": "running",
    }


