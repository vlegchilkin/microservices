from mscom import config
from uvicorn import run as run_app_loop

if __name__ == "__main__":
    run_app_loop(
        "mocks.configuration.app:app",
        host="0.0.0.0",
        port=config.microservice_settings.server_port,
        reload=len(config.microservice_settings.reload_dirs) > 0,
        reload_dirs=config.microservice_settings.reload_dirs,
        log_level=config.log_settings.log_level,
        access_log=config.log_settings.enable_access_log,
    )
