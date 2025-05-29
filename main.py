from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/auth/login")
async def login():
    return {"status": "ok", "token": "fake-token"}

@app.get("/orders")
async def read_orders():
    return [{"order_id": 1}, {"order_id": 2}]

@app.get("/orders/{order_id}")
async def read_order(order_id: int, q: Optional[str] = None):
    return {"order_id": order_id, "q": q}

@app.get("/analytics")
async def read_analytics():
    return {"analytics": "data"}

