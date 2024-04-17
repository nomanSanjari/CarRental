from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Dict

from controllers.auth_controller import AuthController

router = APIRouter(prefix="/auth", tags=["auth"])
controller = AuthController()


@router.post("/login_customer")
async def login(request: Dict):
	email = request["email"]
	password = request["password"]

	result = controller.login_customer(email, password)

	if result:
		response = JSONResponse(
			status_code=status.HTTP_200_OK,
			content=result
		)
		response.set_cookie(
			key="CustomerID",
			value=result["id"],
			httponly=True
		)
		response.set_cookie(
			key="Type",
			value="customer",
			httponly=True
		)

		return response
	else:
		return HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Invalid credentials"
		)


@router.post("/login_employee")
async def login(request: Dict):
	email = request["email"]
	password = request["password"]

	result = controller.login_employee(email, password)

	if result:
		response = JSONResponse(
			status_code=status.HTTP_200_OK,
			content=result
		)
		response.set_cookie(
			key="EmployeeID",
			value=result["id"],
			httponly=True
		)
		response.set_cookie(
			key="Type",
			value="employee",
			httponly=True
		)

		return response
	else:
		return HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Invalid credentials"
		)
