# Day 12｜2026-10-30 周五｜M1 切片与链路

## 今日主题：Cesium 快速上手：把你的瓦片加载进去

**今天预算 1–1.5 小时。** 切法：5min 找回上下文 → 70min 主线 → 15min 记录。

---

## 一、算法（40 分钟，**放在任务之前做**，趁脑子清醒）

- **新题**：[26 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)　`双指针` `简单`
- **复习（第 2/3 遍盲写）**：[217 存在重复元素](https://leetcode.cn/problems/contains-duplicate/)　`哈希` `简单`

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

### 今天加载这个（已下载好）
```bash
cd data/raw && python3 -m http.server 8080
# 浏览器验证 http://localhost:8080/3d-tiles-samples/TilesetWithDiscreteLOD/tileset.json
```
```js
const tileset = await Cesium.Cesium3DTileset.fromUrl(
  'http://localhost:8080/3d-tiles-samples/TilesetWithDiscreteLOD/tileset.json'
)
viewer.scene.primitives.add(tileset)
viewer.zoomTo(tileset)
```
⚠️ **必须走 http，不能 `file://`**（CORS 会拦死，这是最高频的坑）

1. 在 Mac 上装 nginx（或写一个极简 Node 静态服务）
2. 把 Windows 切好的 3D Tiles 拷过来，用本地服务发布
3. 用 Cesium 加载：`Cesium3DTileset.fromUrl(...)` 然后 `viewer.scene.primitives.add(...)`
4. **打开 Network 面板，确认 `tileset.json` 返回 200**（这是 M1 验收的硬指标）

## 三、产出（必须留下，否则等于没做）

- [ ] 本地瓦片服务跑起来
- [ ] Cesium 页面能加载 3D Tiles

## 四、参考资料

📖 [CesiumJS 文档](https://cesium.com/learn/cesiumjs/ref-doc/) · ⌨️ [Sandcastle 示例库](https://sandcastle.cesium.com/)

## 五、验收标准（怎么证明今天真做完了）

✅ Network 面板里 `tileset.json` 是 200
✅ 三维模型可见且不糊

---

## 今日记录（自己填）

```
## D12 复盘
实际投入：__h
产出是否可演示：是/否 —— 链接或文件：
卡住的点（具体到技术名词）：
明天第一件事：
精力（1-5）：
```
