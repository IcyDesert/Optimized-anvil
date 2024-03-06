from fastapi import Form
from pydantic import BaseModel
from typing import List
from .enchantment import Enchantment_ID


class Enchant_request(BaseModel):
    item_code: str = Form(default=..., pattern="^[012]_[0123]$") # pattern="^[012]_[0123]$"
    req_enchantments_id: List[Enchantment_ID] = Form(default=...)