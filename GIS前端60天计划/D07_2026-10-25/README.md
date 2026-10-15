# Day 7｜2026-10-25 周日｜M0 数据与工具

## 今日主题：GDAL + QGIS 实战：把数据集跑通

**今天是大块日：4–6 小时。** 中途不要切任务，一鼓作气做完。

---

## 一、今日任务（按顺序做）

1. 装 QGIS（LTR 版）和 GDAL —— **Mac 上装即可**，不需要 Windows
   ```bash
   brew install --cask qgis          # QGIS LTR
   brew install gdal                 # 有 Apple Silicon 预编译包，无需编译
   gdal-config --version             # 验证
   ```
   备选（工具链更完整）：`conda create -n gis -c conda-forge python=3.12 gdal rasterio pyogrio`
2. 用 QGIS 打开一份公开 shp 数据，在「属性 → 源」里确认它的坐标系（EPSG 编号）
3. 用 ogr2ogr 转成 GeoJSON：`ogr2ogr -f GeoJSON -t_srs EPSG:4326 out.json in.shp`
4. 用 `ogrinfo -al -so in.shp` 查看原始坐标系，和转换后对比
5. 截图三张：QGIS 坐标系信息 / ogrinfo 输出 / 转换后的 GeoJSON 在 geojson.io 里的显示

### 今天要用的数据（三条任选）

**① Natural Earth shp**（**最贴合今天任务：它真的是 shp 格式，能练坐标系确认**）
- https://www.naturalearthdata.com/downloads/ → `Large scale (1:10m)` → `Cultural` → `Admin 0 – Countries`
- 下载 `ne_10m_admin_0_countries.zip`，解压后是一组 `.shp/.dbf/.shx/.prj`
- **`.prj` 文件正是你要在 QGIS「属性 → 源」里对照的东西**

**② DataV 行政区划**（免注册、直连，最快）
```bash
curl -o data/raw/china.json "https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json"
# 再转成 shp 给自己练手（反向转换）
ogr2ogr -f "ESRI Shapefile" data/raw/china_shp data/raw/china.json
```

**③ Esri 世界影像**（免注册，直接当底图，不用下载）
```js
viewer.imageryLayers.addImageryProvider(
  new Cesium.UrlTemplateImageryProvider({
    url: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
  })
)
```

> 更多数据源见 [`公开数据下载清单.md`](../../公开数据下载清单.md)

## 二、产出（必须留下，否则等于没做）

- [ ] 一份可用的 GeoJSON 数据集（M1/M2 直接用）
- [ ] `转换记录.md`
- [ ] 三张截图

> 今天不是算法日（算法固定在 **周二 / 周四 / 周日**）。

## 三、参考资料

📺 B站搜「QGIS 入门教程」「GDAL ogr2ogr 教程」· 📖 [ogr2ogr](https://gdal.org/programs/ogr2ogr.html) · [QGIS](https://qgis.org/) · 📄 [公开数据下载清单](../../公开数据下载清单.md)

## 四、验收标准（怎么证明今天真做完了）

✅ 能说出这份数据原本是什么坐标系
✅ 转换后的 GeoJSON 在 geojson.io 能显示
✅ 有截图和转换记录

---

## 今日记录（自己填）

```
## D7 复盘
实际投入：__h
产出是否可演示：是/否 —— 链接或文件：
卡住的点（具体到技术名词）：
明天第一件事：
精力（1-5）：
```

## 周日专属：拷问三问（录音回答，20 分钟）

> 一个人做项目最大的风险是**自己骗自己**。每周日回答这三个问题并录音：

1. 这一周我做了什么？（**不许说「学习了 X」，只能说「做出了 Y」**）
2. 这个 Y 怎么验证它能用？证据在哪？
3. 如果被追问三层，我哪一层会卡住？

**第 3 个问题卡住的地方，就是下周的第一个任务。**
