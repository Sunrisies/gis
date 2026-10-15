# Day 50｜2026-12-07 周一｜M5 Rust/WASM

## 今日主题：Vite 构建优化

**今天预算 1–1.5 小时。** 切法：5min 找回上下文 → 70min 主线 → 15min 记录。

---

## 一、算法（40 分钟，**放在任务之前做**，趁脑子清醒）

- **新题**：[34 查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)　`二分查找` `中等`
- **新题**：[69 x 的平方根](https://leetcode.cn/problems/sqrtx/)　`二分查找` `简单`
- **复习（第 2/3 遍盲写）**：[226 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/)　`二叉树递归` `简单`

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

1. 跑一次生产构建，看产物体积
2. 用 [rollup-plugin-visualizer](https://github.com/btd/rollup-plugin-visualizer) 分析体积构成
3. Cesium 是个巨包，做拆包与懒加载
4. 对比优化前后的构建体积

## 三、产出（必须留下，否则等于没做）

- [ ] 构建优化配置
- [ ] 体积对比数据

## 四、参考资料

📖 [Vite 构建文档](https://cn.vitejs.dev/guide/build.html) · ⌨️ [rollup-plugin-visualizer](https://github.com/btd/rollup-plugin-visualizer)

## 五、验收标准（怎么证明今天真做完了）

✅ 体积有下降，且能说出降在哪

---

## 今日记录（自己填）

```
## D50 复盘
实际投入：__h
产出是否可演示：是/否 —— 链接或文件：
卡住的点（具体到技术名词）：
明天第一件事：
精力（1-5）：
```
