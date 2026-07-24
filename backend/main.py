from fastapi import FastAPI

app = FastAPI(
    title="SentinelScan API",
    description="Cybersecurity Assessment Platform API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "application": "SentinelScan",
        "status": "online"
    }
