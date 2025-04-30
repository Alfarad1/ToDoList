from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError
import logging

logger = logging.getLogger(__name__)

# Custom handler for 422 errors (validation)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )

# Custom handler for database errors
async def db_exception_handler(request: Request, exc: IntegrityError):
    logger.error(f"DB Integrity error: {exc}")
    return JSONResponse(
        status_code=400,
        content={"detail": "Database integrity error"},
    )

# Optional: catch-all for unhandled exceptions
async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )
