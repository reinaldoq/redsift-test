from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.extractor.extractor import Extractor
from app.server.models.domains import (
    ResponseModel,
    DomainsSchema,
)

router = APIRouter()


@router.post("/", response_description="Domains received and processed")
async def add_domains_data(domains: DomainsSchema = Body(...)):
    domains_json = jsonable_encoder(domains)
    extractor = Extractor()
    page_titles = extractor.get_titles(urls=domains_json['domains'])
    return ResponseModel(page_titles)
