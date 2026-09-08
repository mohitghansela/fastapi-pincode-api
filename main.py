from fastapi import FastAPI

from data import pincode_data
from exceptions import (
    PincodeNotFoundException,
    InvalidPincodeException,
    pincode_not_found_exception_handler,
    invalid_pincode_exception_handler,
)
from models import LocationResponse, Pincode, BulkRequest

app = FastAPI(
    title="Pincode Lookup API",
    description="This API allows you to lookup pincode information.",
    version="1.0.0",
)

# Register custom exception handlers
app.add_exception_handler(
    PincodeNotFoundException,
    pincode_not_found_exception_handler
)

app.add_exception_handler(
    InvalidPincodeException,
    invalid_pincode_exception_handler
)


@app.get("/")
def root():
    return {"message": "Welcome to the Pincode Lookup API!"}


@app.get("/pincode/{pincode}", response_model=LocationResponse)
def lookup_pincode(pincode: str):
    if len(pincode) != 6 or not pincode.isdigit():
        raise InvalidPincodeException(
            pincode,
            reason="Pincode must be a 6-digit number."
        )

    if pincode not in pincode_data:
        raise PincodeNotFoundException(pincode)

    location = pincode_data[pincode]

    return LocationResponse(
        pincode=pincode,
        city=location["city"],
        state=location["state"],
        country="India"
    )


@app.post("/bulk", response_model=list[LocationResponse])
def bulk_lookup(request: BulkRequest):
    results = []
    missing_pincodes = []
    for pincode in request.pincodes:
        if pincode not in pincode_data:
            continue

        location = pincode_data[pincode]

        results.append(
            LocationResponse(
                pincode=pincode,
                city=location["city"],
                state=location["state"],
                country="India"
            )
        )

    return results