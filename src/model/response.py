from fastapi import Response
from typing import List

class Enchant_response(Response):
    success: bool = False
    failure_reason: str | None = None
    optimized_order: List[int] | None = None