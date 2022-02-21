from computer_example import *
from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from pydantic.types import  PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Address, IPv6Address
from pydantic.color import Color

from src.enums.const_enums import Statuses


class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
     status: Statuses
     activated_at: PastDate # Проверка что тут дата прошедщего времени
     expiration_at: FutureDate # Проверка что тут стоит дата будущая
     host_v4: IPv4Address # Для проверки формата ip v4 адреса
     host_v6: IPv6Address # ip v6
     detailed_info: DetailedInfo

comp = Computer.parse_obj(computer)
print(comp)