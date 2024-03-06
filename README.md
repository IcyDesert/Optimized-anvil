# Optimized-anvil

突发奇想，做的一个我的世界铁砧附魔最优顺序网页，旨在用更少的经验等级消耗达到附魔目的。
程序预计使用 browser/server 形式，server 端计划是 FastAPI 框架，核心逻辑是「排序不等式」。

**TODO**：
1. favicon
2. RESTful风格
3. 加入铁砧的音效（成功/失败）
4. 可否将conflict制作成统一的一个数据库，而不是魔咒的特有属性？
5. 对报错数据进行一些处理，比如说 item_code 的字符串匹配
----

This project just came out as a sudden inspiration when I played the game Minecraft, aiming to provide an optimized order of a given group of enchantments, which consumes the least experience-value in mc.
The programme is expected to use "browser/server" architecture, with server post using **FastAPI module** from python.