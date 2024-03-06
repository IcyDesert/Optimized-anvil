from pydantic import BaseModel
from enum import Enum


class Enchantment_ID(int, Enum):
    """ 魔咒ID枚举类型 """
    PROTECTION = 0  # 保护
    FIRE_PROTECTION = 1       # 火焰保护
    FEATHER_FALLING = 2       # 摔落缓冲
    BLAST_PROTECTION = 3      # 爆炸保护
    PROJECTILE_PROTECTION = 4  # 弹射物保护
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
    MENDING = 23              # 经验修补
    SWEEPING_EDGE = 24        # 横扫之刃


conflict_mapping = (
    (
        Enchantment_ID.PROTECTION,
        Enchantment_ID.FIRE_PROTECTION,
        Enchantment_ID.BLAST_PROTECTION,
        Enchantment_ID.PROJECTILE_PROTECTION
     ),
    (
        Enchantment_ID.DEPTH_STRIDER,
    ),
    (
        Enchantment_ID.SHARPNESS,
        Enchantment_ID.BANE_OF_ARTHROPODS,
        Enchantment_ID.SMITE
    ),
    (
        Enchantment_ID.SILK_TOUCH,
        Enchantment_ID.FORTUNE
    ),
    (
        Enchantment_ID.MENDING,
        Enchantment_ID.INFINITY
    )
)


class Enchantment(BaseModel):
    """魔咒模型"""
    ID: Enchantment_ID  # ID，实际上是整数，只能取Enchantment_ID中的枚举成员
    name: str  # 魔咒中文名
    max_level: int = 1  # 最高附魔等级
    times: int = 1  # 乘数，实际附魔消耗的经验是 等级*乘数
    conflict: set[Enchantment_ID] = set()  # 冲突名单，使用集合主要是考虑到集合搜索快

    def __eq__(self, __value: object) -> bool:
        if hasattr(__value, "ID"):
            return self.ID == __value.ID
        return False
    
    def __hash__(self) -> int:
        """有时其会被放入集合，则需要哈希方法"""
        return hash(self.ID)
