from fastapi import FastAPI

app = FastAPI(title="NYC Apartment Search")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
