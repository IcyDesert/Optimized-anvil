from pydantic import BaseModel
from typing import List

class enchant_response(BaseModel):
    success: bool = False
    failure_reason: str | None = None
    optimized_order: List[int] | None = None