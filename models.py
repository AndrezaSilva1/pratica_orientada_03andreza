from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
class User(Base):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(
        String(150), unique=True
    )
    books: Mapped[list["Book"]] = relationship(
        back_populates="user"
    )
class Book(Base):
    __tablename__ = "livros"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(150))
    user_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id")
    )
    user: Mapped["User"] = relationship(
        back_populates="books"
    )