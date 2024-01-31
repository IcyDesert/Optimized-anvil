from pydantic import BaseModel
from typing import List


class enchant_request(BaseModel):
    item: str
    enchantment_list: List[int]