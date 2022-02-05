from typing import List

from pydantic import BaseModel, AnyHttpUrl, Field


class DomainsSchema(BaseModel):
    domains: List[AnyHttpUrl] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "domains": ['https://webscraper.io/test-sites/e-commerce/allinone',
                            'https://webscraper.io/test-sites/e-commerce/static',
                            'https://webscraper.io/test-sites/tables']
            }
        }


def ResponseModel(data):
    return {
        "data": [data],
        "code": 200,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
