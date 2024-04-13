from fastapi import FastAPI
from routers import customer_router, employee_router, vehicle_router, auth_router

app = FastAPI()
app.include_router(customer_router.router, prefix="/api")
app.include_router(employee_router.router, prefix="/api")
app.include_router(vehicle_router.router, prefix="/api")
app.include_router(auth_router.router, prefix="/api")


@app.get("/")
async def root():
	return {
		"message": "Hello World"
	}


@app.get("/hello/{name}")
async def say_hello(name: str):
	return {"message": f"Hello {name}"}
