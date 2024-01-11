from .router import router as comm_router
from starlette.requests import Request
from starlette.responses import JSONResponse


# !!!!
# All functions here have the same name, and it works cause the name doesn't matter.
# We are not calling them directly, it used only for openapi spec as description.
# !!!!


@comm_router.get("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "GET"})


@comm_router.head("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "HEAD"})


@comm_router.post("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "POST"})


@comm_router.put("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "PUT"})


@comm_router.delete("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "DELETE"})


@comm_router.options("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "OPTIONS"})


@comm_router.trace("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "TRACE"})


@comm_router.patch("/some-common-resource")
async def some_common_resource(request: Request):
    return JSONResponse(content={"method": "PATCH"})
