# 可附魔（或者说可选取的）物品名单
from .item import Armor, Weapon, Tool, ArmorType, WeaponType, ToolType
from . import enchantments_list as e


__iu = e.item_universial  # Item_Universal
__au = __iu + e.armor_universal  # Armor_Universal
# Helmet_specific，后面两个分别是「水下呼吸」和「水下速掘」
__hs = __au + (e.armor_specific[0], e.armor_specific[2])
__bts = __au + (e.armor_specific[1],)  # BooT_specific
__ss = __iu + e.sword_specific  # Sword_specific
__bws = __iu + e.bow_specific  # BoW_specific

armor = (
    Armor(
        name="头盔",
        specific_type=ArmorType.HELMET,
        compatiable={item.ID for item in __hs}
    ),
    Armor(
        name="胸甲",
        specific_type=ArmorType.CHESTPLATE,
        compatiable={item.ID for item in __au}
    ),
    Armor(
        name="护腿",
        specific_type=ArmorType.LEGGINGS,
        compatiable={item.ID for item in __au}
    ),
    Armor(
        name="靴子",
        specific_type=ArmorType.BOOTS,
        compatiable={item.ID for item in __bts}
    )
)

weapon = (
    Weapon(
        name="剑",
        specific_type=WeaponType.SWORD,
        compatiable={item.ID for item in __ss}
    ),
    Weapon(
        name="弓",
        specific_type=WeaponType.BOW,
        compatiable={item.ID for item in __bws}
    ),
)

tool = (
    Tool(
        name="镐",
        specific_type=ToolType.PICKAXE
    ),
    Tool(
        name="斧",
        specific_type=ToolType.AXE
    ),
    Tool(
        name="锹",
        specific_type=ToolType.SHOVEL
    ),
    Tool(
        name="锄",
        specific_type=ToolType.HOE
    )
)
