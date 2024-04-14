from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Dict
from controllers.rental_controller import RentalController

router = APIRouter(prefix="/rentals", tags=["rentals"])
controller = RentalController()


@router.post("/create_rental")
async def create_rental(request: Dict):
	start_date = request["start_date"]
	end_date = request["end_date"]
	vehicle_id = request["vehicle_id"]
	employee_id = request["employee_id"]
	customer_id = request["customer_id"]

	if controller.create_rental(start_date, end_date, vehicle_id, employee_id, customer_id):
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
