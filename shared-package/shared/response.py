from typing import Optional, TypeVar, Generic, Dict
from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel
from fastapi.responses import JSONResponse
from shared.constants import *

T = TypeVar("T")


class BaseResponse(GenericModel, Generic[T]):
    status_code: int
    message: str
    data: Optional[T] = None
    error: Optional[str] = None
    errors: Optional[list[dict]] = None
    meta: Optional[Dict] = {}

    def response(self) -> JSONResponse:
        json = {}

        if self.message:
            json["message"] = self.message
        if self.data:
            json["data"] = self.data
        if self.meta:
            json["meta"] = self.meta
        if self.error:
            json["error"] = self.error
        if self.errors:
            json["errors"] = self.errors

        return JSONResponse(
            status_code=self.status_code,
            content=json
        )


# 2xx
def response_ok(data=None, message="Success"):
    return BaseResponse(status_code=HTTP_200_OK, message=message, data=data).response()


def response_created(data=None, message="Created"):
    return BaseResponse(status_code=HTTP_201_CREATED, message=message, data=data).response()


def response_plain_text(message: str):
    return JSONResponse(
        status_code=HTTP_200_OK,
        content=message,
        media_type="text/plain"
    )

# 3xx


def response_redirect(url: str):
    return JSONResponse(
        status_code=HTTP_307_TEMPORARY_REDIRECT,
        headers={"Location": url},
        content=None
    )

# 4xx


def response_bad_request(message="Bad request"):
    return BaseResponse(status_code=HTTP_400_BAD_REQUEST, message=message).response()


def response_not_found(message="Not found"):
    return BaseResponse(status_code=HTTP_404_NOT_FOUND, message=message).response()


def response_unauthorized(message="Unauthorized"):
    return BaseResponse(status_code=HTTP_401_UNAUTHORIZED, message=message).response()


def response_forbidden(message="Forbidden"):
    return BaseResponse(status_code=HTTP_403_FORBIDDEN, message=message).response()


def response_validation_error(error, message="Validation error"):
    return BaseResponse(status_code=HTTP_422_UNPROCESSABLE_ENTITY, message=message, error=error).response()


def response_validation_errors(errors: list[dict], message="Validation errors"):
    return BaseResponse(status_code=HTTP_422_UNPROCESSABLE_ENTITY, message=message, errors=errors).response()
# 5xx


def response_internal_error(message="Something went wrong"):
    return BaseResponse(status_code=HTTP_500_INTERNAL_SERVER_ERROR, message=message).response()
