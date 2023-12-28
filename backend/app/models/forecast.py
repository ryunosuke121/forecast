from sqlalchemy import Date, String, Column, ForeignKey, Integer
from app.db import Base


class Forecast(Base):
    __tablename__ = "forecasts"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False, index=True)
    area_id = Column(Integer, ForeignKey("areas.id"), index=True)
    telop_id = Column(Integer, ForeignKey("m_telops.id"))


class Area(Base):
    __tablename__ = "areas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(
        String(20),
        nullable=False,
    )
    livedoor_area_id = Column(Integer, nullable=False)


class MTelop(Base):
    __tablename__ = "m_telops"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(10), nullable=False)
