from pydantic import BaseModel, field_validator


class Pincode(BaseModel):
    pincode: str
#pincode must be exactly 6 digits and should only contain numbers.
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value):
        if not value.isdigit() or len(value) != 6:
            raise ValueError("Pincode must be a 6-digit number.")
        return value

    
class LocationResponse(BaseModel):
    pincode: str
    city: str
    state: str
    country: str   


class BulkRequest(BaseModel):
    pincodes: list[str]     
    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls, value):
        for pincode in value:
            if not pincode.isdigit() or len(pincode) != 6:
               raise ValueError(f"Pincode {pincode} must be a 6-digit number.")
            if len(value) > 100:
                raise ValueError("You can only request up to 100 pincodes at a time.")
            if len(value) == 0:
                raise ValueError("You must provide at least one pincode.")
        return value         