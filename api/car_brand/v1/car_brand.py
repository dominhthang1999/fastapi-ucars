from typing import List

from fastapi import APIRouter, Depends, Response

from app.car_brand.schema import ExceptionResponseSchema
from app.car_brand.schema.car_brand import CreateCarBrandResponseSchema, CreateCarBrandRequestSchema, \
    GetCarBrandListResponseSchema
from app.car_brand.service import CarBrandService

car_brand_router = APIRouter()


@car_brand_router.get(
    "",
    response_model=List[GetCarBrandListResponseSchema],
    response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def get_car_brand_list():
    return await CarBrandService().get_car_brand_list()


@car_brand_router.post(
    "",
    response_model=CreateCarBrandResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Create a car brand"
)
async def create_car_brand(request: CreateCarBrandRequestSchema):
    await CarBrandService().create_car_brand(**request.dict())
    return Response(status_code=201)


@car_brand_router.get(
    "/{car_brand_id}",
    response_model=GetCarBrandListResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Get a car brand"
)
async def get_car_brand(car_brand_id: int):
    return await CarBrandService().get_car_brand(car_brand_id=car_brand_id)
