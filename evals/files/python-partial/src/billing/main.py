from fastapi import FastAPI

app = FastAPI(title="Billing API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
