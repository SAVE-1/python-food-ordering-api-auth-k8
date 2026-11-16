from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.types import NumericCommon


# Original table:
# CREATE TABLE restaurants (
#     id            BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#     name          TEXT NOT NULL,
#     address       TEXT,
#     cuisine_type  TEXT,
#     rating        NUMERIC(2,1) CHECK (rating BETWEEN 0 AND 5),
#     delivery_fee  NUMERIC(8,2) CHECK (delivery_fee >= 0),
#     created_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
#     UNIQUE (name, address)   -- NULL addresses are treated as distinct; make address NOT NULL to enforce fully
# );

class Base(DeclarativeBase):
    pass

class Restaurants(DeclarativeBase):
    __tablename__ = "restaurants"


    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    address: Mapped[str]
    cuisine_type: Mapped[str]
    rating: Mapped[int] = mapped_column(NumericCommon(2, 1))
    delivery_fee: Mapped[int] = mapped_column(NumericCommon(2, 1))
    # created_at: Mapped[datetime] = mapped_column(DateTime)









