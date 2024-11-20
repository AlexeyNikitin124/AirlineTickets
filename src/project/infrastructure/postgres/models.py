from sqlalchemy.orm import Mapped, mapped_column
from src.project.infrastructure.postgres.database import Base

class Plane(Base):
    __tablename__ = "planes"

    serial_number: Mapped[str] = mapped_column(primary_key=True)
    model: Mapped[str] = mapped_column(nullable=False)
    number_of_passengers: Mapped[int] = mapped_column(nullable=False)
    load_capacity: Mapped[int] = mapped_column(nullable=False)
    airline_owner: Mapped[str] = mapped_column(nullable=False)