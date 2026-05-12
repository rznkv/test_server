from fastapi import APIRouter, Request

router = APIRouter()

@router.get('/client_check')
async def client_check(request: Request):
    host = request.client.host
    port = request.client.port
    return {'message': f'Client connected in {host} - {port}'}


@router.get('/')
async def root():
    return {'message': 'server is running 2'}

