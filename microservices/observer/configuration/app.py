import mscom.config as microservice_config
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from . import log
from mscom.actuator.router import router as actuator_router

app = FastAPI(title="Observer")
app.include_router(actuator_router)


@app.on_event("startup")
async def startup_event():
    log.info(f"Initializing Observer on port {microservice_config.microservice_settings.server_port}")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down Observer")


@app.get("/")
async def root(request: Request):
    return JSONResponse(content={"owner": "Observer"})


@app.get(
    "/celestial_sphere/skies/{sky}"
    "/constellations/{constellation}/star_systems/{star_system}"
)
async def get_star_system(sky: str, constellation: str, star_system: str):
    return JSONResponse(content={"action": "Get Star System"})


@app.get(
    "/celestial_sphere/skies/{sky}"
    "/constellations/{constellation}/star_systems/{star_system}/stars/{star}"
)
async def get_star(sky: str, constellation: str, star_system: str, star: str):
    return JSONResponse(content={"action": "Get Star"})


@app.get(
    "/celestial_sphere/skies/{sky}"
    "/constellations/{constellation}/star_systems/{star_system}/stars/{star}/planets/{planet}"
)
async def get_planet(sky: str, constellation: str, star_system: str, star: str, planet: str):
    return JSONResponse(content={"action": "Get Planet"})


@app.get(
    "/celestial_sphere/skies/{sky}"
    "/constellations/{constellation}/star_systems/{star_system}/stars/{star}/planets/{planet}/oceans/{ocean}"
)
async def get_ocean(sky: str, constellation: str, star_system: str, star: str, planet: str, ocean: str):
    return JSONResponse(content={"action": "Get Ocean"})
