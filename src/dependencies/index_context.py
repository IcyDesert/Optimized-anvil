from src.model.enchantments_list import categories as enc_categories
from src.model.items_list import categories as item_categories

index_context_shared = {
        "item_categories_len": len(item_categories),
        "item_categories": item_categories,
        "item_categories_names": ["盔甲", "武器", "工具"],
        "enc_categories_len": len(enc_categories),
        "enc_categories": enc_categories,
        "enc_categories_names": ["通用", "盔甲通用", "盔甲专用", "工具通用", "剑专用", "弓专用"],
    } # 可否不用依赖项？依赖项是什么？