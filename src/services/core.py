from typing import List, Tuple
from fastapi import APIRouter, Request, Depends, Form
from itertools import chain

# from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from ..model import items_list
from ..model import enchantments_list as enc_list
from ..model.request import Enchant_request
from ..model.enchantment import Enchantment, Enchantment_ID
from ..model.enchantments_list import all_enchantments as __all_enc

checker_sorter = APIRouter()
# templates = Jinja2Templates(directory='src/template')

# all enchantments, sorted by their ID value
# they are sorted so that index of an enchantment is directly mapped to its ID value
# (the initial enchantments list is partly unsorted in terms of ID value)


@checker_sorter.post("/enchant_query/")
async def check(item_code: str = Form(default=..., pattern="^[012]_[0123]$"),
                req_enchantments_id: List[str] = Form(default=...)):
    # Decode the item_code and req_enchantments_id
    item_type, specfic_type = map(int, item_code.split("_"))
    req_enchantments_id = [int(enc) for enc in req_enchantments_id]
    if not (0 <= item_type <= 2 and 0 <= specfic_type <= 3):
        raise ValueError("物品代码错误！")

    # Check for enchantments-item conflicts
    item = items_list.categories[item_type][specfic_type]
    item_check_info = item.conflict_check(req_enchantments_id)
    if item_check_info:
        # some enchantments conflict with the specific item
        __conflict_name = "、".join([f"『{name}』" for name in item_check_info[1]])
        return JSONResponse(
            content={
                "result": "Failed",
                "failure_reason": f"魔咒{__conflict_name}与物品『{item_check_info[0]}』不兼容，追不到的梦想换个梦不就得了~"
            }
        )
    # check enchantments' mutual conflict
    """In this part, my method is to sequentially get 
    1. required enchantments list->set, 2. the entire conflict set of the former,
    then take their intersection. Once the intersection isn't None, 
    there should be conflict enchantments. """
    enc_check_info = enchant_check(req_enchantments_id)
    if enc_check_info:
        return enc_check_info

    req_enchantments = [__all_enc[_id] for  _id in req_enchantments_id]
    success_info = gen_minxp_list(req_enchantments)
    return JSONResponse(
        content={
            "result": "Succeed!",
            "optimized order": "--⟶".join(success_info[0]),
            "minimum xp required": success_info[1]
        }
    )


def enchant_check(req: List[int]):
    """对待附魔的魔咒进行魔咒间冲突检查，若有冲突则返回包含冲突魔咒名称的JSON数据，若无则返回False以便程序直接判断真/假"""
    req_enchantment = [__all_enc[_id] for _id in req]
     # 所有要附上的魔咒的冲突总清单，遍历要附的魔咒并取其冲突名单作并集
    all_coflict = set()
    for enc in req_enchantment:
        all_coflict |= enc.conflict
    all_coflict = set(map(lambda _id: _id.value, all_coflict))

    result = set(req) & all_coflict
    if result:
        __conflict_name = "、".join([f"『{__all_enc[_id].name}』" for _id in result])
        return JSONResponse(
            content={
                "result": "Failed",
                "failure-reason": f"魔咒{__conflict_name}间存在冲突..."
            }
        )
    return False


def gen_minxp_list(req_lst: set[Enchantment]):
    combination: List[tuple[Enchantment, int]] = [
        (enc, enc.max_level * enc.times) for enc in req_lst
    ]
    # list consisting of tuples, which contains Enchantment and its required xp
    combination.sort(key=lambda tup: tup[1])

    optimized_order = [tup[0].name for tup in combination]
    totalxp = sum(tup[1] for tup in combination)

    return optimized_order, totalxp
