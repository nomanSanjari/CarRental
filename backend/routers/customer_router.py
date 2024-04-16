from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Dict
from controllers.customer_controller import CustomerController

router = APIRouter(prefix="/customers", tags=["customers"])
controller = CustomerController()


# CREATE
@router.post("/create_customer")
async def create_customer(request: Dict):
	first_name = request["first_name"]
	last_name = request["last_name"]
	phone_number = request["phone_number"]
	email = request["email"]
	password = request["password"]

	if controller.create_customer(first_name, last_name, phone_number, email, password):
		return JSONResponse(
			status_code=status.HTTP_201_CREATED,
			content={"message": "Customer created successfully"}
		)
	else:
		return HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Email already exists"
		)


# READ
@router.get("/get_customer_by_id")
async def get_customer_by_id(request: Dict):
	customer_id = request["customer_id"]
	result = controller.get_customer_by_id(customer_id)

	if result:
		return JSONResponse(
			status_code=status.HTTP_200_OK,
			content=result
		)
	else:
		return HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Customer not found"
		)


@router.get("/get_all_customers")
async def get_all_customers():
	return controller.get_all_customers()


# UPDATE
@router.put("/update_customer")
async def update_customer(request: Dict):
	customer_id = request["customer_id"]
	updates = request["updates"]

	if controller.update_customer(customer_id, **updates):
		return JSONResponse(
			status_code=status.HTTP_200_OK,
			content={"message": "Customer updated successfully"}
		)
	else:
		return HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Invalid fields provided"
		)


# DELETE
@router.delete("/delete_customer")
async def delete_customer(request: Dict):
	customer_id = request["customer_id"]

	if controller.delete_customer(customer_id):
		return JSONResponse(
			status_code=status.HTTP_200_OK,
			content={"message": "Customer deleted successfully"}
		)
	else:
		return HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Customer not found"
		)
