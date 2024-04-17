from fastapi import FastAPI
from routers import customer_router, employee_router, vehicle_router, auth_router, discount_router, rental_router
from utils.mailer import send_acceptance_email, send_rejection_email

app = FastAPI()
app.include_router(customer_router.router, prefix="/api")
app.include_router(employee_router.router, prefix="/api")
app.include_router(vehicle_router.router, prefix="/api")
app.include_router(discount_router.router, prefix="/api")
app.include_router(rental_router.router, prefix="/api")
app.include_router(auth_router.router, prefix="/api")


@app.get("/")
async def root():
	return {
		"message": "Hello World"
	}