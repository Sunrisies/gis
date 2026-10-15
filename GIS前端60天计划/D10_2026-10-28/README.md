# Day 10｜2026-10-28 周三｜M1 切片与链路

## 今日主题：LOD 调度原理 + Cesium 静态资源坑

**今天预算 1–1.5 小时。** 切法：5min 找回上下文 → 70min 主线 → 15min 记录。

---

## 一、算法（40 分钟，**放在任务之前做**，趁脑子清醒）

- **新题**：[49 字母异位词分组](https://leetcode.cn/problems/group-anagrams/)　`哈希计数` `中等`
- **复习（第 2/3 遍盲写）**：[1 两数之和](https://leetcode.cn/problems/two-sum/)　`哈希` `简单`

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

> 📦 **样例瓦片已下载好**：`data/raw/3d-tiles-samples/`，详见 [`data/数据使用说明.md`](../../data/数据使用说明.md)

## 二、今日任务（按顺序做）

### 今天用这个（已下载好，含三级 LOD）
```
1.0/TilesetWithDiscreteLOD/
├── dragon_low.b3dm      44K   ← 最远时用
├── dragon_medium.b3dm  264K   ← 中距离
└── dragon_high.b3dm    4.3M   ← 最近时用
```
**这三个文件就是 LOD**。把相机拉远拉近，或用 `viewer.zoomTo(tileset)`，看 Network 面板里哪个 b3dm 被请求——**这就是 `geometricError` 在起作用**。

1. 理解瓦片是怎么按需加载的：相机距离 → geometricError → 加载哪一级
2. 理解「屏幕空间误差」（SSE）这个概念
3. **Cesium 静态资源坑**：Workers / Assets / ThirdParty 的路径问题，这是 Mac/Win/部署三处表现不同的经典坑
4. 把踩坑过程记进 `docs/01-切片流程.md`

## 三、产出（必须留下，否则等于没做）

- [ ] LOD 调度原理笔记
- [ ] Cesium 静态资源踩坑记录

## 四、参考资料

📖 [Cesium 官方文档](https://cesium.com/learn/cesiumjs/ref-doc/) · 📺 B站搜「Cesium 3D Tiles 原理」

## 五、验收标准（怎么证明今天真做完了）

✅ 能说清「Cesium 怎么决定加载哪一级瓦片」
✅ Cesium 静态资源在本地能正常跑

---

## 今日记录（自己填）

```
## D10 复盘
实际投入：__h
产出是否可演示：是/否 —— 链接或文件：
卡住的点（具体到技术名词）：
明天第一件事：
精力（1-5）：
```
