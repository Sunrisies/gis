# Day 16｜2026-11-03 周二｜M2 页面与交互

## 今日主题：MapContainer 设计 + 多实例隔离

**今天预算 1–1.5 小时。** 切法：5min 找回上下文 → 70min 主线 → 15min 记录。

---

## 一、今日任务（按顺序做）

1. 设计 `MapContainer.vue` 的 props 与事件（你要暴露什么给外层？）
2. 处理多实例：两个地图组件同时存在时不互相干扰
3. 处理销毁：清空定时器、事件监听、`primitives`
4. 自测：`viewer.scene.primitives.length` 在销毁后是否归零

## 二、产出（必须留下，否则等于没做）

- [ ] 可复用的 `MapContainer.vue`
- [ ] 销毁验证结果

> 今天不是算法日（算法固定在 **周二 / 周四 / 周日**）。

## 三、参考资料

📖 [Vue3 Composition API FAQ](https://cn.vuejs.org/guide/extras/composition-api-faq.html) · [Vue3 渲染机制](https://cn.vuejs.org/guide/extras/rendering-mechanism.html)

## 四、验收标准（怎么证明今天真做完了）

✅ 销毁后 `scene.primitives.length` 归零
✅ 连续挂载/卸载 20 次，内存不持续增长

---

## 今日记录（自己填）

```
## D16 复盘
实际投入：__h
产出是否可演示：是/否 —— 链接或文件：
卡住的点（具体到技术名词）：
明天第一件事：
精力（1-5）：
```
