# Optimized-anvil

## 由于已有同类工具 [最佳附魔指南](https://zh.minecraft.wiki/w/Tutorial:%E6%9C%80%E4%BD%B3%E9%99%84%E9%AD%94%E6%8C%87%E5%8D%97)  ，本项目不再更新。
## 2025.02.03

---
突发奇想，做的一个我的世界铁砧附魔最优顺序网页，旨在用更少的经验等级消耗达到附魔目的。
程序预计使用 browser/server 形式，server 端计划是 FastAPI 框架，核心逻辑是「排序不等式」。

### TODO

1. favicon
3. 加入铁砧的音效（成功/失败）
4. 可否将conflict制作成统一的一个数据库，而不是魔咒的特有属性？
5. 对报错数据进行一些处理，比如说 item_code 的字符串匹配
5. 写一份fastapi文档和一份使用文档

---

### 预计更新内容
v0.1.1 修改一些数据名称，加favicon
v0.1.2 对一些报错进行处理
v0.x.0 加入JavaScript、CSS——可以着手写fetch API获取服务端数据了；加入铁砧音效；更改数据保存类型
v1.0.0？ 实现结果的网页显示

----

This project just came out as a sudden inspiration when I played the game Minecraft, aiming to provide an optimized order of a given group of enchantments, which consumes the least experience-value in mc.

The programme is expected to use "browser/server" architecture, with server post using **FastAPI module** from python.

---

### 更新日志
v0.1.1 TODO
> 修改数据名称，比如说isxxx之类；实现那个查找类
> favicon加入static文件夹
> 处理可能的报错数据（在main里）


v0.1.0
> 实现基础功能——输入魔咒可以输出经验最少的附魔顺序
> 返回一个JSON响应
