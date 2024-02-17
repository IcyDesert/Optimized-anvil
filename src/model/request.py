from fastapi import Request
from typing import List


class Enchant_request(Request):
    item: str
    enchantment_list: List[int]