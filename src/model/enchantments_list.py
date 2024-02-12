from .elements_models import Enchantment

from .elements_models import Enchantment_ID as _id

enchantments = [
    Enchantment(
        _id.PROTECTION, 
        {_id.BLAST_PROTECTION, _id.FIRE_PROTECTION, _id.PROJECTILE_PROTECTION,},
       4
    ),
    Enchantment(
        _id.FIRE_PROTECTION,
        {_id.PROTECTION, _id.FIRE_PROTECTION, _id.PROJECTILE_PROTECTION,},
        4,
    ),
    Enchantment(
        _id.FEATHER_FALLING,
        max_level=4,
    ),
    Enchantment(
        _id.BLAST_PROTECTION,
        {_id.PROTECTION, _id.FIRE_PROTECTION, _id.PROJECTILE_PROTECTION,},
        4,
    ),
    Enchantment(
        _id.PROJECTILE_PROTECTION,
        {_id.PROTECTION, _id.BLAST_PROTECTION, _id.FIRE_PROTECTION,},
        4,
    ),
    Enchantment(
        _id.THORNS,
        max_level=3,
    ),
    Enchantment(
        _id.RESPIRATION,
        max_level=3,
    ),
]