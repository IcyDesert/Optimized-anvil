from pydantic import BaseModel
from typing import List


class Enchant_request(BaseModel):
    item: str
    enchantment_list: List[int]