from fastapi import APIRouter

from src.api.models.basic import Root

router = APIRouter()


@router.get("/", response_model=Root)
async def root() -> Root:
    """get info about the authors and the group"""
    return Root()
