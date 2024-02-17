"""可附魔物品的模型"""
from typing import Set, Dict
from enum import Enum
from .enchantment import Enchantment_ID
from pydantic import BaseModel
from .enchantments_list import item_universial, tool_universal


class ItemType(Enum):
    ARMOR = 1
    WEAPON = 2
    TOOL = 3


class ArmorType(Enum):
    HELMET = 1
    CHESTPLATE = 2
    LEGGINGS = 3
    BOOTS = 4


class WeaponType(Enum):
    SWORD = 1
    BOW = 2
    CROSSBOW = 3
    TRIDENT = 4


class ToolType(Enum):
    PICKAXE = 1
    AXE = 2
    SHOVEL = 3
    HOE = 4


class Item(BaseModel):
    """待附魔的物品的模型，属性有\n
    name 魔咒中文名\n
    item_type 大的分类，分为盔甲、武器和工具\n
    specific_type 细分，盔甲就大四件，武器暂时包括剑、弓、弩、三叉戟（后两者功能施工中），工具是镐、斧、锹、锄\n
    compatiable 兼容魔咒
    """
    name: str
    item_type: ItemType
    specific_type: ArmorType | WeaponType | ToolType
    compatiable: Set[Enchantment_ID]

    def conflict_check(self, req_enchantment: Dict[Enchantment_ID, int]) -> None:
        """检查是否有不相容魔咒"""
        pass
        # for item in req_enchantment:
        #     if item in self.compatable:
        #         self.success = True
        #         print(
        #             f"Conflict found: #{self.item_type}-#{self.specific_type} conflict with #{item} !")
        #         return None
        # self.success = True

# 细分子类
class Armor(Item):
    item_type: ItemType = ItemType.ARMOR


class Weapon(Item):
    item_type: ItemType = ItemType.WEAPON


class Tool(Item):
    item_type: ItemType = ItemType.TOOL
    # 工具类只能附上「通用」和「工具通用」两种附魔，因此在模型里提前设定默认值
    compatiable: Set[Enchantment_ID] = {
        item.ID for item in (item_universial + tool_universal) 
    }
