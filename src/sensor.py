from database_manager import Base, Column, Integer, String, ForeignKey, Enum, DateTime
from parking_status import ParkingStatus


class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parking_status = Column(Enum(ParkingStatus))
    updated_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
