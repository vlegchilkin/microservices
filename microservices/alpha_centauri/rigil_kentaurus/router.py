import secrets

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic_settings import BaseSettings, SettingsConfigDict
from starlette.requests import Request
from starlette.responses import JSONResponse

from . import log

router = APIRouter()
security = HTTPBasic()

# unlinked router example
# from .details import router as details_router
# router.include_router(details_router)


class RigilKentaurusRouterSettings(BaseSettings):
    basic_auth_username: str
    basic_auth_password: str

    model_config = SettingsConfigDict(env_prefix='RIGIL_KENTAURUS_')


settings = RigilKentaurusRouterSettings()


@router.on_event("startup")
async def startup_event():
    log.info("Rigil Kentaurus startup completed")


@router.on_event("shutdown")
async def shutdown_event():
    log.info("Rigil Kentaurus shutdown completed")


def basic_auth(func):
    """HTTP Basic Authorization wrapper"""
    async def wrapper(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
        correct_username = secrets.compare_digest(credentials.username, settings.basic_auth_username)
        correct_password = secrets.compare_digest(credentials.password, settings.basic_auth_password)
        if not (correct_username and correct_password):
            if not correct_username:
                original = settings.basic_auth_username
                received = credentials.username
                log.warn(f"Wrong username received: {received}, should be {original}")
            else:
                masked_password = f"{credentials.password[:2]}***" if credentials.password else "None"
                log.warn(f"Wrong password received: {masked_password}")

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect user or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return await func(request)

    return wrapper


@router.get("/")
@basic_auth
async def root(request: Request):
    return JSONResponse(content={"owner": "Rigil Kentaurus"})
