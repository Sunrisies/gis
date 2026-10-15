# Day 22｜2026-11-09 周一｜M2 页面与交互

## 今日主题：海量点渲染：PointPrimitiveCollection

**今天预算 1–1.5 小时。** 切法：5min 找回上下文 → 70min 主线 → 15min 记录。

---

## 一、算法（40 分钟，**放在任务之前做**，趁脑子清醒）

- **新题**：[3 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)　`滑动窗口` `中等`
- **复习（第 2/3 遍盲写）**：[26 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)　`双指针` `简单`

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

1. **搞清 Entity 为什么比 Primitive 慢**（这是 M3 的核心考点）
2. 用 `PointPrimitiveCollection` 渲染 10 万个点
3. 对比测试：同样 10 万点，Entity 方式 vs Primitive 方式，帧率差多少
4. 把对比结果记下来（这是项目素材）

### 10 万个点从哪来（三条任选）

**① 自己造 —— 最推荐**（点数可控、坐标系可控、秒生成）
```bash
node -e "
const fs=require('fs'), N=100000, pts=[];
for(let i=0;i<N;i++){
  pts.push([118+Math.random()*8, 28+Math.random()*8, Math.random()*500]);
}
fs.writeFileSync('data/raw/points-100k.json', JSON.stringify(pts));
console.log('生成', N, '个点');
"
```
**为什么推荐这条**：做 M3 性能对比时你需要**同样的 10 万个点反复测 5 次**，
自己造的可以固定随机种子，换机器也复现。真实数据做不到这点。

**② 真实点云**（想用真实数据就用它）
```bash
git clone https://github.com/PDAL/data.git data/raw/pdal-data
# 里面是几 MB 的 LAS/LAZ，免注册
```
转成 Cesium 能读的格式：
```bash
ogr2ogr -f GeoJSON points.geojson data/raw/pdal-data/1.2-with-color.las
```
或用 `py3dtiles convert xxx.las --out data/tiles/` 切成 `pnts`（3D Tiles 点云）

**③ Cesium ion 点云资产**（免注册额度内）
- https://ion.cesium.com/assetdepot → 找点云类资产 → Add to my assets
- 注意每月只有 10 次 Asset Depot 裁剪额度，别浪费

> 更多数据源见 [`公开数据下载清单.md`](../../公开数据下载清单.md)

## 三、产出（必须留下，否则等于没做）

- [ ] 10 万点渲染 Demo
- [ ] Entity vs Primitive 帧率对比数据

## 四、参考资料

📖 [Cesium 文档](https://cesium.com/learn/cesiumjs/ref-doc/) · ⌨️ [Scene Rendering Performance 示例](https://cesium.com/downloads/cesiumjs/releases/1.134/Apps/Sandcastle/gallery/Scene%20Rendering%20Performance.html)

## 五、验收标准（怎么证明今天真做完了）

✅ 10 万点能渲染出来
✅ 有 Entity vs Primitive 的帧率对比数字

---

## 今日记录（自己填）

```
## D22 复盘
实际投入：__h
产出是否可演示：是/否 —— 链接或文件：
卡住的点（具体到技术名词）：
明天第一件事：
精力（1-5）：
```
