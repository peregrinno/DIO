from fastapi import APIRouter

router = APIRouter()

@router.post(path='/')
async def post():
    pass   