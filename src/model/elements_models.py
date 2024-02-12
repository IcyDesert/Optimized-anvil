from typing import List, Dict, Set
from pydantic import BaseModel
from enum import Enum

class Enchantment_ID(Enum):
    """ 魔咒ID枚举类型 """
    PROTECTION = 0 # 保护
    FIRE_PROTECTION = 1       # 火焰保护
    FEATHER_FALLING = 2       # 摔落缓冲
    BLAST_PROTECTION = 3      # 爆炸保护
    PROJECTILE_PROTECTION = 4 # 弹射物保护
    THORNS = 5                # 荆棘
    RESPIRATION = 6           # 水下呼吸
    DEPTH_STRIDER = 7         # 深海探索者
    AQUA_AFFINITY = 8         # 水下速掘
    SHARPNESS = 9             # 锋利
    SMITE = 10                # 亡灵杀手
    BANE_OF_ARTHROPODS = 11   # 节肢杀手
    KNOCKBACK = 12            # 击退
    FIRE_ASPECT = 13          # 火焰附加
    LOOTING = 14              # 掠夺
    EFFICIENCY = 15           # 效率
    SILK_TOUCH = 16           # 精准采集
    UNBREAKING = 17           # 耐久
    FORTUNE = 18              # 时运
    POWER = 19                # 力量
    PUNCH = 20                # 冲击
    FLAME = 21                # 火矢
    INFINITY = 22             # 无限
    MENDING = 26              # 经验修补
    SWEEPING_EDGE = 38        # 横扫之刃

class Enchantment(BaseModel):
    ID: Enchantment_ID # ID，实际上是整数，只能取Enchantment_ID中的枚举成员
    max_level: int# 最高附魔等级
    success: bool # 附魔成功与否
    conflict_set: Set[Enchantment_ID] | None # 冲突名单，使用集合主要是考虑到集合搜索快

    def __init__(self, ID: Enchantment_ID, 
                 conflict: Set[Enchantment_ID] | None = None,
                 max_level: int = 1, **data):
        super().__init__(**data)
        self.ID = ID
        self.max_level = max_level
        self.conflict_set = conflict
        
    def conflict_check(self, req_enchantment: Dict[Enchantment_ID, int]) -> None:
        for item in req_enchantment:
            if item in self.conflict_set:
                self.success = False
                print(f"Conflict found: #{self.ID} conflict with #{item}!")
                return None
        self.success = True


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
    item_type: ItemType
    specific_type: ArmorType | WeaponType | ToolType
    conflict_set: Set[Enchantment_ID] | None

    def __init__(self, item_type: ItemType, 
                 specific_type: ArmorType | WeaponType | ToolType,
                 conflict_set: Set[Enchantment_ID] | None = None,
                 **data):
        super().__init__(**data)
        self.item_type = item_type
        self.specific_type = specific_type
        self.conflict_set = conflict_set
        
    def conflict_check(self, req_enchantment: Dict[Enchantment_ID, int]) -> None:
        for item in req_enchantment:
            if item in self.conflict_set:
                self.success = False
                print(f"Conflict found: #{self.item_type}-#{self.specific_type} conflict with #{item} !")
                return None
        self.success = True
