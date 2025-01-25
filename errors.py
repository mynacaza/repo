from fastapi import HTTPException


class RequiresLogin(HTTPException):
    pass
