# Day 6｜2026-10-24 周六｜M0 数据与工具

## 今日主题：数据格式与体积（决定后面怎么选型）

**今天预算 1–1.5 小时。** 切法：5min 找回上下文 → 70min 主线 → 15min 记录。

---

## 一、今日任务（按顺序做）

1. 对比 shp / GeoJSON / TopoJSON / MVT(pbf) 的用途与体积差异
2. 理解 3D Tiles / GLTF / GLB / Draco 各自解决什么问题
3. 拿你的数据集实测：同一份数据转成 GeoJSON 和 TopoJSON，体积差多少

> 📦 **数据已下载好**：见 [`data/数据使用说明.md`](../../data/数据使用说明.md)（含按天对照表）

**用这份数据做对比**（已下载好）：
```bash
curl -o data/raw/china.json "https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json"
ls -lh data/raw/china.json                      # 看 GeoJSON 原始体积
npx topojson-server data/raw/china.json > china.topo.json
ls -lh china.topo.json                          # 对比 TopoJSON 体积
```
行政区划这种**共享边界**的数据，TopoJSON 通常能小 60%~80%——这就是你要的对比结论。
其他可选：https://www.naturalearthdata.com/downloads/（换全球数据量更大，差异更明显）
4. 写进 `docs/01-切片流程.md`，作为切片方案的铺垫

## 二、产出（必须留下，否则等于没做）

- [ ] `docs/01-切片流程.md` 补「为什么最终要切成 3D Tiles」
- [ ] 体积对比数据

> 今天不是算法日（算法固定在 **周二 / 周四 / 周日**）。

## 三、参考资料

📖 [3D Tiles 规范](https://github.com/CesiumGS/3d-tiles) 概述部分 · [glTF 规范](https://www.khronos.org/gltf/)

## 四、验收标准（怎么证明今天真做完了）

✅ 能解释「为什么不能直接加载 shp，非要切片」

---

## 今日记录（自己填）

```
## D6 复盘
实际投入：__h
产出是否可演示：是/否 —— 链接或文件：
卡住的点（具体到技术名词）：
明天第一件事：
精力（1-5）：
```
