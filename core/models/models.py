from core.DB.database import Base
from sqlalchemy import String,Boolean,Integer,Column,Unicode

class User(Base):
    __tablename__='User'
    id=Column(Integer,primary_key=True)
    first_name=Column(String(255),nullable=False)
    last_name=Column(String(255), nullable=False)
    email=Column(String(100),unique=True,nullable=False)
    mobile=Column(Unicode(12))
    is_active=Column(Boolean)


