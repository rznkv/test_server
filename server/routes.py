from fastapi import APIRouter, Request
from shared.models import MathRequest

router = APIRouter()

@router.get('/client_check')
async def client_check(request: Request):
    host = request.client.host
    port = request.client.port
    return {'message': f'Client connected in {host} - {port}'}


@router.get('/')
async def root():
    return {'message': 'server is running'}

@router.get('/square')
async def square(x: float):

    return {
        'x': x,
        'square': x * x
    }

@router.post('/calculate')
async def calculate(data: MathRequest):
    a = data.digits[0]
    b = data.digits[1]

    if data.action == "+":
        result = a + b

    elif data.action == "-":
        result = a - b

    else:
        result = "unknown action"

    return {
        "digits": data.digits,
        "action": data.action,
        "result": result
    }