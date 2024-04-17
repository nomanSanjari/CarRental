from fastapi import APIRouter, HTTPException, Response, status
from typing import Dict

from starlette.responses import JSONResponse

from controllers.discount_controller import DiscountController

router = APIRouter(prefix="/discounts", tags=["discounts"])
controller = DiscountController()


@router.post("/create_discount")
async def create_discount(request: Dict):
	discount_type = request["discount_type"]
	discount_amount = request["discount_amount"]

	result = controller.create_discount(discount_type, discount_amount)

	if result is not None:
		return JSONResponse(
			status_code=status.HTTP_201_CREATED,
			content=result
		)
	else:
		return HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Error creating discount"
		)


@router.get("/get_all_discounts")
async def get_all_discounts():
	results = controller.get_all_discounts()

	if results is not None:
		return JSONResponse(
			status_code=status.HTTP_200_OK,
			content=results
		)
	else:
		return HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=results
		)


@router.get("/get_discount_by_id")
async def get_discount_by_id(request: Dict):
	discount_id = request["discount_id"]
	result = controller.get_discount_by_id(discount_id)

	if result is not None:
		return result
	else:
		return HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
		)


@router.put("/update_discount")
async def update_discount(request: Dict):
	discount_id = request["discount_id"]
	updates = request["updates"]

	result = controller.update_discount(discount_id, **updates)

	if result:
		return Response(
			status_code=status.HTTP_200_OK,
			content="Discount updated successfully"
		)
	else:
		return HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Error updating discount"
		)


@router.delete("/delete_discount")
async def delete_discount(request: Dict):
	discount_id = request["discount_id"]

	result = controller.delete_discount(discount_id)
	if result:
		return Response(
			status_code=status.HTTP_200_OK,
			content="Discount deleted successfully"
		)
	else:
		return HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Error deleting discount"
		)
