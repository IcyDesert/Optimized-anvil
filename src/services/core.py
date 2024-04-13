from typing import List
from fastapi import APIRouter, Form

# from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from ..model.items_list import categories as __categories # 所有物品的集合
from ..model.request import Enchant_request
from ..model.enchantment import Enchantment, Enchantment_ID
from ..model.enchantments_list import all_enchantments as __all_enc # 所有魔咒的集合


checker_sorter = APIRouter()


@checker_sorter.post("/enchant_query/")
async def check(item_code: str = Form(default=..., pattern="^[012]_[0123]$"),
                req_enchantments_id: List[str] = Form(default=...)):
    """对接收到的表单数据进行处理，包括处理冲突问题和生成最优顺序
    参数有：
    item_code 待附魔的物品代码
    req_enchantments_id 选定的魔咒 ID 列表，str 类型是因为 HTML5 会自动将多选框的 value 转为 String 类型
    返回值：JSON 类型的响应
    """
    # Decode item_code and req_enchantments_id
    item_type, specfic_type = map(int, item_code.split("_"))
    if not (0 <= item_type <= 2 and 0 <= specfic_type <= 3):
        raise ValueError("物品代码错误！")
    req_enchantments_id = [int(enc) for enc in req_enchantments_id] # cover initial data, converting it into int

    # Check for enchantments-item conflicts
    item = __categories[item_type][specfic_type] # the item to be enchanted
    item_check_info = item.conflict_check(req_enchantments_id)
    if item_check_info:
        # some enchantments conflict with the specific item
        _conflict_name = "、".join([f"『{name}』" for name in item_check_info[1]])
        return JSONResponse(
            content={
                "result": "Failed",
                "failure_reason": f"魔咒{_conflict_name}与物品『{item_check_info[0]}』不兼容，追不到的梦想换个梦不就得了~"
            }
        )
    
    # check enchantments' mutual conflict
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
    """对待附魔的魔咒进行魔咒间冲突检查。\n
    若有冲突，则返回包含冲突魔咒名称的JSON数据；若无则返回False，以便程序直接判断真/假。
    参数：
    req 整数列表，实际上是魔咒id列表"""

    req_enchantment = [__all_enc[_id] for _id in req] # get the required Enchantment list 
    # get the entire conflict "list" of all required Enchantment, using set for deduplication
    all_coflict: set[Enchantment_ID] = set()
    for enc in req_enchantment:
        all_coflict |= enc.conflict
    all_coflict_id: set[int] = set(map(lambda _id: _id.value, all_coflict))

    # if the intersection of required enchantments' ID and conflict ID isn't None, conflict must occur
    result = set(req) & all_coflict_id
    if result:
        _conflict_name = "、".join([f"『{__all_enc[_id].name}』" for _id in result])
        return JSONResponse(
            content={
                "result": "Failed",
                "failure-reason": f"魔咒{_conflict_name}间存在冲突..."
            }
        )
    return False


def gen_minxp_list(req_lst: list[Enchantment]):
    """根据给定的魔咒列表，生成消耗最少经验值的附魔顺序。
    参数：\n
    req_lst 指定的魔咒列表
    返回值：\n
    (optimized_order, totalxp) 第一个是最优顺序，包含各魔咒的名称；第二个是最少需要的经验 
    """
    combination: List[tuple[Enchantment, int]] = [
        (enc, enc.max_level * enc.times) for enc in req_lst
    ]
    # list consisting of tuples, which contains Enchantment and its required xp
    combination.sort(key=lambda tup: tup[1])

    optimized_order = [tup[0].name for tup in combination]
    
    l = len(req_lst)
    tmplist = [x for x in range(l, 0, -1)]
    totalxp = sum([tmplist[i]*combination[i][1] for i in range(l)])

    return optimized_order, totalxp
