# Day 38｜2026-11-25 周三｜M3 性能基线

## 今日主题：wasm-bindgen 与第一个 WASM 模块

**今天预算 1–1.5 小时。** 切法：5min 找回上下文 → 70min 主线 → 15min 记录。

---

## 一、算法（40 分钟，**放在任务之前做**，趁脑子清醒）

- **新题**：[144 二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/)　`二叉树递归` `简单`
- **新题**：[104 二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)　`二叉树递归` `简单`
- **复习（第 2/3 遍盲写）**：[438 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)　`滑动窗口+哈希` `中等`

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

1. 理解 `wasm-bindgen` 干什么（生成 JS 与 Rust 之间的胶水代码）
2. 写一个最简单的导出函数，用 `wasm-pack build` 编译
3. 在 JS 里调用它，确认能跑
4. 理解编译产物结构（.wasm / .js / .d.ts）

## 三、产出（必须留下，否则等于没做）

- [ ] 第一个可用的 WASM 模块
- [ ] 编译产物说明笔记

## 四、参考资料

📖 [Rust and WebAssembly 官方书](https://rustwasm.github.io/docs/book/) · [wasm-bindgen 指南](https://rustwasm.github.io/docs/wasm-bindgen/) · [wasm-pack](https://rustwasm.github.io/wasm-pack/)

## 五、验收标准（怎么证明今天真做完了）

✅ JS 能调用 Rust 编译出来的函数

---

## 今日记录（自己填）

```
## D38 复盘
实际投入：__h
产出是否可演示：是/否 —— 链接或文件：
卡住的点（具体到技术名词）：
明天第一件事：
精力（1-5）：
```
