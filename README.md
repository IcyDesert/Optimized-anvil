# Optimized-anvil

突发奇想，做的一个我的世界铁砧附魔最优顺序网页，旨在用更少的经验等级消耗达到附魔目的。
程序预计使用 browser/server 形式，server 端计划是 FastAPI 框架，核心逻辑是「排序不等式」。

----

This project just came out as a sudden inspiration when I played the game Minecraft, aiming to provide an optimized order of a given group of enchantments, which consumes the least experience-value in mc.

The programme is expected to use "browser/server" architecture, with server post using **FastAPI module** from python.

---

### 更新日志
v0.1.2 TODO
> 修改数据名称，比如说isxxx之类
> css、js加入
> 添加 favicon
> 处理可能的报错数据（在main里）
> 添加食用手册


v0.1.1
> 修改了「最小经验值」的错误计算方法，现在是正确的了。

v0.1.0
> 实现基础功能——输入魔咒可以输出经验最少的附魔顺序。
> 返回一个JSON响应。