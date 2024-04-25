from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/")
async def handle_post(request: Request):
    # payload = await request.json() # If Required
    return {"status_code": 200}


@app.delete("/")
async def handle_delete(request: Request):
    # payload = await request.json() # If Required
    return {"status_code": 200}
