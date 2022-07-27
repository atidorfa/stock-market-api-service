import os
import uvicorn


if __name__ == "__main__":
    uvicorn.run("app.app_main:app", host="0.0.0.0", port=8000, log_config=os.getenv("APP_LOGGING_CONFIG"), reload=True, workers=1)
