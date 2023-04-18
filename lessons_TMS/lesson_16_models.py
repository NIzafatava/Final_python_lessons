# file _init_

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import db
from models import Base
from models.phone_book import PhoneBook
from models.contact import Contact


"""
ORM models of the application.
"""

from sqlalchemy.orm import DeclarativeBase

# file db
class Base(DeclarativeBase):
    pass

# file main
engine = None
Session = sessionmaker()


def configure_engine():
    global engine
    if engine is None:
        engine = create_engine("postgresql://postgres:postgres@localhost:5432/lessondb")
        Session.configure(bind=engine)

db.configure_engine()
# Base.metadata.drop_all(db.engine)
Base.metadata.create_all(db.engine)

session = db.Session()

# anns_phone_book = PhoneBook(name="Ann's")
# session.add(anns_phone_book)
# session.commit()

anns_phone_book = session.query(PhoneBook).filter_by(name="Ann's").first()
print(anns_phone_book, type(anns_phone_book))
print(anns_phone_book.contacts, type(anns_phone_book.contacts), type(anns_phone_book.contacts[0]))
print(anns_phone_book.contacts[0].phone)

# anns_contact = Contact(name='Ivan', phone='17235417')
# print(anns_contact)
# anns_contact.phonebook = anns_phone_book
# session.add(anns_contact)
# session.commit()


from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from models import Base

# file contacts
class Contact(Base):
    __tablename__ = "contact"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    phone: Mapped[str]
    phone_book_id = mapped_column(ForeignKey("phonebook.id"))
    phonebook: Mapped["PhoneBook"] = relationship("PhoneBook", back_populates="contacts")

    def __repr__(self):
        return f'{self.name}: {self.phone}'


from sqlalchemy.orm import Mapped, mapped_column, relationship

# from models import Base

# file phone book

class PhoneBook(Base):
    __tablename__ = "phonebook"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    contacts: Mapped[list["Contact"]] = relationship(back_populates="phonebook")

    def __repr__(self):
        return f'{self.name}'