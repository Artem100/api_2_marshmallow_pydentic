from pprint import pprint

from src.models.computer.computer import Computer
from src.schema.computer.computerschema import ComputerSchema


def test_computer_required_fields():
    model = Computer("1", "ACTIVE", "2011-10-12", "2023-10-23", "91.192.222.17", "2001:0db8:85a3:0000:0000:8a2e:0370:7334")
    some_json = ComputerSchema.from_orm(model)
    pprint(some_json.json(), indent=2)