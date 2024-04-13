"""可附魔物品的模型"""
from enum import Enum
from .enchantment import Enchantment
from pydantic import BaseModel
from .enchantments_list import item_universial, tool_universal, all_enchantments as _all_enc


class ItemType(Enum):
    ARMOR = 0
    WEAPON = 1
    TOOL = 2


class ArmorType(Enum):
    HELMET = 0
    CHESTPLATE = 1
    LEGGINGS = 2
    BOOTS = 3


class WeaponType(Enum):
    SWORD = 0
    BOW = 1
    CROSSBOW = 2
    TRIDENT = 3


class ToolType(Enum):
    PICKAXE = 0
    AXE = 1
    SHOVEL = 2
    HOE = 3


class Item(BaseModel):
    """待附魔的物品的模型。\n
    属性有：\n
    name 魔咒中文名\n
    item_type 大的分类，分为盔甲、武器和工具\n
    specific_type 细分，盔甲就大四件，武器暂时包括剑、弓、弩、三叉戟（后两者功能施工中），工具是镐、斧、锹、锄\n
    compatiable 兼容魔咒\n
    方法有：\n
    conflict_check 
    """
    name: str
    item_type: ItemType
    specific_type: ArmorType | WeaponType | ToolType
    compatiable: set[Enchantment]


    def conflict_check(self, req_enchantment: list[int]) -> bool | tuple[str, list[str]]:
        """检查是否有不相容魔咒。
        如果不相容返回二元元组 (本物品名称, 所有不兼容魔咒的名称列表) ，如果相容则返回False方便程序通过布尔值直接判断，虽然不太合人的逻辑。
        param req_enchantment 要附魔的魔咒ID（整数）的列表"""
        compatiable_ID: set[int] = {i.ID.value for i in self.compatiable}

        # result is a set of enchantments, which are in the request list but not in compatiable list
        # if result isn't None, then there must be conflict enchantments
        result = set(req_enchantment) - compatiable_ID
        if result:
            _conflict = [_all_enc[_id].name for _id in result]
            return (self.name, _conflict)
        return False


# subcategories of Item
class Armor(Item):
    """盔甲模型。\n
    item_type 定为 ItemType.ARMOR
    """
    item_type: ItemType = ItemType.ARMOR


class Weapon(Item):
    """武器模型。\n
    item_type 定为 ItemType.WEAPON
    """
    item_type: ItemType = ItemType.WEAPON


class Tool(Item):
    """工具模型。\n
    item_type 定为 ItemType.TOOL\n
    由于工具只能附上「物品通用」和「工具通用」两种附魔，故 compatiable 默认为这两个 
    """
    item_type: ItemType = ItemType.TOOL
    compatiable: set[Enchantment] = set(item_universial + tool_universal)
