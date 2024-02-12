from typing import List
from fastapi import APIRouter

from ..model.elements_models import Enchantment, Enchantment_ID

checker_router = APIRouter()

@checker_router.get("/anvil/")
async def check_conflict(req_enchantments: List[Enchantment_ID]) -> None:
    pass