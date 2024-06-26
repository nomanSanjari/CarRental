from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Dict
from controllers.vehicle_controller import VehicleController

router = APIRouter(prefix="/vehicle", tags=["auth"])
controller = VehicleController()


# CREATE
@router.post("/create_vehicle")
async def create_vehicle(request: Dict):
	vin = request["vin"]
	make = request["make"]
	model = request["model"]
	vehicle_class = request["vehicle_class"]
	vehicle_type = request["vehicle_type"]
	weekly_rate = request["weekly_rate"]
	daily_rate = request["daily_rate"]
	odometer_reading = request["odometer_reading"]
	drive_train = request["drive_train"]
	is_available = request["is_available"]

	if controller.create_vehicle(vin, make, model, vehicle_class, vehicle_type, weekly_rate, daily_rate, odometer_reading, drive_train, is_available):
		return JSONResponse(
			status_code=status.HTTP_201_CREATED,
			content={"message": "Vehicle created successfully"}
		)
	else:
		return HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Vehicle already exists"
		)


# READ
@router.get("/get_all_vehicles")
async def get_all_vehicles():
	return controller.get_all_vehicles()


@router.get("/get_vehicle_by_id")
async def get_vehicle_by_id(request: Dict):
	vehicle_id = request["vehicle_id"]
	result = controller.get_vehicle_by_id(vehicle_id)

	result["daily_rate"] = str(result["daily_rate"])
	result["weekly_rate"] = str(result["weekly_rate"])
	result["odometer_reading"] = str(result["odometer_reading"])

	if result:
		return JSONResponse(
			status_code=status.HTTP_200_OK,
			content=result
		)
	else:
		return HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Vehicle not found"
		)


@router.get("/get_vehicle_by_vin")
async def get_vehicle_by_vin(request: Dict):
	vin = request["vin"]
	result = controller.get_vehicle_by_vin(vin)

	result["daily_rate"] = str(result["daily_rate"])
	result["weekly_rate"] = str(result["weekly_rate"])
	result["odometer_reading"] = str(result["odometer_reading"])

	if result:
		return JSONResponse(
			status_code=status.HTTP_200_OK,
			content=result
		)
	else:
		return HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Vehicle not found"
		)

@router.get("/search_vehicles")
async def search_vehicles(request: Dict):
	if request["is_available"] and request["is_available"] != "":
		is_available = request["is_available"]
	else:
		is_available = None

	if request["drive_train"] and request["drive_train"] != "":
		drive_train = request["drive_train"]
	else:
		drive_train = None

	if request["vehicle_class"] and request["vehicle_class"] != "":
		vehicle_class = request["vehicle_class"]
	else:
		vehicle_class = None

	if request["vehicle_type"] and request["vehicle_type"] != "":
		vehicle_type = request["vehicle_type"]
	else:
		vehicle_type = None

	return controller.search_vehicles(is_available, drive_train, vehicle_class, vehicle_type)

# UPDATE
@router.put("/update_vehicle")
async def update_vehicle(request: Dict):
	vehicle_id = request["vehicle_id"]
	updates = request["updates"]

	if controller.update_vehicle(vehicle_id, **updates):
		return JSONResponse(
			status_code=status.HTTP_200_OK,
			content={"message": "Vehicle updated successfully"}
		)
	else:
		return HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Invalid fields provided"
		)


# DELETE
@router.delete("/delete_vehicle")
async def delete_vehicle(request: Dict):
	vehicle_id = request["vehicle_id"]

	if controller.delete_vehicle(vehicle_id):
		return JSONResponse(
			status_code=status.HTTP_200_OK,
			content={"message": "Vehicle deleted successfully"}
		)
	else:
		return HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Vehicle not found"
		)
