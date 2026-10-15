# Day 2｜2026-10-20 周二｜M0 数据与工具

## 今日主题：GDAL / ogr2ogr 命令基础

**今天预算 1–1.5 小时。** 切法：5min 找回上下文 → 70min 主线 → 15min 记录。

---

## 一、今日任务（按顺序做）

1. 搞清 shp / GeoJSON / KML 三种格式的关系与互转
2. 练熟 4 个命令：格式转换、`-t_srs` 重投影、`-clipsrc` 裁剪、`ogrinfo` 查看信息
3. 拿一份公开数据实际跑一遍转换
4. 整理成 `docs/工具命令速查.md`

### 先下数据（三条任选，**推荐第一条**）

**① 阿里云 DataV 行政区划**（免注册、直连、无需 key）
```bash
mkdir -p data/raw && cd data/raw
curl -o china.json "https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json"
curl -o zhejiang.json "https://geo.datav.aliyun.com/areas_v3/bound/330000_full.json"
```
换 `adcode` 就能拿别的省（`440000` 广东、`110000` 北京）。带 `_full` 含下级区划。

**② Natural Earth 全球底图矢量**（免注册、无版权限制）
- https://www.naturalearthdata.com/downloads/ → `Large scale (1:10m)` → `Cultural` → `Admin 0 – Countries`
- **选 shp 格式**，正好用来练 shp → GeoJSON 转换

**③ Geofabrik OSM 真实道路/建筑**（免注册）
- https://download.geofabrik.de/asia/china.html → `china-latest.osm.pbf`
- 体积大（约 2 GB），**想练手就挑个小国家**（Monaco 几十 MB）
- GDAL 原生支持读 `.pbf`：
  ```bash
  ogr2ogr -f GeoJSON -where "building IS NOT NULL" buildings.geojson china-latest.osm.pbf
  ```

> 更多数据源见 [`公开数据下载清单.md`](../../公开数据下载清单.md)

## 二、产出（必须留下，否则等于没做）

- [ ] 能跑通的命令清单（≥4 条）
- [ ] `docs/工具命令速查.md`

> 今天不是算法日（算法固定在 **周二 / 周四 / 周日**）。

## 三、参考资料

📺 B站搜「GDAL ogr2ogr 教程」· 📖 [ogr2ogr 官方](https://gdal.org/programs/ogr2ogr.html) · [OSGeo 中文](https://www.osgeo.cn/)

## 四、验收标准（怎么证明今天真做完了）

✅ 能不查资料写出「shp 转 GeoJSON 并重投影到 4326」这条命令

---

## 今日记录（自己填）

```
## D2 复盘
实际投入：__h
产出是否可演示：是/否 —— 链接或文件：
卡住的点（具体到技术名词）：
明天第一件事：
精力（1-5）：
```
