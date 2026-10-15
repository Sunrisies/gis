# Day 31｜2026-11-18 周三｜M3 性能基线

## 今日主题：Mapbox GL JS 上手

**今天预算 1–1.5 小时。** 切法：5min 找回上下文 → 70min 主线 → 15min 记录。

---

## 一、算法（40 分钟，**放在任务之前做**，趁脑子清醒）

- **新题**：[203 移除链表元素](https://leetcode.cn/problems/remove-linked-list-elements/)　`链表` `简单`
- **新题**：[206 反转链表](https://leetcode.cn/problems/reverse-linked-list/)　`链表` `简单`
- **复习（第 2/3 遍盲写）**：[3 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)　`滑动窗口` `中等`

<details><summary>算法规则与 JS 五个坑（点开看）</summary>

**算法规则（重要）：**
- 每周 **3 次**（周二 / 周四 / 周日），每次 **40 分钟**，固定时间
- **同一题做 3 遍**：第 1 遍看题解 → 隔天默写 → 一周后盲写。**3 遍 1 题 > 1 遍 3 题**
- 每次 40 分钟 = **新题 25min + 旧题第 2/3 遍 15min**
- **只做简单和中等**，困难题这 63 天一律不碰
- 写题前先手打 3 个模板（数组遍历 / Map 计数 / 双指针），5 分钟练手感
- 语言就用 JS
- 总题单见 [`../总表.md`](../总表.md) 第三节

**JS 写算法题的坑（先记住，能省几小时）：**
1. `arr.sort()` 默认按**字符串字典序** —— `[10,9,1].sort()` → `[1,10,9]`，必须写 `(a,b)=>a-b`
2. `new Array(m).fill([])` 各行**共享同一引用**，要用 `Array.from({length:m},()=>[])`
3. 回溯收集结果必须 `path.slice()`，否则拿到的是同一个引用
4. `Map.get` 取不到是 `undefined`，而值本身可能是 0 —— 判断存在要用 `has()`
5. 深拷贝用 `structuredClone()`

</details>

## 二、今日任务（按顺序做）

1. 装 Mapbox GL JS，跑通官方第一个示例
2. 理解 Mapbox 的核心概念：source（数据源）和 layer（渲染层）的分离设计
3. 对比 Cesium：Mapbox 是二维地图为主，渲染模型完全不同
4. 记录两者的设计差异

## 三、产出（必须留下，否则等于没做）

- [ ] Mapbox Demo 跑通

## 四、参考资料

📖 [Mapbox GL JS 文档](https://docs.mapbox.com/mapbox-gl-js/api/) · ⌨️ [Mapbox 官方示例](https://docs.mapbox.com/mapbox-gl-js/example/) · 📺 B站搜「Mapbox GL JS 教程」

## 五、验收标准（怎么证明今天真做完了）

✅ Mapbox Demo 能跑起来

---

## 今日记录（自己填）

```
## D31 复盘
实际投入：__h
产出是否可演示：是/否 —— 链接或文件：
卡住的点（具体到技术名词）：
明天第一件事：
精力（1-5）：
```
