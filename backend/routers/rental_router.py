from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from starlette.requests import Request
from typing import Dict
from controllers.rental_controller import RentalController

router = APIRouter(prefix="/rentals", tags=["rentals"])
controller = RentalController()


@router.post("/create_rental")
async def create_rental(request: Dict):
	start_date = request["start_date"]
	end_date = request["end_date"]
	vehicle_id = request["vehicle_id"]
	customer_id = request["customer_id"]
	discount_id = request["discount_id"]
	pricing_type = request["pricing_type"]

	if controller.create_rental(start_date, end_date, vehicle_id, customer_id, discount_id, pricing_type):
		return JSONResponse(
			status_code=status.HTTP_201_CREATED,
			content={"message": "Rental created successfully"}
		)
	else:
		return HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Error creating rental"
		)


@router.get("/get_rental_by_id")
async def get_rental_by_id(request: Dict):
	rental_id = request["rental_id"]
	result = controller.get_rental_by_id(rental_id)

	result["start_date"] = result["start_date"].strftime("%Y-%m-%d")
	result["end_date"] = result["end_date"].strftime("%Y-%m-%d")

	if result:
		return JSONResponse(
			status_code=status.HTTP_200_OK,
			content=result
		)
	else:
		return HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Rental not found"
		)


@router.get("/get_all_rentals")
async def get_all_rentals():
	return controller.get_all_rentals()


@router.get("/get_pending_rentals")
async def get_pending_rentals():
	return controller.get_pending_rentals()


@router.put('/accept_rental')
async def accept_rental(request: Request):
	employee = False

	if 'Type' in request.cookies and request.cookies['Type'] == 'employee':
		employee = True

	request = await request.json()
	rental_id = request["rental_id"]

	if employee:
		if controller.accept_rental(rental_id):
			return JSONResponse(
				status_code=status.HTTP_200_OK,
				content={"message": "Rental verified successfully"}
			)
		else:
			return HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				detail="Error verifying rental"
			)
	else:
		return HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Unauthorized"
	)


@router.put('/reject_rental')
async def reject_rental(request: Request):
	employee = False

	if 'Type' in request.cookies and request.cookies['Type'] == 'employee':
		employee = True

	request = await request.json()
	rental_id = request["rental_id"]

	if controller.reject_rental(rental_id):
		return JSONResponse(
			status_code=status.HTTP_200_OK,
			content={"message": "Rental rejected successfully"}
		)
	else:
		return HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Error rejecting rental"
		)


@router.put("/update_rental")
async def update_rental(request: Dict):
	rental_id = request["rental_id"]
	updates = request["updates"]

	if controller.update_rental(rental_id, **updates):
		return JSONResponse(
			status_code=status.HTTP_200_OK,
			content={"message": "Rental updated successfully"}
		)
	else:
		return HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Error updating rental"
		)


@router.delete("/delete_rental")
async def delete_rental(request: Dict):
	rental_id = request["rental_id"]

	if controller.delete_rental(rental_id):
		return JSONResponse(
			status_code=status.HTTP_200_OK,
			content={"message": "Rental deleted successfully"}
		)
	else:
		return HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Error deleting rental"
		)
