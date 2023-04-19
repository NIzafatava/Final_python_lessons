# Для дз 11 написать модели, используя SQLAlchemy ORM. За пример можно брать модели
# Contact и PhoneBook, которые мы смотрели на уроке, а также читать документацию по
# ссылке в чате. Дублирую условие задачи:


# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Класс для истории должен хранить операцию (снятие или пополнение), сумму, дату
# и время операции.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey, Enum, Table, Column, Integer, String, DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

class Base(DeclarativeBase):
    pass

engine = None
Session = sessionmaker()

def configure_engine():
    global engine
    if engine is None:
        engine = create_engine("postgresql://postgres:izofatova123@localhost:5432/lessondb")
        Session.configure(bind=engine)


configure_engine()

Base.metadata.create_all(engine)
session = Session()

#creating module "Type_of_operation"

class Type_of_operation(enum.Enum):
    adding = 1
    withdraw = 0


#creating module "Bank Account"

class BankAccount(Base):
    __tablename__ = 'bank_account'

    id: Mapped[int] = mapped_column(primary_key=True)
    account_number: Mapped[int]
    balance: Mapped[int]
    history: Mapped['HistoryBankAccount'] = relationship('HistoryBankAccount', back_populates='account')
#
    def __repr__(self):
        return f'{self.account_number}:{self.balance}'
#
#
#
# #creating module "History of the Bank Account"
class HistoryBankAccount(Base):
    __tablename__ = 'history bank account'

    id: Mapped[int] = mapped_column(primary_key=True)
    id_account_number: Mapped[int] = mapped_column(ForeignKey('bank_account.account_number'))
    type_of_operation: Mapped[str] = mapped_column(Enum(Type_of_operation))
    amount_of_operation: Mapped[int]
    account: Mapped['BankAccount'] = relationship('BankAccount', back_populates='history')



my_history = HistoryBankAccount(amount_of_operation = 40)
session.add(my_history)
session.commit()

Base.metadata.create_all(engine)
session = Session()
my_account = BankAccount(account_number=23567, balance=300)
print(my_account)
my_account.history = my_history
session.add(my_account)
session.commit()







