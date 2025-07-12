from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id", onupdate="CASCADE", ondelete="CASCADE"))

    category = relationship("Category", back_populates="books")