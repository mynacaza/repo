from starlette.middleware.base import BaseHTTPMiddleware


from fastapi import Request
from fastapi.responses import RedirectResponse


class CustomMiddlewate(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # if request.url.path in ["/login", "/", "/docs", "/openapi.json", "/sign-up"] or request.url.path.startswith('/static'):
        response = await call_next(request) 
        return response
    
        token = request.headers.get("Authorization")
        if not token:
            return RedirectResponse('http://localhost:8000')
        
        response = await call_next(request)
        return response

