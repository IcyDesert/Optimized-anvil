"""可获取魔咒（或者说可在网页选择的魔咒）数据库，分类存储"""
from .enchantment import Enchantment, Enchantment_ID as _id
from itertools import chain

# 物品通用
item_universial = (
    Enchantment(
        ID=_id.UNBREAKING,
        name="耐久",
        max_level=3,
    ),
    Enchantment(
        ID=_id.MENDING,
        name="经验修补",
        times=2,
        conflict={
            _id.INFINITY,
        }
    ),
)

# 盔甲通用
armor_universal = (
    Enchantment(
        ID=_id.PROTECTION,
        name="保护",
        max_level=4,
        conflict={
            _id.BLAST_PROTECTION,
            _id.FIRE_PROTECTION,
            _id.PROJECTILE_PROTECTION,
        }
    ),
    Enchantment(
        ID=_id.FIRE_PROTECTION,
        name="火焰保护",
        max_level=4,
        conflict={
            _id.PROTECTION,
            _id.FIRE_PROTECTION,
            _id.PROJECTILE_PROTECTION,
        },
    ),
    Enchantment(
        ID=_id.FEATHER_FALLING,
        name="摔落缓冲",
        max_level=4,
    ),
    Enchantment(
        ID=_id.BLAST_PROTECTION,
        name="爆炸保护",
        max_level=4,
        times=2,
        conflict={
            _id.PROTECTION,
            _id.FIRE_PROTECTION,
            _id.PROJECTILE_PROTECTION,
        },
    ),
    Enchantment(
        ID=_id.PROJECTILE_PROTECTION,
        name="弹射物保护",
        max_level=4,
        conflict={
            _id.PROTECTION,
            _id.BLAST_PROTECTION,
            _id.FIRE_PROTECTION,
        }
    ),
    Enchantment(
        ID=_id.THORNS,
        name="荆棘",
        max_level=3,
        times=4
    ),
)

# 某些特定种类盔甲才生效
armor_specific = (
    Enchantment(
        ID=_id.RESPIRATION,
        name="水下呼吸",
        max_level=3,
        times=2
    ),
    Enchantment(
        ID=_id.DEPTH_STRIDER,
        name="深海探索者",
        max_level=3,
        times=2
    ),
    Enchantment(
        ID=_id.AQUA_AFFINITY,
        name="水下速掘",
        max_level=3,
        times=2
    )
)

# 工具通用
tool_universal = (
    Enchantment(
        ID=_id.EFFICIENCY,
        name="效率",
        max_level=5,
    ),
    Enchantment(
        ID=_id.SILK_TOUCH,
        name="精准采集",
        times=4,
        conflict={
            _id.FORTUNE,
        }
    ),
    Enchantment(
        ID=_id.FORTUNE,
        name="时运",
        max_level=3,
        times=2,
        conflict={
            _id.SILK_TOUCH,
        }
    )
)

# 剑专用
sword_specific = (
    Enchantment(
        ID=_id.SHARPNESS,
        name="锋利",
        max_level=5,
        conflict={
            _id.BANE_OF_ARTHROPODS,
            _id.SMITE,
        }
    ),
    Enchantment(
        ID=_id.SMITE,
        name="亡灵杀手",
        max_level=5,
        conflict={
            _id.SHARPNESS,
            _id.BANE_OF_ARTHROPODS,
        }
    ),
    Enchantment(
        ID=_id.BANE_OF_ARTHROPODS,
        name="节肢杀手",
        max_level=5,
        conflict={
            _id.SHARPNESS,
            _id.SMITE,
        }
    ),
    Enchantment(
        ID=_id.KNOCKBACK,
        name="击退",
        max_level=2,
    ),
    Enchantment(
        ID=_id.FIRE_ASPECT,
        name="火焰附加",
        max_level=2,
        times=2
    ),
    Enchantment(
        ID=_id.LOOTING,
        name="抢夺",
        max_level=3,
    ),
    Enchantment(
        ID=_id.SWEEPING_EDGE,
        name="横扫之刃",
        max_level=3,
        times=2
    )
)

# 弓专用
bow_specific = (
    Enchantment(
        ID=_id.POWER,
        name="力量",
        max_level=5,
    ),
    Enchantment(
        ID=_id.PUNCH,
        name="冲击",
        max_level=2,
        times=2
    ),
    Enchantment(
        ID=_id.FLAME,
        name="火矢",
        times=2
    ),
    Enchantment(
        ID=_id.INFINITY,
        name="无限",
        times=4,
        conflict={
            _id.MENDING,
        }
    )
)

categories: tuple[tuple[Enchantment]] = (
    item_universial,
    armor_universal,
    armor_specific,
    tool_universal,
    sword_specific,
    bow_specific
)

# 《魔咒大全》
all_enchantments: list[Enchantment] = list(chain(*categories))
all_enchantments.sort(key=lambda enc: enc.ID.value)