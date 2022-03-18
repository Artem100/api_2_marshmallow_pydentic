import json
from typing import Optional

from pydantic import BaseModel, ValidationError

copy_i = {"title": "1000","body": "alone","userId": "6669","id": 101}

class NewsFeedResponse(BaseModel):
    title: int
    body: int
    userId: int
    id: Optional[int]

# try:
#     # json_item = json.dumps(copy_i)
#     # comp = NewsFeedResponse(**copy_i)
#     NewsFeedResponse.parse_obj(copy_i)
#     # print(comp)
# except ValidationError as e:
#     print(e)