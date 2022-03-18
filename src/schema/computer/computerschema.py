from pydantic import BaseModel, HttpUrl, UUID4, EmailStr, ValidationError
from pydantic.types import  PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Address, IPv6Address
from pydantic.color import Color
from typing import Optional

from src.enums.const_enums import Statuses


class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4

    class Config:
        orm_mode = True


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr

    class Config:
        orm_mode = True


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]

    class Config:
        orm_mode = True


class ComputerSchema(BaseModel):
     status: Statuses
     activated_at: PastDate # Проверка что тут дата прошедщего времени
     expiration_at: FutureDate # Проверка что тут стоит дата будущая
     host_v4: IPv4Address # Для проверки формата ip v4 адреса
     host_v6: IPv6Address # ip v6
     detailed_info: Optional[DetailedInfo] = {}

     class Config:
         orm_mode = True

# try:
#     comp = ComputerSchema.parse_obj(computer)
#     print(comp)
# except ValidationError as e:
#     print(e)