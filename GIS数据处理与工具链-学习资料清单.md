# GIS 数据处理与工具链 · 学习资料清单（面向 GIS 前端 / Vue3 + Cesium 背景 / Mac 主力机 + Windows 切片机）

> 核验说明：以下所有 `https://` 与 `http://` 链接均在 2026 年本次整理时逐条发起 HTTP 请求核验（含跟随重定向后的最终地址）。少量域名因本机网络出口被拦截/被 Cloudflare 人机校验拦截（返回 429、连接重置或无响应），已在该条目后明确标注「本次未直连核验」，请以浏览器实测为准；这些条目均来自官方站点搜索结果，非编造 URL。

---

## 1. GDAL / ogr2ogr

- [GDAL 官网](https://gdal.org/) —— GDAL/OGR 官方门户，包含栅格（GDAL）与矢量（OGR）全部驱动列表、命令行工具索引和 API 文档，是最权威的第一手资料（标签：官方 | 优先级 P0）。**注：本次访问被 Cloudflare 人机校验拦截（HTTP 429），域名与页面真实存在，浏览器可正常打开。**
- [ogr2ogr 官方手册](https://gdal.org/en/stable/programs/ogr2ogr.html) —— 矢量格式转换、重投影（`-t_srs`）、裁剪（`-clipsrc`）、属性过滤（`-where`/`-sql`）的全部参数说明，是你最常查的一页（标签：官方 | 优先级 P0）。**注：同上，本次未直连核验。**
- [ogr2ogr manpage（Debian 镜像，已核验可直连）](https://manpages.debian.org/testing/gdal-bin/ogr2ogr.1.en.html) —— 上面官方手册的纯文本替代镜像，已确认包含 `-of/-f <format_name>`、`-t_srs`、`-s_srs`、`-clipsrc [-clipdst]`、`-lco` 等关键参数，查命令比官网更快（标签：官方 | 优先级 P0）。
- [gdalwarp manpage（Debian 镜像）](https://manpages.debian.org/testing/gdal-bin/gdalwarp.1.en.html) —— 栅格影像重投影/裁剪工具 `gdalwarp` 的参数说明，做影像切片前必须掌握的一步（标签：官方 | 优先级 P0）。
- [gdal_translate manpage（Debian 镜像）](https://manpages.debian.org/testing/gdal-bin/gdal_translate.1.en.html) —— 栅格格式互转、波段抽取、生成 COG/瓦片金字塔（`-co TILED=YES`）的入口工具（标签：官方 | 优先级 P0）。
- [gdal2tiles manpage（Debian 镜像）](https://manpages.debian.org/testing/gdal-bin/gdal2tiles.1.en.html) —— 把 GeoTIFF 切成 TMS/XYZ 影像瓦片的官方工具参数，第 3 节影像切片方案的核心命令（标签：官方 | 优先级 P0）。
- [GMT 中文手册 · GDAL 章节](https://docs.gmt-china.org/6.3/utilities/gdal/) —— **已核验可直连的高质量中文资料**：用中文解释 GDAL 与 OGR 的分工、支持的栅格/矢量格式，并演示 `ogr2ogr` 的典型用法，是零基础最快建立概念的一篇（标签：教程 | 优先级 P0）。
- [GDAL Cheat Sheet（GitHub，★1.2k）](https://github.com/dwtkns/gdal-cheat-sheet) —— 英文但极简的常用命令速查表，覆盖格式转换、重投影、裁剪、按属性筛选，适合贴在编辑器旁边（标签：教程 | 优先级 P0）。
- [OSGeo/gdal 源码仓库（GitHub，★6.1k）](https://github.com/OSGeo/gdal) —— 提 issue、查驱动实现、看 CHANGELOG 的地方；顺手可以看 `doc/` 目录下的文档源码（标签：官方 | 优先级 P1）。
- [GDAL 二进制包下载汇总（OSGeo Trac）](https://trac.osgeo.org/gdal/wiki/DownloadingGdalBinaries) —— 各平台安装方式汇总（Homebrew / conda / OSGeo4W / Docker），Mac 与 Windows 装 GDAL 先看这里（标签：官方 | 优先级 P0）。
- [GDAL Releases（GitHub）](https://github.com/OSGeo/gdal/releases) —— 官方发布页，查版本号与变更；排查「conda 装的 GDAL 版本和 brew 不一致」时用得上（标签：官方 | 优先级 P2）。

**最小命令速查（先照着敲通一遍再扩展）**

```bash
# shp -> GeoJSON（注意 -lco ENCODING=UTF-8 解决中文属性乱码）
ogr2ogr -f GeoJSON -lco ENCODING=UTF-8 out.geojson in.shp

# GeoJSON -> shp（-nlt POLYGON 指定几何类型，避免 MultiPolygon 报错）
ogr2ogr -f "ESRI Shapefile" -nlt POLYGON out_dir in.geojson

# KML -> GeoJSON
ogr2ogr -f GeoJSON out.geojson in.kml

# 重投影：源坐标系 WGS84 -> CGCS2000，或 -> Web Mercator
ogr2ogr -f GeoJSON -s_srs EPSG:4326 -t_srs EPSG:4490 out.geojson in.shp
ogr2ogr -f GeoJSON -t_srs EPSG:3857 out.geojson in.shp     # 只给 -t_srs，源坐标系自动识别

# 按范围裁剪（bbox 或裁到一个 shp/GeoJSON 图层）
ogr2ogr -f GeoJSON -clipsrc 116.0 39.5 116.8 40.2 out.geojson in.shp
ogr2ogr -f GeoJSON -clipsrc clip_area.geojson out.geojson in.shp

# 查看数据信息（坐标系、要素数、字段）
ogrinfo -so -al in.shp
gdalinfo in.tif
```

---

## 2. QGIS

- [QGIS 官网](https://qgis.org/) —— 项目主页、新闻与下载入口；Mac 装 QGIS 建议直接用官方 `.dmg`（标签：官方 | 优先级 P0）。
- [QGIS 下载页](https://qgis.org/download/) —— 区分 LTR（长期支持版）与 Latest（尝鲜版），初学一律选 LTR；页面同时给出 macOS / Windows / Linux 的安装包（标签：官方 | 优先级 P0）。
- [QGIS 官方安装指南](https://qgis.org/resources/installation-guide/) —— 按操作系统分节的安装说明，含 macOS 的 `.dmg` 与 Homebrew 两种装法与首次启动的权限提示（标签：官方 | 优先级 P0）。
- [QGIS 官方文档 · 简体中文（3.44）](https://docs.qgis.org/3.44/zh-Hans/docs/index.html) —— **官方简体中文文档总入口（已核验可直连）**，注意新版中文的路径是 `zh-Hans`（带连字符），不是 `zh_Hans`（用下划线会被重定向到英文版）（标签：官方 | 优先级 P0）。
- [QGIS 中文文档 · 打开数据](https://docs.qgis.org/3.44/zh-Hans/docs/user_manual/managing_data_source/opening_data.html) —— 怎么把 shp/GeoJSON/GeoTIFF/CSV 拖进 QGIS、图层坐标系不匹配时会发生什么（标签：官方 | 优先级 P0）。
- [QGIS 中文文档 · 使用投影](https://docs.qgis.org/3.44/zh-Hans/docs/user_manual/working_with_projections/working_with_projections.html) —— **重点章节**：项目坐标系与图层坐标系的关系、如何查看某个图层的 CRS、如何用「另存为」导出成目标坐标系（等价于 GUI 版 `ogr2ogr -t_srs`）（标签：官方 | 优先级 P0）。
- [QGIS 中文文档 · 矢量数据属性与导出](https://docs.qgis.org/3.44/zh-Hans/docs/user_manual/working_with_vector/vector_properties.html) —— 导出 GeoJSON/shp 时的图层选项、编码设置（中文属性乱码就在这里改）（标签：官方 | 优先级 P1）。
- [QGIS 中文文档 · 插件机制](https://docs.qgis.org/3.44/zh-Hans/docs/user_manual/plugins/plugins.html) —— 插件安装与管理、插件仓库入口、离线安装 `.zip` 的方法（内网机器很有用）（标签：官方 | 优先级 P1）。
- [QGIS 官方插件仓库](https://plugins.qgis.org/) —— 按下载量/评分检索插件，插件文档与主页链接都挂在这里（标签：工具 | 优先级 P1）。
- [QuickMapServices 插件](https://plugins.qgis.org/plugins/QuickMapServices/) —— 一键接入 Google/OSM/Bing 等底图作为参考图层，用来肉眼比对「你的数据到底偏没偏」（标签：工具 | 优先级 P0）。
- [MMQGIS 插件](https://plugins.qgis.org/plugins/mmqgis/) —— 老牌批量处理插件：批量格式转换、批量裁剪、按属性分图层导出，适合把手工操作变成批处理（标签：工具 | 优先级 P1）。
- [QMetaTiles 插件](https://plugins.qgis.org/plugins/QMetaTiles/) —— 在 QGIS 内按范围下载 XYZ 在线瓦片或导出本地 XYZ 瓦片目录，做离线底图很实用（标签：工具 | 优先级 P1）。
- [qgis2web 插件](https://plugins.qgis.org/plugins/qgis2web/) —— 把 QGIS 工程直接导出为 Leaflet/OpenLayers 网页地图，快速验证数据是否可用（标签：工具 | 优先级 P2）。
- [QGIS 源码仓库（GitHub，★14.6k）](https://github.com/qgis/QGIS) —— 遇到诡异 bug 时查 issue 与版本修复记录（标签：官方 | 优先级 P2）。

---

## 3. 切片工具链

### 3.1 切片工具怎么选（**不要用 CesiumLab**）

> **为什么不推荐 CesiumLab**：闭源商业软件，免费版有功能/水印限制，输出格式与参数不透明。
> 更要紧的是——**面试时讲不清楚「切片内部怎么算的」**，因为你只是点了几个按钮。
> 下面全是**开源、命令行、可复现**的方案，切片参数你能逐条解释。

**按数据类型的方案对照**：

| 数据类型 | 用什么 | 平台 | 说明 |
|---|---|---|---|
| OSGB 倾斜摄影 → 3D Tiles | `fanvanzh/3dtiles` | **Mac + Win + Docker** | 开源，支持 OSGB/SHP/FBX |
| shp 建筑白模 → 3D Tiles | `fanvanzh/3dtiles` | **Mac + Win** | 带高度字段挤压成白模 |
| 点云 LAS/LAZ → 3D Tiles | `py3dtiles` | **Mac（纯 Python）** | 无需编译 |
| 影像 GeoTIFF → XYZ 瓦片 | `gdal2tiles` | **Mac + Win** | GDAL 自带 |
| DEM → Cesium 地形瓦片 | `cesium-terrain-builder` | Docker | 或 `tin-terrain` |
| 矢量 GeoJSON → MVT | `tippecanoe` | Mac + Win | 矢量瓦片事实标准 |
| 模型 OBJ/glTF 优化 | `gltf-pipeline` | **Mac + Win** | Draco 压缩 |

**关键点：Mac 上这条链路是通的。** 唯一需要 Windows 的场景是大批量倾斜摄影切片（数据量大、原厂工具链在 Windows），但如果只用公开示例数据或点云，**全程在 Mac 上就能完成**。

### 3.2 命令行 / 跨平台切片工具

- [fanvanzh/3dtiles（GitHub，★2.3k）](https://github.com/fanvanzh/3dtiles) —— **本项目的切片主力**：开源 3D Tiles 转换工具集，支持 **OSGB → 3D Tiles、Shapefile → 3D Tiles、FBX → 3D Tiles**，明确支持 macOS（Intel 与 Apple Silicon）和 Windows，提供 Windows 预编译包与 Docker 镜像（标签：工具 | 优先级 P0）。
- [fanvanzh/3dtiles 中文说明（README_ZH）](https://github.com/fanvanzh/3dtiles/blob/master/README_ZH.md) —— 中文功能列表、各平台编译步骤与使用说明（标签：教程 | 优先级 P0）。
- [CesiumGS/3d-tiles-tools（GitHub，★539）](https://github.com/CesiumGS/3d-tiles-tools) —— Cesium 官方 Node 工具链：`gzip/ungzip`（瓦片 gzip 化）、`glbToB3dm`、`glbToI3dm`、`createTilesetJson`、`optimize`、`upgrade`（1.0 → 1.1）、`analyze`、坐标转换等；`npm install 3d-tiles-tools` 即可用，`engines: node >=18`（标签：官方 | 优先级 P0）。
- [CesiumGS/3d-tiles-validator（GitHub，★476）](https://github.com/CesiumGS/3d-tiles-validator) —— **切片产出后必跑**的校验器，能在浏览器打开前发现 tileset.json 与瓦片二进制的结构错误，省掉大量「Cesium 里一片空白但控制台没报错」的排查时间（标签：官方 | 优先级 P0）。
- [py3dtiles 官方仓库（GitLab，已迁移）](https://gitlab.com/py3dtiles/py3dtiles) —— Python 库/命令行，做 **LAS/XYZ 点云 → 3D Tiles（pnts）**、点云 tileset 合并与内容读取。**主仓库已从 GitHub 迁到 GitLab**，别再照着旧 GitHub README 装（标签：官方 | 优先级 P0）。
- [py3dtiles on PyPI](https://pypi.org/project/py3dtiles/) —— 产物是 `py3-none-any.whl`（纯 Python 轮子），**Apple Silicon 上 `pip install py3dtiles` 无需编译**，Mac 可用（标签：官方 | 优先级 P0）。
- [PrincessGod/objTo3d-tiles（GitHub，★841）](https://github.com/PrincessGod/objTo3d-tiles) —— 把 OBJ 模型批量化转为 3D Tiles（b3dm），用于建筑白模、手工模型批量入库（标签：工具 | 优先级 P1）。
- [OpenDroneMap/ODM（GitHub，★6.5k）](https://github.com/OpenDroneMap/ODM) —— 无人机照片 → 点云/正射/三维模型的开源摄影测量流水线，需要「自己造倾斜摄影数据」练习时用它（标签：工具 | 优先级 P2）。

### 3.3 倾斜摄影 OSGB → 3D Tiles 的通用流程

- [OSGB → 3D Tiles 流程说明（mars3d 文档）](http://mars3d.cn/docs/data/osgb-tileset/) —— 中文分步流程（标签：教程 | 优先级 P0）。**注：本次未直连核验。**
- [fanvanzh/3dtiles 中文 README](https://github.com/fanvanzh/3dtiles/blob/master/README_ZH.md) —— 命令行版流程与参数（标签：教程 | 优先级 P0）。

**流程要点（综合以上两份资料）**：OSGB 数据必须是「`Data` 目录的上一级」作为输入根目录，且同级需有 `metadata.xml`；输入坐标系通常由 `metadata.xml` 中的 `SRS` 决定；切片时选择 **空间参考（如 EPSG:4326 或 4490）、最大层级、几何误差/瓦片大小、是否生成 LOD 与纹理压缩**；输出目录里必须同时存在 `tileset.json` 与 `*.b3dm/*.i3dm/*.pnts` 与纹理目录，缺一不可；切完先用 3d-tiles-validator 校验，再起本地 HTTP 服务（不能 `file://` 直接打开）加载。

### 3.4 影像 / 地形 / 矢量瓦片切片方案

- [gdal2tiles 手册（Debian 镜像）](https://manpages.debian.org/testing/gdal-bin/gdal2tiles.1.en.html) —— 影像 → XYZ/TMS 瓦片的标准方案，支持 `-p raster/mercator/geodetic`、`-z` 指定层级、`--xyz` 生成前端通用的 XYZ 目录结构（标签：官方 | 优先级 P0）。
- [maptiler/tileserver-gl（GitHub，★2.9k）](https://github.com/maptiler/tileserver-gl) —— 一条命令把 `.mbtiles` 发布成 XYZ/WMTS 服务，自带预览页面，本地开发与内网部署都极省事（标签：工具 | 优先级 P0）。
- [consbio/mbtileserver（GitHub，★794）](https://github.com/consbio/mbtileserver) —— 纯 Go 单文件二进制，把 mbtiles 目录发布为瓦片服务，内网离线部署时不用装 Node（标签：工具 | 优先级 P1）。
- [mapbox/tippecanoe（GitHub，★3.1k）](https://github.com/mapbox/tippecanoe) —— **矢量**瓦片（MVT/pbf）生产事实标准：GeoJSON → mbtiles，自动处理简化、抽稀、属性裁剪（标签：工具 | 优先级 P0）。
- [developmentseed/titiler（GitHub，★1.2k）](https://github.com/developmentseed/titiler) —— 从 COG（Cloud Optimized GeoTIFF）**动态**出 XYZ 瓦片，免去预先切全量瓦片，适合数据会频繁更新的场景（标签：工具 | 优先级 P1）。
- [CesiumGS/quantized-mesh（GitHub）](https://github.com/CesiumGS/quantized-mesh) —— Cesium 地形瓦片（quantized-mesh 1.0）格式规范，理解地形切片产物到底是什么（标签：官方 | 优先级 P1）。
- [ahuarte47/cesium-terrain-builder（GitHub，★275）](https://github.com/ahuarte47/cesium-terrain-builder) —— 把 DEM（GeoTIFF）切成 Cesium 可用的地形瓦片，原版 `geo-data/cesium-terrain-builder` 的活跃分支（标签：工具 | 优先级 P1）。
- [tum-gis/cesium-terrain-builder-docker（GitHub，★270）](https://github.com/tum-gis/cesium-terrain-builder-docker) —— 上面工具的 Docker 封装，避免在 Mac 上手工编 CTB（标签：工具 | 优先级 P1）。
- [heremaps/tin-terrain（GitHub，★612）](https://github.com/heremaps/tin-terrain) —— DEM → Terrain RGB / Terrarium 地形瓦片（Mapbox 风格），做三维地形底图时用（标签：工具 | 优先级 P2）。
- [Cesium 官方教程 · 地形](https://cesium.com/learn/cesiumjs-learn/cesiumjs-terrain/) —— 讲清 Cesium 地形服务怎么接、地形夸张系数、本地地形服务如何加载（标签：官方 | 优先级 P0）。
- [CesiumGS/obj2gltf（GitHub，★1.9k）](https://github.com/CesiumGS/obj2gltf) —— OBJ → glTF/GLB 官方转换器，3D Tiles 前的模型预处理（标签：官方 | 优先级 P1）。
- [CesiumGS/gltf-pipeline（GitHub，★2.1k）](https://github.com/CesiumGS/gltf-pipeline) —— glTF 优化：Draco 压缩、纹理压缩、去除冗余，直接决定 3D Tiles 的最终体积（标签：官方 | 优先级 P0）。

---

## 4. 公开数据集（务实可用，含注册与免费额度说明）

### 4.1 Cesium ion（免费额度 + 示例资产）

- [Cesium ion 平台主页](https://cesium.com/platform/cesium-ion/) —— 官方在线切片与资产托管平台，注册免费账号即可上传数据在线切片（标签：官方 | 优先级 P0）。
- [Cesium ion 定价与免费额度（已核验页面内容）](https://cesium.com/platform/cesium-ion/pricing/) —— **Community 免费版（个人非商用）额度：存储 10 GB、每月流量 15 GB、每月实景建模 20 gigapixels、每月实景分析 5 小时、全球影像 1,000 sessions/月、Google Photorealistic 3D Tiles 1,000 root tiles/月、地理编码 50,000/月、Asset Depot 数据裁剪 10 次/月**；Commercial 版 $149/月起（存储 100 GB、流量 150 GB/月）（标签：官方 | 优先级 P0）。
- [Cesium ion Asset Depot（可直接领取的免费资产）](https://ion.cesium.com/assetdepot) —— 登录后在这里把官方与合作伙伴的免费数据集「加到自己账户」，是零成本拿到真实 3D Tiles 的最快路径（标签：官方 | 优先级 P0）。
- [Cesium ion 精选 3D 内容总览](https://cesium.com/platform/cesium-ion/content/) —— 列出可用的全球资产：Cesium World Terrain、Cesium World Bathymetry、Cesium Moon / Mars、**Cesium OSM Buildings（全球建筑白模，非常实用的免费城市模型）**、Japan 3D Buildings、Sentinel-2 影像，以及合作伙伴的 Bing Maps 影像、Google Photorealistic 3D Tiles、Vexcel 3D Cities（标签：官方 | 优先级 P0）。
- [Cesium World Terrain 说明](https://cesium.com/platform/cesium-ion/content/cesium-world-terrain/) —— 全球高精度 3D 地形（最高约 1 米精度），免费账号可直接接入；也可把自己的 DEM 传上去合并（标签：官方 | 优先级 P0）。
- [Aerometrex 旧金山倾斜摄影数据免费开放（官方博客）](https://cesium.com/blog/2022/12/13/aerometrex-san-francisco-data-now-available-on-cesium/) —— **只要有免费 Cesium ion 账号，就能在 Asset Depot 免费领取旧金山、丹佛等城市的高精度倾斜摄影 3D Tiles**，这是免费「真实倾斜摄影数据」最靠谱的来源（标签：官方 | 优先级 P0）。
- [Cesium 官方教程 · Photorealistic 3D Tiles（Google 真实感三维城市）](https://cesium.com/learn/photorealistic-3d-tiles-learn/) —— 免费账号每月 1,000 root tiles，做效果演示够用（标签：官方 | 优先级 P1）。

### 4.2 3D Tiles / glTF 示例数据仓库（免注册，直接 git clone）

- [CesiumGS/3d-tiles-samples（GitHub，★347）](https://github.com/CesiumGS/3d-tiles-samples) —— **官方示例瓦片集**，覆盖 3D Tiles 1.0 与 1.1，含 LOD、request volume、billboard、点云、glTF 集成等最小可运行样例，是理解 tileset.json 结构的最佳素材（标签：官方 | 优先级 P0）。
- [CesiumJS 内置 SampleData](https://github.com/CesiumGS/cesium/tree/main/Apps/SampleData) —— CesiumJS 仓库自带的模型与瓦片（含 `CesiumMilkTruck`、`Dragon` 等 glTF，以及 3D Tiles 示例），clone 下来就能加载（标签：官方 | 优先级 P0）。
- [bertt/cesium_3dtiles_samples（GitHub，★58）](https://github.com/bertt/cesium_3dtiles_samples) —— 社区整理的各类 3D Tiles 样例（含点云、BIM、地形），补充官方样例之外的边界情况（标签：教程 | 优先级 P1）。
- [Cesium 官方教程 · Data Formats](https://cesium.com/learn/data-formats/) —— 官方对 3D Tiles、glTF、点云、地形等格式的支持矩阵与推荐转换路径，选数据前先看它（标签：官方 | 优先级 P0）。

### 4.3 点云数据

- [OpenTopography 数据门户](https://portal.opentopography.org/) —— 全球 LiDAR 点云与 DEM 的主要免费分发平台，**需要免费注册**，部分数据集（如 SRTM、NASADEM）登录后可直接下载，LiDAR 大范围数据需要提交申请（标签：工具 | 优先级 P0）。
- [PDAL/data（GitHub）](https://github.com/PDAL/data) —— PDAL 官方测试数据仓库，含大量小体积 LAS/LAZ（几 MB 级），**免注册、可直接下载**，非常适合在 Mac 上快速跑通「LAS → 3D Tiles」链路（标签：工具 | 优先级 P0）。
- [USGS 3DEP LiDAR 下载（The National Map）](https://apps.nationalmap.gov/downloader/) —— 美国本土 LiDAR 点云与 DEM 官方下载器，**免注册、按框选下载**，LAZ 分幅数据，做点云切片练习量足够（标签：官方 | 优先级 P1）。
- [SRTM GL3 全球 90m 数据说明（Data.gov）](https://catalog.data.gov/dataset/shuttle-radar-topography-mission-srtm-gl3-global-90m) —— SRTM 90m DEM 的官方元数据与下载入口说明，全球覆盖、免注册（标签：官方 | 优先级 P1）。

### 4.4 DEM 高程数据

- [USGS EarthExplorer](https://earthexplorer.usgs.gov/) —— SRTM、ASTER、3DEP、Landsat 等海量数据的统一检索下载器，**需免费注册**；按「多边形/坐标框」检索 SRTM 1arcsec 的最常用入口（标签：官方 | 优先级 P0）。
- [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) —— 欧空局哥白尼数据（含 **Copernicus DEM GLO-30/GLO-90**，全球 30m/90m），**免费注册**，30m 全球 DEM 目前质量与覆盖最好的免费选项之一（标签：官方 | 优先级 P0）。
- [ASTER GDEM 官方页（NASA/JAXA）](https://asterweb.jpl.nasa.gov/gdem.asp) —— 全球 30m DEM，**需免费注册 Earthdata 账号**下载；比 SRTM 覆盖更靠极地但噪声更多（标签：官方 | 优先级 P1）。
- [ALOS World 3D 30m（AW3D30，JAXA）](https://www.eorc.jaxa.jp/ALOS/en/aw3d30/index.htm) —— 日本 JAXA 全球 30m DSM，**免费注册**后按图幅下载，中国区域质量优于 ASTER（标签：官方 | 优先级 P1）。
- [国家对地观测科学数据中心 · DEM 专题](https://data.casearth.cn/thematic/dem/448) —— 国内可访问的 DEM 数据专题，部分数据 **免登录 FTP 下载**，是中国区域高程数据的国内来源（标签：官方 | 优先级 P0）。
- [地理空间数据云（GSCloud，中科院）](https://www.gscloud.cn/) —— 国内最常用的免费遥感/DEM 下载站（含 SRTM、Landsat、MODIS），**需手机号注册**，国内下载速度快（标签：工具 | 优先级 P0）。**注：本次未直连核验（连接被重置），请在浏览器实测。**
- [资源环境科学数据中心（RESDC）](https://www.resdc.cn/) —— 中科院地理所，提供中国行政区划、人口、土地利用等矢量数据，**需注册**（标签：工具 | 优先级 P1）。**注：本次未直连核验。**

### 4.5 倾斜摄影 / 城市三维模型

- [Cesium ion Asset Depot](https://ion.cesium.com/assetdepot) —— 免费领取 Aerometrex 旧金山/丹佛倾斜摄影 3D Tiles（见 4.1），**这是最省事的免费倾斜摄影数据**（标签：官方 | 优先级 P0）。
- [3D BAG（荷兰）](https://3dbag.nl/en/viewer) —— 荷兰全国 3D 建筑模型，**CC BY 4.0 免费下载**（CityJSON/OBJ），可转 glTF/3D Tiles，是免费的「真实城市三维模型」（标签：工具 | 优先级 P1）。
- [Berlin 3D Download Portal（柏林）](https://www.businesslocationcenter.de/berlin3d-downloadportal/) —— 柏林官方三维城市模型下载（含 LOD1/LOD2 的 CityGML、以及倾斜摄影网格模型），**免费**，需在页面选择区块下载（标签：官方 | 优先级 P1）。
- [OpenCityModel（GitHub）](https://github.com/OpenCityModel/OpenCityModel) —— 开放城市建筑体块数据集与工具链，适合批量生成白模瓦片（标签：工具 | 优先级 P2）。
- [Cesium OSM Buildings（ion 内容页）](https://cesium.com/platform/cesium-ion/content/) —— 全球建筑白模 3D Tiles，免费账号直接接入，无需自己切片（标签：官方 | 优先级 P0）。
- [OpenStreetMap 官方数据下载](https://www.openstreetmap.org/) —— 建筑轮廓来源；结合高度字段可自造白模（标签：官方 | 优先级 P1）。

### 4.6 GeoJSON 行政区划数据

- [DataV.GeoAtlas 直连 GeoJSON 接口（已核验返回 200，582 KB，35 个省级要素）](https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json) —— 阿里云 DataV 行政区划边界，**免注册、无需 key、直连 JSON**；把 `100000` 换成省/市 `adcode` 即可拿下级边界，带 `_full` 后缀会包含下级区划；要素属性含 `adcode/name/center/centroid/childrenNum/level`（标签：官方 | 优先级 P0）。
- [DataV.GeoAtlas 可视化选择器（网页版）](https://datav.aliyun.com/portal/school/atlas/area_selector) —— 点选省市区后可视化预览并复制下载链接，配合上面的直连接口使用（标签：官方 | 优先级 P0）。**注：本次未直连核验（连接被重置）。**
- [modood/Administrative-divisions-of-China（GitHub，★21.0k）](https://github.com/modood/Administrative-divisions-of-China) —— 中国省市区街道四级行政区划数据（JSON/CSV/SQL），**免注册**，做「名称 ↔ adcode ↔ 层级」映射时比抓边界更实用（标签：工具 | 优先级 P0）。
- [longwosion/geojson-map-china（GitHub）](https://github.com/longwosion/geojson-map-china) —— 中国各级行政区划 GeoJSON 归档仓库，含省/市/县多级文件，**免注册、git clone 即用**（标签：工具 | 优先级 P1）。
- [xiangyuecn/AreaCity-JsSpider-StatsGov（GitHub）](https://github.com/xiangyuecn/AreaCity-JsSpider-StatsGov) —— 国家统计局行政区划 + 边界数据抓取与转换工具，可自行生成最新 GeoJSON（标签：工具 | 优先级 P2）。
- [geojson.cn · 中国地图数据集](https://geojson.cn/data/atlas/china) —— 中文站点，提供中国及各省市区县 GeoJSON 打包下载与「天地图标准矢量」等数据集说明（标签：工具 | 优先级 P1）。**注：本次未直连核验。**
- [Natural Earth 数据下载](https://www.naturalearthdata.com/downloads/) —— 全球国界、海岸线、河流、城市点等矢量数据，**免注册、无版权限制**，做底图与投影验证的标准素材（标签：官方 | 优先级 P0）。
- [Geofabrik · 中国 OSM 提取](https://download.geofabrik.de/asia/china.html) —— 免注册下载中国 `china-latest.osm.pbf`（约 2 GB 级），再用 tippecanoe/osmium 加工成建筑、道路数据（标签：工具 | 优先级 P1）。

---

## 5. 坐标系与国内偏移

- [EPSG:4490 · CGCS2000 官方条目](https://epsg.io/4490) —— 已核验页面标题为「China Geodetic Coordinate System 2000 - EPSG:4490」，给出 CGCS2000 的 WKT、PROJ 定义与 `proj4js` 字符串，转投影时直接抄这里（标签：官方 | 优先级 P0）。
- [EPSG:4326 · WGS84](https://epsg.io/4326) —— 最常见的经纬度坐标系，GPS 原始输出与 GeoJSON 规范都基于它（标签：官方 | 优先级 P0）。
- [EPSG:3857 · Web Mercator](https://epsg.io/3857) —— 所有网页地图瓦片（XYZ/TMS）使用的投影，前端加载瓦片时瓦片索引就是它（标签：官方 | 优先级 P0）。
- [spatialreference.org · EPSG:4490](https://spatialreference.org/ref/epsg/4490/) —— 另一个坐标系定义查询站，提供 proj4、WKT、ESRI WKT 等多种格式（标签：工具 | 优先级 P1）。
- [OSGeo Wiki · China datums](https://wiki.osgeo.org/wiki/China_datums) —— 英文但权威，梳理 WGS84 / CGCS2000 / Beijing 1954 / Xian 1980 以及 GCJ-02 的关系与差异量级（标签：官方 | 优先级 P0）。
- [Wikipedia · Restrictions on geographic data in China](https://en.wikipedia.org/wiki/Restrictions_on_geographic_data_in_China) —— 解释 GCJ-02（火星坐标）、BD-09 的由来、法规背景与偏移机制，理解「为什么必须纠偏」的权威入门（标签：教程 | 优先级 P0）。
- [proj4js 官网](https://proj4js.org/) —— **前端做严格投影变换（EPSG 间转换）的首选库**，支持自定义 proj4 字符串、`transform()` API，Vue 项目直接用（标签：官方 | 优先级 P0）。
- [proj4js/proj4js（GitHub，★2.2k）](https://github.com/proj4js/proj4js) —— 源码、issue 与更新记录；注意它**不做 GCJ-02 纠偏**（GCJ-02 不是标准投影），纠偏要用 gcoord/coordtransform（标签：官方 | 优先级 P0）。
- [hujiulong/gcoord（GitHub，★3.3k）](https://github.com/hujiulong/gcoord) —— **中文开发者最常选用的坐标系转换库**，支持 WGS84 / GCJ-02 / BD-09 / Web Mercator 等互转，**可直接传入 GeoJSON 对象**批量转换，浏览器构建仅约 3 KB gzip，无运行时依赖，Vue3 项目开箱即用（标签：工具 | 优先级 P0）。
- [gcoord Wiki · 地理坐标系（中文）](https://github.com/hujiulong/gcoord/wiki/地理坐标系) —— 用中文把「地理坐标 vs 投影坐标、各家地图用的到底是哪套坐标系」讲清楚了，前端背景的人看这一篇就够建立心智模型（标签：教程 | 优先级 P0）。
- [wandergis/coordtransform（GitHub，★4.7k）](https://github.com/wandergis/coordtransform) —— 极简的 WGS84 / GCJ-02 / BD-09 互转模块，README 中文；另有配套的 **CLI 版本可直接转换 GeoJSON 文件**（[coordtransform-cli](https://github.com/wandergis/coordtransform-cli)）与 Python 版本，做数据批处理时很顺手（标签：工具 | 优先级 P1）。
- [googollee/eviltransform（GitHub，★2.6k）](https://github.com/googollee/eviltransform) —— 多语言（JS/Go/C/Python）实现的 GCJ-02 ⇄ WGS84 转换，代码短到可以逐行读懂算法本身，适合搞清「纠偏到底怎么算的」（标签：教程 | 优先级 P1）。
- [掘金 · 中国地图坐标系转换实践](https://juejin.cn/post/7607097714300076042) —— 中文实战文章，围绕国内地图坐标系转换的真实痛点与实现（标签：教程 | 优先级 P1）。
- [网易 · 同一个坐标，谷歌、高德、百度地图却指向三个地方](https://www.163.com/dy/article/ECGIV6CR051196HN.html) —— 中文科普，直观感受 GCJ-02/BD-09 偏移的直观后果（标签：教程 | 优先级 P2）。

**关键结论速记**：WGS84 与 CGCS2000（EPSG:4490）在米级精度上**几乎等价**（CGCS2000 实现更精确、椭球参数有微小差异），国内正式项目常把 CGCS2000 当 WGS84 用；**GCJ-02 与 BD-09 是加密偏移坐标，不是标准 EPSG 坐标系**，因此只能用 gcoord / coordtransform / eviltransform 这类算法库纠偏，proj4js 无解；Web Mercator（3857）是显示用投影，瓦片索引必须是它。

---

## 6. 瓦片服务与部署

### 6.1 本地用 nginx / Node 发布瓦片

- [nginx 官方入门指南](https://nginx.org/en/docs/beginners_guide.html) —— `server`/`location`/`root`/`alias` 基础配置，发布瓦片目录只需要一个 `location /tiles/ { root ...; }`（标签：官方 | 优先级 P0）。
- [nginx `ngx_http_headers_module`（CORS 与缓存头）](https://nginx.org/en/docs/http/ngx_http_headers_module.html) —— 用 `add_header Access-Control-Allow-Origin *` 解决 Cesium 跨域加载瓦片；同时用 `Cache-Control` 给瓦片长缓存（标签：官方 | 优先级 P0）。
- [掘金 · 从零搭建离线地图服务：Nginx + Cesium/Leaflet 实战指南](https://juejin.cn/post/7647356541463298100) —— 中文实战，从目录结构、nginx 配置到 Cesium 加载的完整链路（标签：教程 | 优先级 P0）。
- [maptiler/tileserver-gl（GitHub，★2.9k）](https://github.com/maptiler/tileserver-gl) —— 免写 nginx 配置的选择：`npx tileserver-gl xxx.mbtiles` 直接起 XYZ/WMTS 服务（标签：工具 | 优先级 P0）。
- [consbio/mbtileserver（GitHub，★794）](https://github.com/consbio/mbtileserver) —— 单文件 Go 二进制发布 mbtiles 目录，适合内网机器（无 Node/Python 环境）部署（标签：工具 | 优先级 P1）。
- [知乎 · 地图影像（XYZ 切片）下载即发布方案](https://zhuanlan.zhihu.com/p/610352191) —— 中文长文，讲影像 XYZ 瓦片的获取与发布思路（标签：教程 | 优先级 P1）。**注：本次抓取被反爬拦截（HTTP 403），浏览器可正常访问。**

**踩坑点**：3D Tiles 与瓦片必须通过 HTTP(S) 访问，**不能用 `file://`**（浏览器的 CORS 会直接拦死）；`.json` 要返回 `application/json`，`.b3dm/.pnts/.i3dm` 建议 `application/octet-stream`；如果切片时做了 gzip 预压缩（3d-tiles-tools `gzip`），要确保 nginx 不重复压缩且 `Content-Encoding: gzip` 正确。

### 6.2 3D Tiles 部署到对象存储 + CDN

- [Cloudflare R2 官方文档](https://developers.cloudflare.com/r2/) —— 对象存储 + 公共存储桶（public bucket）直接对外提供 HTTPS 访问，配自定义域名即是 CDN，**无需改一行前端代码**（标签：官方 | 优先级 P0）。
- [Cloudflare R2 定价（已核验页面内容）](https://developers.cloudflare.com/r2/pricing/) —— **免费额度：每月 10 GB 存储、100 万次 Class A 请求、1000 万次 Class B 请求；出网流量（egress）完全免费**——这对 3D Tiles 这种「体积大、请求次数极多」的场景是决定性优势（标签：官方 | 优先级 P0）。
- [Cloudflare Pages 限制（已核验页面内容）](https://developers.cloudflare.com/pages/platform/limits/) —— **单个静态资源上限 25 MiB**，官方明确建议「更大的文件上传到 R2 并使用公共桶」；这直接说明了「3D Tiles 不要直接塞进 Pages」（标签：官方 | 优先级 P0）。
- [Vercel 限制（已核验页面内容）](https://vercel.com/docs/limits) —— **静态文件上传上限：Hobby 100 MB / Pro 1 GB**；3D Tiles 一个 tileset 动辄几百 MB 到数 GB，因此 Vercel 只能放前端壳，瓦片必须外链对象存储（标签：官方 | 优先级 P0）。
- [Vercel Blob 用量与定价](https://vercel.com/docs/vercel-blob/usage-and-pricing) —— 若确实想在 Vercel 侧存文件，看这里的存储/操作/流量计费方式（标签：官方 | 优先级 P1）。
- [Netlify 旧版套餐定价（已核验页面内容）](https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-legacy-plans/legacy-pricing-plans/) —— **免费版带宽 100 GB/月且为硬性上限**，超出即停服；瓦片流量极易打满，属于「能部署但别用来承载瓦片」的典型（标签：官方 | 优先级 P1）。
- [Netlify Large Media 要求与限制](https://docs.netlify.com/build/git-workflows/large-media/requirements-and-limitations/) —— 基于 Git LFS 的大文件方案，官方已标注**废弃（deprecated）**，不要用它来托管 3D Tiles（标签：官方 | 优先级 P2）。
- [阿里云 DataV TwinFabric · 是否可以接入 OSS 或静态 HTTP 服务承载的 3DTiles](https://help.aliyun.com/zh/datav/datav-twinfabric/support/can-i-access-the-3dtiles-slice-hosted-by-oss-or) —— 国内云厂商对「3D Tiles 放 OSS + 静态 HTTP」的官方答疑（标签：官方 | 优先级 P1）。**注：本次未直连核验。**

### 6.3 内网 / 离线部署的常见做法

- [mars3d 官方文档 · 发布三维数据服务](http://mars3d.cn/docs/data/server/) —— 中文版「离线地图数据怎么组织、怎么用 nginx 发布」的完整说明，含目录结构与跨域配置（标签：教程 | 优先级 P0）。**注：本次未直连核验。**
- [掘金 · 从零搭建离线地图服务：Nginx + Cesium/Leaflet 实战指南](https://juejin.cn/post/7647356541463298100) —— 同上，实战视角（标签：教程 | 优先级 P0）。
- [consbio/mbtileserver（GitHub，★794）](https://github.com/consbio/mbtileserver) —— 内网无外网依赖的单文件瓦片服务（标签：工具 | 优先级 P1）。
- [QGIS QMetaTiles 插件](https://plugins.qgis.org/plugins/QMetaTiles/) —— 在有网机器上预先下载 XYZ 瓦片成目录，再整个拷贝进内网（离线底图最常用套路）（标签：工具 | 优先级 P1）。
- [国家对地观测科学数据中心 · DEM 专题（免登录 FTP）](https://data.casearth.cn/thematic/dem/448) —— 内网环境里提前准备好 DEM 数据源（标签：工具 | 优先级 P2）。

**离线部署套路**：① 有网机器上用 gdal2tiles / QMetaTiles / fanvanzh-3dtiles 产出瓦片目录 → ② 整个目录拷贝进内网 → ③ nginx 指向该目录并加 CORS + 缓存头 → ④ 前端把 `Cesium3DTileset`/`UrlTemplateImageryProvider` 的地址从公网换成内网 IP；**注意内网无 HTTPS 时，若页面在 HTTPS 下加载瓦片会被 mixed-content 拦截**，需要内网也配自签证书或用内网 HTTP 页面。

---

## 7. GIS 数据格式对比

- [RFC 7946 · The GeoJSON Format（官方规范）](https://www.rfc-editor.org/rfc/rfc7946.html) —— GeoJSON 的正式标准：坐标必须是 WGS84（CRS84）、**必须使用经纬度顺序**、不支持自定义 CRS，这一点决定了「GeoJSON 天生不能带投影」（标签：官方 | 优先级 P0）。
- [ESRI Shapefile 技术白皮书（PDF）](https://www.esri.com/content/dam/esrisites/sitecore-archive/Files/Pdfs/library/whitepapers/pdfs/shapefile.pdf) —— shp 格式的原始定义，理解「为什么 shp 必须配套 .dbf/.shx/.prj」「字段名限制 10 字符」「编码问题从哪来」（标签：官方 | 优先级 P1）。
- [Mapbox Vector Tile Specification](https://mapbox.github.io/vector-tile-spec/) —— MVT（`.pbf`）的官方规范：几何用瓦片内整数坐标 + 命令流编码，属性用 protobuf，这就是 MVT 比 GeoJSON 小一个数量级的原因（标签：官方 | 优先级 P0）。
- [Mapbox 官方 · Vector tiles standards](https://docs.mapbox.com/data/tilesets/guides/vector-tiles-standards/) —— 讲清 MVT 的图层/要素/属性约束、瓦片边界裁剪规则与最佳实践（标签：官方 | 优先级 P0）。
- [Mapbox Vector Tiles Reference](https://docs.mapbox.com/vector-tiles/reference/) —— XYZ 瓦片编号、URL 模板、TileJSON 字段的参考手册，前端拼瓦片 URL 时对照（标签：官方 | 优先级 P1）。
- [3D Tiles 规范（CesiumGS/3d-tiles，★2.6k）](https://github.com/CesiumGS/3d-tiles) —— 3D Tiles 规范主仓库，tileset.json 字段、b3dm/i3dm/pnts 二进制结构、几何误差与 LOD 机制都在这里（标签：官方 | 优先级 P0）。
- [3D Tiles 规范目录（1.0 与 1.1）](https://github.com/CesiumGS/3d-tiles/tree/main/specification) —— 直接进入规范正文，**注意 1.1 用 glTF 取代 b3dm/i3dm、引入 metadata 与 implicit tiling**，新项目优先按 1.1 建（标签：官方 | 优先级 P0）。
- [glTF 官方网站（Khronos）](https://www.khronos.org/gltf/) —— 「3D 界的 JPEG」，3D Tiles 的内容载体；理解 glTF 是理解 3D Tiles 1.1 的前提（标签：官方 | 优先级 P0）。
- [glTF 2.0 规范（Khronos Registry）](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html) —— 完整规范正文（标签：官方 | 优先级 P1）。
- [KHR_draco_mesh_compression 扩展规范](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_draco_mesh_compression) —— glTF 中启用 Draco 压缩的标准扩展，**3D Tiles 体积优化的关键一环**（标签：官方 | 优先级 P0）。
- [google/draco（GitHub，★7.5k）](https://github.com/google/draco) —— Draco 几何压缩库本体，官方宣称在保持视觉保真度的前提下大幅压缩网格；配合 gltf-pipeline 使用（标签：官方 | 优先级 P0）。
- [topojson/topojson（GitHub，★4.9k）](https://github.com/topojson/topojson) —— TopoJSON：把共享边界只存一次 + 整数化坐标 + 量化，**同一份行政区划数据通常能比 GeoJSON 小 60%~80%**，但前端需用 topojson-client 还原（标签：工具 | 优先级 P0）。
- [mapbox/togeojson（GitHub，★1.3k）](https://github.com/mapbox/togeojson) —— KML/GPX → GeoJSON 的 JS 实现，纯前端场景不想装 GDAL 时用它（标签：工具 | 优先级 P1）。
- [Cesium 官方 · Data Formats](https://cesium.com/learn/data-formats/) —— 官方视角的格式支持矩阵与转换建议（标签：官方 | 优先级 P0）。

**选型速记**

| 格式 | 用途 | 体积特征 | 何时用 |
|---|---|---|---|
| shp | 传统 GIS 交换，ArcGIS 生态 | 中等，但必须多文件配套 | 从测绘/规划院拿到的原始数据，**入库后立刻转 GeoJSON** |
| GeoJSON | Web 交互、前后端交换 | 大（文本 + 重复边界 + 全精度坐标） | 小数据量矢量、调试、原型；超过几 MB 就该换 MVT |
| TopoJSON | 面状数据（行政区划）传输 | 比 GeoJSON 小 60%~80% | 面共享边界的行政区划、专题地图 |
| MVT / pbf | 矢量瓦片服务 | 最小，且支持分级抽稀 | Mapbox/MapLibre/天地图风格的矢量底图 |
| 3D Tiles | 三维瓦片（倾斜摄影/白模/点云/BIM） | 大（几 GB 级），靠 LOD + gzip + Draco 压 | 三维场景的绝对主力 |
| glTF / GLB | 单个三维模型 | GLB 单文件、比 glTF+外部资源更好分发 | 单体模型（车、设备、建筑单栋）；3D Tiles 1.1 的瓦片内容 |
| Draco | glTF 内的几何压缩扩展 | 几何数据通常可压到原体积的 1/5 ~ 1/10 量级 | 所有交付到 Web 的 glTF/3D Tiles 都应开启 |

---

## Mac 用户避坑提示（Apple Silicon / arm64）

**1）GDAL 命令行：优先 Homebrew，别用 pip 装**
`brew install gdal` 在 Apple Silicon 上有官方预编译瓶（bottle），已核验 [Homebrew gdal 页面](https://formulae.brew.sh/formula/gdal) 明确标注「macOS on Apple Silicon: tahoe ✅ sequoia ✅」且 Linux ARM64 也有，当前稳定版 3.13.3，**无需编译、无需 Rosetta**。装完用 `gdal-config --version` 确认。相反，PyPI 上的 [GDAL](https://pypi.org/project/GDAL/) 当前 3.13.3 **只发布了 `gdal-3.13.3.tar.gz` 源码包，没有任何 wheel**，`pip install gdal` 必然走源码编译，最常见的报错就是找不到 `gdal-config`。

**2）Python 生态：用「自带 GDAL 的 wheel」或 conda-forge，不要自己编 GDAL**
- 已核验：PyPI 的 [rasterio](https://pypi.org/project/rasterio/)（1.5.2）发布了 `macosx_15_0_arm64` wheel、[pyogrio](https://pypi.org/project/pyogrio/)（0.13.0）发布了 `macosx_12_0_arm64` wheel——**这两个包把 GDAL 打包进了 wheel**，`pip install rasterio pyogrio` 在 M 系列芯片上开箱即用，栅格读写和矢量读写全覆盖，日常根本不需要 `import gdal`。
- [PDAL](https://pypi.org/project/pdal/) 在 PyPI 上当前只有 `pdal-3.5.5.tar.gz` 源码包（点云处理），**不要 pip 装**；用 conda-forge：[pdal-feedstock](https://github.com/conda-forge/pdal-feedstock) 提供 osx-arm64 构建。
- GDAL 的 arm64 二进制同样走 conda-forge：[gdal-feedstock](https://github.com/conda-forge/gdal-feedstock)。
- 推荐组合（Mac）：`conda create -n gis -c conda-forge python=3.12 gdal rasterio pyogrio pdal py3dtiles laspy` —— 一条命令把整条工具链装成 arm64 原生，避免 brew 与 pip 的版本互踩。
- [py3dtiles](https://pypi.org/project/py3dtiles/) 是 `py3-none-any` 纯 Python wheel，**Mac 直接 pip 装没问题**，是 Mac 上做点云 → 3D Tiles 最顺手的工具。

**3）Docker：x86_64 镜像要靠 Rosetta 模拟，能不用就不用**
Docker Desktop for Mac 已核验可正常安装（[官方安装文档](https://docs.docker.com/desktop/setup/install/mac-install/)），但大量 GIS 镜像（老的 GIS 基础镜像、部分 CTB 镜像、FME/ArcGIS 相关镜像）**只发布 `linux/amd64`**，在 M 系列上会走 Rosetta 2 模拟运行，表现为「慢几倍」「随机内存溢出」「编译类镜像直接崩」。处理方式：
- 显式声明 `docker run --platform linux/amd64`，并确认 Docker Desktop 里已启用 Rosetta（Settings → General）；
- 优先找有 arm64 变体的镜像（如 [tum-gis/cesium-terrain-builder-docker](https://github.com/tum-gis/cesium-terrain-builder-docker) 这类项目多已支持多架构）；
- 换更轻的容器运行时：[OrbStack](https://orbstack.dev/)（[文档](https://docs.orbstack.dev/)）或 [Colima](https://github.com/abiosoft/colima)，在 arm64 上的启动速度与内存占用明显优于 Docker Desktop，做长时间切片更稳；
- 已知问题汇总见 [Docker Desktop 已知问题](https://docs.docker.com/desktop/troubleshoot-and-support/troubleshoot/known-issues/)。

**4）路径与文件名：3d-tiles-tools 要求「大小写敏感」，macOS 默认不是**
macOS 的 APFS 默认**大小写不敏感**，而 [3d-tiles-tools 的 README](https://github.com/CesiumGS/3d-tiles-tools) 明确写着「所有输入输出路径大小写敏感，即使 Windows 这类系统不区分大小写，命令行里的名字也必须与实际完全一致」。在 Mac 上开发时肉眼很难发现 `Tileset` 与 `tileset` 写错，但产物拷到 Linux 服务器/OSS 上就会 404。**对策**：切片产出后用 3d-tiles-validator 校验，并在部署前用一台 Linux（或 WSL）做一次全量加载测试。

**5）macOS 的「海量小文件」是真实的性能坑**
一个倾斜摄影 tileset 轻松几十万个 `.b3dm`/`.json` 小文件文件。在 macOS 上：拷贝/删除这种目录用 Finder 会卡死，务必用 `rsync -a --delete` 或 `ditto`；`cp -r` 反而比 `rsync` 慢很多。同时 **不要在 iCloud Drive / 桌面同步目录里切片**，同步进程会疯狂抢占 I/O，建议放在外置 SSD 或 `~/GIS/` 这类非同步目录。

**6）为什么切片这件事更应该放到 Windows 上做**
- **图形化切片工具**（CesiumLab / GISBox 等）只有 Windows 版，胜在「点几下就出结果」，但**闭源、参数不透明，面试时讲不清内部怎么算的**。本项目改用开源命令行方案（`fanvanzh/3dtiles` + `py3dtiles`），**Mac 上全程可跑通**，且每个切片参数你都能解释。
- 国内倾斜摄影上下游（ContextCapture / Smart3D、部分 OSGB 处理工具、ArcGIS 桌面套件、FME 的部分许可）**本身就是 Windows-only 生态**，数据交付方给的原始 OSGB 工程也多在 Windows 上做质检。
- Windows + NTFS 处理**海量小文件**的目录遍历、批量重命名、压缩打包体验明显好于 macOS；且切片机通常需要挂载大容量硬盘，Windows 主机的扩展成本更低。
- Windows 原生跑 GDAL/ogr2ogr 有 **OSGeo4W** 安装包（见 [GDAL 二进制下载汇总](https://trac.osgeo.org/gdal/wiki/DownloadingGdalBinaries)），也可以用 WSL2 + conda-forge，两条路都比在 Mac 上折腾交叉编译省心。
- **分工建议**：Mac 上做前端开发、数据探查（QGIS）、格式转换与预处理（GDAL/ogr2ogr 走 brew 或 conda-forge）、小规模 3D Tiles 试验（fanvanzh/3dtiles 支持 macOS arm64，py3dtiles 纯 Python 可用）；把**大批量倾斜摄影切片、地形切片、点云切片**放到 Windows 机器上跑 CesiumLab，产物通过移动硬盘或对象存储同步回来。
