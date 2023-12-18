from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Word(Base):
    __tablename__ = 'word'

    id: Mapped[int] = mapped_column(primary_key=True)
    eng_name: Mapped[str] = mapped_column()
    ru_name: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(nullable=True)
