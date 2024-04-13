from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Dict
from controllers.employee_controller import EmployeeController

router = APIRouter(prefix="/employee", tags=["employee"])
controller = EmployeeController()


# CREATE
@router.post("/employee")
async def create_customer(request: Dict):
	first_name = request["first_name"]
	last_name = request["last_name"]
	phone_number = request["phone_number"]
	email = request["email"]
	password = request["password"]

	if controller.create_employee(first_name, last_name, phone_number, email, password):
		return JSONResponse(
			status_code=status.HTTP_201_CREATED,
			content={"message": "Employee created successfully"}
		)
	else:
		return HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Email already exists"
		)


# READ
@router.get("/get_employee_by_id")
async def get_employee_by_id(request: Dict):
	employee_id = request["employee_id"]
	result = controller.get_employee_by_id(employee_id)

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


@router.get("/get_all_employee")
async def get_all_employee():
	return controller.get_all_employees()


# UPDATE
@router.put("/update_employee")
async def update_employee(request: Dict):
	employee_id = request["employee_id"]
	updates = request["updates"]

	if controller.update_employee(employee_id, **updates):
		return JSONResponse(
			status_code=status.HTTP_200_OK,
			content={"message": "Employee updated successfully"}
		)
	else:
		return HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Invalid fields provided"
		)


# DELETE
@router.delete("/delete_employee")
async def delete_customer(request: Dict):
	employee_id = request["employee_id"]

	if controller.delete_employee(employee_id):
		return JSONResponse(
			status_code=status.HTTP_200_OK,
			content={"message": "Employee deleted successfully"}
		)
	else:
		return HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Employee not found"
		)
