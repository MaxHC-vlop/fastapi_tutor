from typing import Optional

from app.database import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Date, ForeignKey, Computed


class Bookings(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_to: Mapped[Date] = mapped_column(Date, nullable=False)
    date_from: Mapped[Date] = mapped_column(Date, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    total_days: Mapped[int] = mapped_column(Integer, Computed("date_to - date_from"))
    total_cost: Mapped[int] = mapped_column(Integer, Computed("(date_to - date_from) * price"))
