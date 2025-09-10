from fastapi import APIRouter

router = APIRouter(tags=['health'])


@router.get('/health', tags=['health'])
async def healthcheck() -> dict[str, str]:
    return {'status': 'ok'}
