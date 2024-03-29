from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel


app = FastAPI()


class SHotel(BaseModel):
    addres: str
    name: str
    stars: int


class HotelArgs():
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
    ) -> None:
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.spa = spa
        self.stars = stars
        

@app.get("/hotels", response_model=list[SHotel])
def get_hotels(
        search_args: HotelArgs = Depends(),
    ):
    hotels = [
        {
            "addres": "HEre",
            "name": "SUPADUDA",
            "stars": "5",
        }
    ]
    return hotels, search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

@app.post("/bookings")
def add_booking(booking: SBooking):
    pass
