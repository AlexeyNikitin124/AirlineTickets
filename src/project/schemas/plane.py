from pydantic import BaseModel, Field, ConfigDict

class PlaneSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    serial_number: int
    model: str
    number_of_passengers: int
    load_capacity: int
    airline_owner: str