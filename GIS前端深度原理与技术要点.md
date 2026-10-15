# Cesium / Mapbox 深度原理 + GIS 前端知识要点（链接已核实版）

> **定位**：与同目录 [`GIS前端学习资料清单.md`](GIS前端学习资料清单.md)（视频优先版）互补——那份解决「怎么快速上手」，这份解决「原理要挖多深、怎么讲清楚」。
>
> **核实说明**：以下每条均经 `web_search` 检索 + HTTP 请求逐个实测。
> - `✅` = 实测返回 200，链接可用
> - `⚠️环境受限` = 该站点本身正常，是**本机代理网络无法直连**（CSDN / 知乎 / 超图官网 / Mars3D 等国内站点），链接来自搜索引擎索引的真实页面，请自行点开确认
> - 已剔除 Cesium 1.x 早期失效博客（旧 cesium.com/blog 路径大量 404），换成现行地址

---

## 1. Cesium 官方与源码向

### 1.1 官方 API 文档（Reference Documentation）

- [Viewer](https://cesium.com/learn/cesiumjs/ref-doc/Viewer.html) ✅ —— Cesium 应用入口，初始化场景、挂载 widget、管理 `requestRenderMode` / `targetFrameRate`，理解引擎生命周期的第一步（官方 | P0）
- [Scene](https://cesium.com/learn/cesiumjs/ref-doc/Scene.html) ✅ —— 三维场景本体，掌管 `primitives` 集合、光照、大气、后处理与 `requestRenderMode`、`maximumRenderTimeChange`，态势平台所有渲染开关都在这里（官方 | P0）
- [Camera](https://cesium.com/learn/cesiumjs/ref-doc/Camera.html) ✅ —— 相机模型，含 `flyTo`/`setView`/`lookAt`、视锥与 `frustum`，是理解「3D Tiles 为何加载某层瓦片」的前提（官方 | P0）
- [Entity](https://cesium.com/learn/cesiumjs/ref-doc/Entity.html) ✅ —— 高层数据驱动 API，位置/朝向可绑定 `Property` 随时间变化，写态势标绘最顺手，但海量数据下是性能瓶颈（官方 | P0）
- [Primitive](https://cesium.com/learn/cesiumjs/ref-doc/Primitive.html) ✅ —— 低层渲染单元，直接对应一次 WebGL draw call，`PrimitiveCollection` 可批量管理，性能优化的核心抓手（官方 | P0）
- [DataSource](https://cesium.com/learn/cesiumjs/ref-doc/DataSource.html) ✅ —— 数据源抽象，`GeoJsonDataSource`/`CzmlDataSource`/`KmlDataSource` 均继承它，轨迹回放常用 CZML（官方 | P0）
- [ImageryProvider](https://cesium.com/learn/cesiumjs/ref-doc/ImageryProvider.html) ✅ —— 影像图层抽象基类，理解 `UrlTemplateImageryProvider`/`WebMapTileServiceImageryProvider` 才配得出离线底图（官方 | P0）
- [TerrainProvider](https://cesium.com/learn/cesiumjs/ref-doc/TerrainProvider.html) ✅ —— 地形提供者，含 `CesiumTerrainProvider`（quantized-mesh）与 `createWorldTerrainAsync`（官方 | P0）
- [Cesium3DTileset](https://cesium.com/learn/cesiumjs/ref-doc/Cesium3DTileset.html) ✅ —— 3D Tiles 加载入口，`maximumScreenSpaceError`/`maximumMemoryUsage`/`cacheBytes` 等调度参数全在这里（官方 | P0）
- [PointPrimitiveCollection](https://cesium.com/learn/cesiumjs/ref-doc/PointPrimitiveCollection.html) ✅ —— 10 万级点渲染的正解，全部点合并为单批次提交（官方 | P0）
- [BufferPointCollection](https://cesium.com/learn/cesiumjs/ref-doc/BufferPointCollection.html) ✅ —— 较新版本提供的 TypedArray 批式点集合，比逐点 `add()` 更适合超大点集（官方 | P1）
- [CustomShader](https://cesium.com/learn/cesiumjs/ref-doc/CustomShader.html) ✅ —— 不写 Primitive 也能注入 GLSL 改材质，做动态材质/热力效果的关键（官方 | P0）
- [EntityCluster](https://cesium.com/learn/cesiumjs/ref-doc/EntityCluster.html) ✅ —— Entity 层聚合，海量标签/点先聚合再渲染（官方 | P1）
- [Cartesian3](https://cesium.com/learn/cesiumjs/ref-doc/Cartesian3.html) ✅ / [Cartographic](https://cesium.com/learn/cesiumjs/ref-doc/Cartographic.html) ✅ / [Transforms](https://cesium.com/learn/cesiumjs/ref-doc/Transforms.html) ✅ / [WebMercatorProjection](https://cesium.com/learn/cesiumjs/ref-doc/WebMercatorProjection.html) ✅ —— 坐标体系四件套，详见第 4 章（官方 | P0）
- [GeographicProjection](https://cesium.com/learn/cesiumjs/ref-doc/GeographicProjection.html) ✅ —— 等经纬度投影，用于 `SceneMode.SCENE2D` / 哥伦布视图（官方 | P1）
- [global.html（全量 API 索引）](https://cesium.com/learn/cesiumjs/ref-doc/global.html) ✅ —— 按需检索入口（官方 | P2）

### 1.2 教程与示例

- [CesiumJS Quickstart 官方入门](https://cesium.com/learn/cesiumjs-learn/cesiumjs-quickstart/) ✅ —— 零基础起步，含 token 申请与最小可运行工程（官方 | P0）
- [CesiumJS Learn 教程总目录](https://cesium.com/learn/cesiumjs-learn/) ✅ —— 官方教程聚合页，按「入门 / 影像地形 / 3D Tiles / 数据可视化」分组（官方 | P0）
- [Cesium Sandcastle 在线沙盒](https://cesium.com/learn/cesiumjs-sandcastle/) ✅ —— 官方可运行示例集合，改代码即时预览，学 API 最高效入口（官方 | P0）
- [Sandcastle：Scene Rendering Performance](https://sandcastle.cesium.com/?src=Scene%20Rendering%20Performance.html) ✅ —— 官方专门演示性能差异的示例，直接对比优化前后帧率，**做「性能优化对比」照抄即可**（官方 | P0）
- [同示例：版本锁定快照](https://cesium.com/downloads/cesiumjs/releases/1.134/Apps/Sandcastle/gallery/Scene%20Rendering%20Performance.html) ✅ —— 避免官方升级后示例漂移（官方 | P2）

### 1.3 博客、社区与源码

- [Cesium 官方博客](https://cesium.com/blog/) ✅ —— 官方发布版本说明、3D Tiles 演进、性能特性，判断「资料是否过时」的权威时间线（官方 | P0）
- [Cesium Releases in March 2025（月更示例）](https://cesium.com/blog/2025/03/03/cesium-releases-in-march-2025/) ✅ —— 感知当前版本号与 API 变更节奏，避免学早期写法（官方 | P2）
- [CesiumJS GitHub 仓库](https://github.com/CesiumGS/cesium) ✅ —— 源码，重点看 `packages/engine/Source/Scene/`（官方仓库 | P0）
- [源码：Cesium3DTileset.js](https://github.com/CesiumGS/cesium/blob/main/packages/engine/Source/Scene/Cesium3DTileset.js) ✅ —— 内含 `screenSpaceError` 计算公式与注释，是「瓦片调度原理」的终极依据（官方仓库 | P0）
- [Cesium 官方社区论坛](https://community.cesium.com/) ✅ —— 官方开发者答疑区，「Entity vs Primitive 性能差异」这类问题的权威回答基本都在这里（官方社区 | P0）
- [Cesium 平台介绍页](https://cesium.com/platform/cesiumjs/) ✅ —— 产品化能力总览，讲选型理由时引用（官方 | P2）
- [CesiumJS-tutorial（hujiulin，中文）](https://github.com/hujiulin/CesiumJS-tutorial) ✅ —— 中文教程仓库，覆盖 Viewer / Entity / DataSource / 坐标（博客·仓库 | P1）
- [Cesium 中文网 cesium.net.cn](https://cesium.net.cn/) ⚠️429 —— Cesium 官方中文站，含中文文档、教程与 3D Tiles 专栏（实测站点存活但限流，浏览器可直接打开）（官方中文站 | P0）
- Mars3D（`mars3d.cn`）与 Cesium 中文社区（`cesium.xin`）：⚠️环境受限。两者中文资料质量高（Mars3D 有完整的 [坐标系文档](http://mars3d.cn/docs/basis/crs/) 与 [OSGB 转 3D Tiles 教程](http://mars3d.cn/docs/data/osgb-tileset/)），是国产 Cesium 封装的重要参考，请自行访问。

---

## 2. 3D Tiles

### 2.1 规范（Specification）——最权威

- [3D Tiles 官方规范主目录](https://github.com/CesiumGS/3d-tiles/tree/main/specification) ✅ —— 规范入口，1.1 版起以 glTF 为第一瓦片格式（官方规范 | P0）
- [规范正文单文件 README.adoc（最适合通读）](https://raw.githubusercontent.com/CesiumGS/3d-tiles/main/specification/README.adoc) ✅ —— 纯文本全文，含 `geometricError`/`refine`/`boundingVolume` 的原始定义（已逐段核实）（官方规范 | P0）
- [规范正文 GitHub 渲染版（带锚点）](https://github.com/CesiumGS/3d-tiles/blob/main/specification/README.adoc#tileset-json) ✅ —— 便于跳转 `tileset.json` 章节（官方规范 | P0）
- [tileset.schema.json（字段级 JSON Schema）](https://github.com/CesiumGS/3d-tiles/blob/main/specification/schema/tileset.schema.json) ✅ —— `tileset.json` 每个字段的类型/必填/默认值权威定义，写工具或校验必备（官方规范 | P0）
- [OGC 3D Tiles 1.1 标准（22-025r4）](https://docs.ogc.org/cs/22-025r4/22-025r4.html) ✅ —— 3D Tiles 已进入 OGC 标准体系，标准化后的正式文档，适合引用（官方标准 | P1）

> **已核实的 `tileset.json` 核心字段（直接背）**
>
> | 字段 | 含义与要点 |
> |---|---|
> | `asset.version` | 规范版本，如 `"1.1"` |
> | 顶层 `geometricError` | 根节点几何误差（米），整个 tileset 的最大误差 |
> | `root` | 根瓦片，向下递归 `children` |
> | `boundingVolume.region` | `[west, south, east, north, minH, maxH]`，**经纬度单位是弧度**（基于 EPSG:4979 但单位偏离定义） |
> | `boundingVolume.box` | 12 个数 = 中心点 + 3 个半轴向量（OBB），列主序风格 |
> | `boundingVolume.sphere` | 4 个数 = 中心 xyz + 半径（米） |
> | `geometricError` | **非负数**；表示该瓦片对其源几何的简化误差。根最大、越深越小、叶子趋近 0；值越大细化越激进 |
> | `refine` | `"REPLACE"`（子替代父）或 `"ADD"`（父子同时渲染）；**根节点必填**，其余省略则**继承父节点** |
> | `content.uri` | 指向 `b3dm`/`i3dm`/`pnts`/`cmpt`（1.0 旧格式，1.1 起 deprecated）或 **`glb`（1.1 主推）**；也可指向另一个 `tileset.json` 形成「瓦片集套瓦片集」 |
> | `transform` | 4×4 仿射矩阵，**列主序**，本地→父坐标系；会按最大缩放因子**缩放 `geometricError`** |
> | `viewerRequestVolume` | 相机进入该包围体才请求渲染，用于异构数据集组合 |
> | `implicitTiling` | `subdivisionScheme`(QUADTREE/OCTREE) / `availableLevels` / `subtreeLevels` / `subtrees.uri`，用模板 URI 表达规则四叉/八叉树 |

### 2.2 原理讲解与应用

- [3D Tiles Essentials（官方科普与图示）](https://cesium.com/why-cesium/3d-tiles/3d-tiles-essentials/) ✅ —— 官方出品，用图讲清 boundingVolume / geometricError / ADD vs REPLACE / 四叉八叉树，**面试前看图复习最省时间**（官方 | P0）
- [3D Tiles Samples 官方样例瓦片集](https://github.com/CesiumGS/3d-tiles-samples) ✅ —— 每个目录一个可运行样例（含 `TilesetWithRequestVolume`），对照规范看最直观（官方仓库 | P1）
- [3d-tiles-tools 官方工具集](https://github.com/CesiumGS/3d-tiles-tools) ✅ —— 官方 Node 工具，b3dm→glb 转换、tileset 优化与校验，数据处理必备（官方工具 | P1）
- [Cesium Native：TilesetOptions 结构](https://cesium.com/learn/cesium-native/ref-doc/structCesium3DTilesSelection_1_1TilesetOptions.html) ✅ —— 原生端同款调度参数，佐证调度逻辑（官方 | P2）

> **LOD 调度原理（必须能讲清）**：客户端计算 **屏幕空间误差 SSE**——用 `geometricError`、瓦片到相机的距离、屏幕尺寸与分辨率，算出「若只渲染本瓦片而不渲染子瓦片会引入多少像素级误差」；**超过 `maximumScreenSpaceError`（Cesium 默认 16）就细化到子瓦片**。这就是 3D Tiles 能「按需加载、按需渲染」的核心。

### 2.3 glTF / GLB 与 Draco 压缩

- [glTF 2.0 规范仓库（KhronosGroup）](https://github.com/KhronosGroup/glTF) ✅ —— 3D Tiles 1.1 主力瓦片格式，理解 GLB 容器结构（JSON chunk + BIN chunk）（官方规范 | P0）
- [Khronos glTF 官网](https://www.khronos.org/gltf/) ✅ —— 生态与工具链总览，含导出器清单（官方 | P2）
- [KHR_draco_mesh_compression 扩展规范](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_draco_mesh_compression/README.md) ✅ —— Draco 如何嵌入 glTF 的权威说明（官方规范 | P0）
- [Google Draco 仓库](https://github.com/google/draco) ✅ —— 几何压缩库本体，压缩率与解码开销数据来源（官方仓库 | P1）
- [Cesium 官方博客：Draco 压缩](https://cesium.com/blog/2018/04/09/draco-compression/) ✅ —— 官方讲 Cesium 如何支持 Draco、对加载体积与性能的影响（官方 | P0）
- [fanvanzh/3dtiles（OSGB → 3D Tiles 工具）](https://github.com/fanvanzh/3dtiles) ✅ —— 国内使用最广的倾斜摄影转换工具，**「OSGB 怎么转 3D Tiles」的标准答案**（仓库 | P0）
- [osgb23dtiles（Python 实现）](https://pypi.org/project/osgb23dtiles/) ✅ —— 另一种开源转换路径，工具链备选（仓库 | P2）

---

## 3. Cesium 性能优化

### 3.1 按需渲染 requestRenderMode（官方）

- [官方博客：Improving Performance with Explicit Rendering](https://cesium.com/blog/2018/01/24/cesium-scene-rendering-performance/) ✅ —— **`requestRenderMode` 的权威出处**，讲清按需渲染原理与收益：静态场景下几乎不再出帧（官方 | P0）
- [Scene API：requestRenderMode / maximumRenderTimeChange](https://cesium.com/learn/cesiumjs/ref-doc/Scene.html#requestRenderMode) ✅ —— 参数级说明与注意事项（**改动场景后需手动 `scene.requestRender()`**）（官方 | P0）
- [Viewer API：requestRenderMode](https://cesium.com/learn/cesiumjs/ref-doc/Viewer.html#requestRenderMode) ✅ —— Viewer 构造期直接开启的写法（官方 | P0）

### 3.2 Entity vs Primitive 与海量点（官方）

- [Cesium 官方社区论坛](https://community.cesium.com/) ✅ —— 官方开发者对「何时该用 Primitive」的权威回答集中地，检索 `Entity vs Primitive performance`（官方社区 | P0）
- [PointPrimitiveCollection API](https://cesium.com/learn/cesiumjs/ref-doc/PointPrimitiveCollection.html) ✅ —— **10 万点渲染正解**：所有点合并进一个批次、一次 draw call（官方 | P0）
- [BufferPointCollection API](https://cesium.com/learn/cesiumjs/ref-doc/BufferPointCollection.html) ✅ —— TypedArray 批量灌点，适合更大点集（官方 | P1）
- [Cesium3DTileset API（内存与调度参数）](https://cesium.com/learn/cesiumjs/ref-doc/Cesium3DTileset.html) ✅ —— `maximumScreenSpaceError`、`maximumMemoryUsage`（默认 512MB）、`cacheBytes`、`maximumNumberOfLoadedTiles`——**「加载慢 / 内存爆」的调参入口**（官方 | P0）

### 3.3 CustomShader（官方）

- [CustomShader API](https://cesium.com/learn/cesiumjs/ref-doc/CustomShader.html) ✅ —— 注入 GLSL 改材质，无需自写 Primitive（官方 | P0）
- [CustomShader 官方指南（源码内文档）](https://github.com/CesiumGS/cesium/blob/main/Documentation/CustomShaderGuide/README.md) ✅ —— 官方唯一系统性教程：`vertexShaderText`/`fragmentShaderText`、varying、与内置材质的混合方式（官方 | P0）

### 3.4 中文性能优化实践

- [记使用 Cesium 渲染三维场景导致崩溃的优化思路跟过程（掘金）](https://juejin.cn/post/7442600267746902050) ✅ —— 真实「渲染崩溃 → 定位 → 优化」复盘，讲内存与批次控制，高度贴合你的「性能优化对比」模块（博客 | P0）
- [cesium 中 primitives 和 entities 的区别（掘金）](https://juejin.cn/post/7486391100648161319) ✅ —— 中文里把两者差异与性能取舍讲得较清楚的一篇（博客 | P0）
- [Cesium 中 Primitive 与 Entity 的区别（掘金）](https://juejin.cn/post/7521708544724746279) ✅ —— 上篇的对照阅读，补充适用场景（博客 | P1）
- [Cesium、Three & WebGL 详解（二）：渲染引擎向 GPU 传数据、性能优化、引擎对比（CSDN）](https://blog.csdn.net/m0_55049655/article/details/148800127) ⚠️环境受限 —— 从「CPU→GPU 传数据」角度解释性能瓶颈，是理解 Primitive 为何快的底层视角（博客 | P1）
- [别再卡顿了！Cesium 加载 10 万+ 点数据性能优化实战（CSDN 文库）](https://wenku.csdn.net/column/22c0g7s9xds) ⚠️环境受限 —— 面向 10 万+ 点的优化实战含完整代码（博客 | P1）
- [Cesium 渲染图层长期不删除会导致内存泄漏吗？（CSDN 问答）](https://ask.csdn.net/questions/8448577) ⚠️环境受限 —— 直接对应 destroy / remove / 图层释放这一高频考点（问答 | P1）
- [3DTiles 之使用 customShader 调整风格（博客园）](https://www.cnblogs.com/zhifang1027/articles/18546259) ⚠️环境受限 —— 中文实战示例，对 3D Tiles 用 CustomShader 换风格（博客 | P1）

### 3.5 内存泄漏与销毁要点（必须能讲清）

- `viewer.entities.removeAll()` 清实体
- `scene.primitives.remove(primitive)` 后**必须调用 `primitive.destroy()`** 释放 GPU 资源
- `viewer.dataSources.remove(ds, true)` —— **第二参数为 true 才真正销毁**
- `viewer.imageryLayers.remove(layer, true)` —— 同理
- 自定义 `Primitive` 在 `destroy()` 里释放 `VertexArray`/`Buffer`/`ShaderProgram`/`Texture`
- 事件监听（`viewer.scene.postRender.addEventListener` 等）必须成对移除
- 排查手段：Chrome DevTools Memory 面板，反复进出场景对比堆快照

---

## 4. 坐标系

### 4.1 Cesium 官方坐标 API

- [Cartesian3](https://cesium.com/learn/cesiumjs/ref-doc/Cartesian3.html) ✅ —— **ECEF 地心空间直角坐标**（米），Cesium 内部一切位置最终都归到它（官方 | P0）
- [Cartographic](https://cesium.com/learn/cesiumjs/ref-doc/Cartographic.html) ✅ —— **经纬高**，`longitude`/`latitude` 单位是**弧度**、`height` 是米（官方 | P0）
- [Transforms](https://cesium.com/learn/cesiumjs/ref-doc/Transforms.html) ✅ —— `eastNorthUpToFixedFrame`（局部 ENU 坐标系）等，做标绘/贴地/模型朝向必用（官方 | P0）
- [WebMercatorProjection](https://cesium.com/learn/cesiumjs/ref-doc/WebMercatorProjection.html) ✅ —— **EPSG:3857** Web 墨卡托投影类，与经纬度互转（官方 | P0）

### 4.2 坐标系标准（EPSG 权威定义）

- [EPSG:4326（WGS 84 经纬度）](https://epsg.io/4326) ✅ —— 全球定位系统基准，**经纬度以度为单位**（官方标准 | P0）
- [EPSG:4490（CGCS2000 经纬度）](https://epsg.io/4490) ✅ —— 中国 2000 国家大地坐标系，**国内测绘法定基准**（官方标准 | P0）
- [EPSG:3857（Web Mercator）](https://epsg.io/3857) ✅ —— 所有 Web 瓦片地图（OSM/高德/Mapbox）使用的投影，**面积严重变形但切片规整**（官方标准 | P0）
- [华为云：GIS 中经纬度坐标系和投影坐标系总结（4326 / 4490 / 3857）](https://bbs.huaweicloud.com/blogs/393239) ✅ —— 中文里把三者讲得最直白的一篇，**CGCS2000 vs WGS84 的差异（厘米级、工程上近似等同）说得很清楚**（博客 | P0）

### 4.3 转换库

- [proj4js 官网](https://proj4js.org/) ✅ —— JS 坐标系转换标准库，按 EPSG 代码任意投影互转，处理 4490/3857/北京54 等工程坐标系的正解（官方文档 | P0）
- [gcoord（hujiulong/gcoord，npm 指向的官方仓库）](https://github.com/hujiulong/gcoord) ✅ —— 轻量、专注中国偏移坐标系互转（WGS84/GCJ02/BD09），`gcoord.transform(geojson, gcoord.WGS84, gcoord.GCJ02)` 一行纠偏（仓库 | P0）

### 4.4 坐标转换要点（必须能讲清）

- **转换链**：业务经纬度 → `Cartesian3.fromDegrees(lon, lat, h)` → 内部 ECEF；取回时 `Cartographic.fromCartesian(cartesian)` → 弧度 → `Cesium.Math.toDegrees()`
- **CGCS2000 与 WGS84**：椭球参数（长半轴、扁率）几乎一致，同一点坐标差异在**厘米级**；工程中常近似等同，但严格入库应保留 EPSG:4490 标识
- **GCJ-02（火星坐标）**：国测局加密坐标系，高德/腾讯底图使用；**WGS84 原始 GPS 数据不纠偏就会在地图上偏移数百米**。百度另有 BD-09（在 GCJ-02 上二次偏移）
- **典型坑**：倾斜摄影 3D Tiles 数据是 WGS84、底图是 GCJ-02 → 整体错位；离线瓦片的切片方案（TMS/XYZ/WMTS）与 Cesium 的 `WebMercatorTilingScheme`/`GeographicTilingScheme` 不匹配 → 瓦片错层

---

## 5. Mapbox GL JS

### 5.1 官方文档与架构

- [Mapbox GL JS API 文档](https://docs.mapbox.com/mapbox-gl-js/api/) ✅ —— Map/Source/Layer/MapMouseEvent 全量 API（官方 | P0）
- [Mapbox GL JS Guides（使用指南）](https://docs.mapbox.com/mapbox-gl-js/guides/) ✅ —— 按主题组织，比 API 文档更适合系统学习（官方 | P0）
- [Mapbox GL JS ARCHITECTURE.md（架构说明）](https://github.com/mapbox/mapbox-gl-js/blob/main/ARCHITECTURE.md) ✅ —— **官方解释渲染流水线**：Style → Source 缓存/瓦片管理 → Worker 池解析与布局 → 主线程 WebGL 绘制。回答「Mapbox 原理」就靠它（官方仓库 | P0）
- [MapLibre GL JS 文档](https://maplibre.org/maplibre-gl-js/docs/) ✅ —— Mapbox GL JS v2 的开源分支，**API 高度兼容且无需 token**，做项目与内网部署的实用替代（官方文档 | P1）

### 5.2 Style Specification 与 Expression

- [Style Specification 总目录](https://docs.mapbox.com/style-spec/reference/) ✅ —— 样式规范根节点，所有 source/layer 类型索引（官方规范 | P0）
- [Expressions（表达式语法）](https://docs.mapbox.com/style-spec/reference/expressions/) ✅ —— `interpolate`/`step`/`case`/`match`/`get`/`zoom` 全表，**数据驱动样式与动态效果的核心**（官方规范 | P0）
- [Layers（图层类型参考）](https://docs.mapbox.com/style-spec/reference/layers/) ✅ —— fill/line/symbol/circle/heatmap/fill-extrusion/raster 各类型属性（官方规范 | P0）

### 5.3 矢量瓦片（MVT）

- [Vector Tile Specification v2.1（Mapbox 官方）](https://github.com/mapbox/vector-tile-spec/tree/master/2.1) ✅ —— **MVT 权威规范**：Protobuf 编码、图层/要素/几何命令（MoveTo/LineTo/ClosePath）、瓦片内坐标与 extent（默认 4096）（官方规范 | P0）
- [vector-tile-spec 主仓库](https://github.com/mapbox/vector-tile-spec) ✅ —— 含 v1 历史与变更说明（官方规范 | P1）
- [Mapbox：Vector tiles 入门指南](https://docs.mapbox.com/data/tilesets/guides/vector-tiles-introduction/) ✅ —— 官方讲「为什么用矢量瓦片」：体积小、一套瓦片多种样式、客户端换肤（官方 | P1）
- [Mapbox：Vector tiles standards](https://docs.mapbox.com/data/tilesets/guides/vector-tiles-standards/) ✅ —— 生产级切片标准（图层命名、属性、简化策略），做离线切片时参考（官方 | P2）

### 5.4 聚合、3D 与自定义 WebGL 图层

- [官方示例：Cluster（点聚合）](https://docs.mapbox.com/mapbox-gl-js/example/cluster/) ✅ —— `cluster: true` + `clusterRadius` + `point_count` 数据驱动样式，**海量点二维侧的标准解法**（官方示例 | P0）
- [官方示例：Add a custom style layer（自定义 WebGL 图层）](https://docs.mapbox.com/mapbox-gl-js/example/custom-style-layer/) ✅ —— `type: 'custom'` 实现 `render(gl, matrix)`，直接写 WebGL，**「custom layer 怎么写」的标准答案**（官方示例 | P0）
- [官方示例：Add a 3D model（three.js 集成）](https://docs.mapbox.com/mapbox-gl-js/example/add-3d-model/) ✅ —— 在同一画布叠加 three.js 场景，理解 Mapbox 与外部渲染器共享 WebGL 上下文的方式（官方示例 | P1）

### 5.5 Mapbox vs Cesium 选型

- [地图可视化的艺术：深入比较 Mapbox、OpenLayers、Leaflet 和 Cesium（腾讯云）](https://cloud.tencent.com/developer/article/2490668) ✅ —— 横向对比四者适用场景，**中文里讲「选型」最完整的一篇**（博客 | P0）
- [三维 GIS 平台架构与实现：从数据引擎到 Web 可视化（腾讯云）](https://cloud.tencent.com/developer/article/2730415) ✅ —— 讲平台级架构（数据引擎 → 服务 → Web 渲染），把单点知识串成体系，**讲「项目架构」时极有用**（博客 | P0）
- [数字孪生项目开发技术对比（阿里云开发者社区）](https://developer.aliyun.com/article/1752167) ⚠️环境受限 —— 从数字孪生工程角度对比技术栈（博客 | P1）

---

## 6. WebGL 基础（够用即可）

> 目标不是学会写引擎，而是能看懂 Cesium 自定义 Primitive 与 Mapbox custom layer 里的 WebGL 代码。

- [MDN：WebGL 教程（中文）](https://developer.mozilla.org/zh-CN/docs/Web/API/WebGL_API/Tutorial) ✅ —— 从 `getContext('webgl')` 到着色器编译、绘制三角形，最权威入门（官方文档 | P0）
- [WebGL Fundamentals 中文版](https://webglfundamentals.org/webgl/lessons/zh_cn/) ✅ —— **最推荐的系统教程**：讲清 attribute/uniform/varying、矩阵变换、纹理、**实例化（instancing）**。海量渲染的性能关键正是 instancing（博客 | P0）
- [The Book of Shaders（中文）](https://thebookofshaders.com/?lan=ch) ✅ —— GLSL 着色器思维与常用函数，写 CustomShader 前必读（博客 | P0）
- [WebGL Fundamentals 英文原版](https://webglfundamentals.org/) ✅ —— 中文版偶有章节滞后，对照使用（博客 | P2）
- [LearnOpenGL 中文版](https://learnopengl-cn.github.io/) ✅ —— 深入理解渲染管线、帧缓冲、批次与性能（选读深度篇即可）（博客 | P1）

**GIS 为什么用 WebGL（要点）**

1. **硬件加速**：GPU 并行处理顶点与像素；Canvas 2D 在万级图形时即崩
2. **批量提交**：顶点数据常驻 VBO，一次 `drawElements` 画完十万点/整片瓦片，把 CPU→GPU 通信次数降到 1
3. **可编程着色器**：颜色/高度/热力/动态材质都在 GPU 上算，支持逐要素差异化渲染而不增加 draw call
4. **实例化（Instancing）**：同一几何体用不同变换矩阵批量绘制，是海量模型/要素渲染的核心手段

**自定义 Primitive 的最低 WebGL 知识清单**：`WebGLRenderingContext` 获取与状态管理 → `Buffer`/`VertexArray` 组织顶点属性 → `ShaderProgram` 编译链接 → `attribute`/`uniform`/`varying` 传参 → MVP 矩阵变换 → `drawElements` 索引绘制 → `destroy()` 释放 GL 资源。Cesium 的 `Primitive`/`Geometry`/`Appearance` 三层正是对这些步骤的封装。

---

## 7. GIS 前端知识自测题与同行总结

### 7.1 同行的知识复盘

- [2026 三维 WebGIS 开发面试题 + 答案（B 站专栏）](https://www.bilibili.com/opus/1196587427843538945) ✅ —— 成体系题目清单，适合批量过题（自测题 | P0）
- [2025 GIS 开发面试全解析：核心知识体系与实战技巧（百度开发者）](https://developer.baidu.com/article/detail.html?id=6048066) ⚠️环境受限 —— 从「核心知识体系」角度组织，适合查漏（自测题 | P1）
- [2025 中科院 GIS 开发面试题及答案（CSDN）](https://blog.csdn.net/2301_78220461/article/details/155450242) ⚠️环境受限 —— 偏科研院所风格，GIS 理论基础题较多（自测题 | P2）

### 7.2 专题自测题

- [WebGIS 面试题：GIS 篇（一）（CSDN）](https://blog.csdn.net/jdjxbsus/article/details/155017616) ⚠️环境受限 —— 系列文章，按 GIS 基础/坐标系/服务分层出题（自测题 | P1）
- [WebGIS 面试题：GIS 篇（七）](https://avoid.overfit.cn/post/3bfeea4f7bd8416ca0625ee5a89cb3d7) ⚠️环境受限 —— 同系列后续篇，含三维与切片内容（自测题 | P2）
- [2026 三维 webgis 开发面试题 + 答案（GitCode）](https://gitcode.csdn.net/69e82d060a2f6a37c5a16e45.html) ⚠️环境受限 —— 另一份成体系题目（自测题 | P2）
- [WebGIS 面试题及详细答案（book118 文档）](https://max.book118.com/html/2026/0518/5030000032013214.shtm) ⚠️环境受限 —— 文档版含详细答案，当题库刷（自测题 | P2）

### 7.3 场景题（对应项目模块）

- **瓦片 404 / 黑屏**：[Cesium 加载离线地图时瓦片 404 或黑屏，如何定位资源路径与坐标系问题（CSDN 问答）](https://ask.csdn.net/questions/9365355) ⚠️环境受限 —— 直接给出排查路径（问答 | P0）
- **地形加载失败**：[Cesium 中 TerrainTile 加载失败如何排查（CSDN 问答）](https://ask.csdn.net/questions/9206121) ⚠️环境受限 —— 地形服务排查（问答 | P1）
- **内网离线部署**：[ShareQiu1994/cesium-offline-server](https://github.com/ShareQiu1994/cesium-offline-server) ✅ —— **可跑的开源离线地图/地形/3dtiles 服务**，做「内网离线部署」这题的最佳实操参考（仓库 | P0）
- **OSGB 转换实战**：[GISBox：OSGB 转 3DTiles 全攻略](https://www.gisbox.com.cn/articles/v1/kxcnowse68gt/) ⚠️环境受限 —— 图文步骤，从 OSGB 目录到可加载 tileset（博客 | P1）
- **OSGB 顶层节点合并**：[手把手教你合并 OSGB 顶层节点，让 Cesium 加载 3DTiles 飞起来（CSDN 文库）](https://wenku.csdn.net/column/58z1med2pjn) ⚠️环境受限 —— 讲清「为什么顶层节点多会卡」与合并收益（博客 | P1）
- **3D Tiles 加载技术解析**：[3D Tiles 瓦片加载技术深度解析与 3D 建模应用（百度云）](https://cloud.baidu.com/article/3370787) ⚠️环境受限 —— 综述型文章（博客 | P2）

### 7.4 GIS 厂商官方技术资源

- [SuperMap iClient JavaScript 官网](https://iclient.supermap.io/) ⚠️环境受限 —— 超图官方 Web 客户端，含 Cesium/Leaflet/OpenLayers 三套封装与大量示例（厂商官方 | P1）
- [SuperMap 新一代三维 GIS 技术体系](https://www.supermap.com/zh-cn/a/product/10i-tec-3-2021.html) ⚠️环境受限 —— 超图官方三维技术体系介绍，讲主流三维 GIS 技术栈时可引用（厂商官方 | P1）
- [51WORLD 官网](https://www.51world.com/) ✅ —— 数字孪生头部厂商，其行业方案页可了解真实项目形态（厂商官方 | P2）
- [数字冰雹官网](https://www.digitalhailstorm.com/) ✅ —— 大屏可视化与数字孪生厂商，态势平台类产品的参考（厂商官方 | P2）
- 中科星图（GEOVIS）、航天宏图、四维图新：其技术内容多发布于腾讯云开发者社区与 CSDN 专栏，腾讯云侧可访问性更好。例：[中科星图 GVE 案例（腾讯云）](https://cloud.tencent.com/developer/article/2457764) ✅

---

## GIS 前端高频知识自测（36 题）

> 36 题，只列题目 + 一句话答题要点。

### A. Cesium 引擎与选型

1. **Cesium 和 Three.js 有什么区别？为什么 GIS 用 Cesium？** —— Three.js 是通用渲染引擎、无地理基准；Cesium 内置 WGS84 椭球/ECEF 坐标、瓦片 LOD 调度、地形影像服务对接与时间系统，是「地理正确」的三维引擎。
2. **Cesium 的核心对象各自职责？** —— Viewer（应用入口）、Scene（场景与渲染开关）、Camera（相机/视锥）、Entity（数据驱动高层 API）、Primitive（GPU 批次低层 API）、DataSource（数据源）、Provider（影像/地形）。
3. **Cesium 的坐标体系是怎样的？** —— 内部统一用 ECEF 的 `Cartesian3`（米）；`Cartographic` 是经纬高（弧度）；渲染时经模型视图投影矩阵变换到裁剪空间。
4. **模型「飘在空中」或「沉入地下」怎么解决？** —— 高度基准不一致或未做地形贴合；用 `clampToHeightMostDetailed` 或 `sampleTerrainMostDetailed` 采样地形高度纠正。
5. **Cesium 怎么做二三维切换？** —— `scene.morphTo2D()/morphToColumbusView()/morphTo3D()`；注意切换后相机与坐标需重新计算。

### B. 3D Tiles 原理（最高频）

6. **3D Tiles 是什么？解决什么问题？** —— 面向海量异构三维数据流式传输的开放规范（已入 OGC 标准），用 HLOD 树 + 包围体 + 几何误差实现按需加载与按需渲染。
7. **`tileset.json` 有哪些关键字段？** —— `asset`、根 `geometricError`、`root`（递归含 `boundingVolume`/`geometricError`/`refine`/`content.uri`/`children`/`transform`）、`implicitTiling`。
8. **`geometricError` 是什么？怎么决定加载哪一层？** —— 该瓦片对其源几何的简化误差（米），根最大、叶子趋近 0；客户端据此与相机距离算屏幕空间误差 SSE，超过 `maximumScreenSpaceError`（默认 16）就细化。
9. **`refine` 的 ADD 和 REPLACE 有什么区别？** —— REPLACE 用子瓦片替代父瓦片；ADD 父子同时渲染（适合点云/递进细节）；根节点必填，子节点继承。
10. **`boundingVolume` 有哪几种？要注意什么？** —— `region`（经纬高，**弧度**）、`box`（12 个数 OBB）、`sphere`（4 个数）；用于视锥剔除与调度。
11. **`b3dm`/`i3dm`/`pnts`/`cmpt` 分别是什么？现在还用吗？** —— 分别是批量模型/实例化模型/点云/复合瓦片，属 1.0 旧格式；**1.1 起主推 glTF/GLB**，旧格式已 deprecated。
12. **3D Tiles 的 LOD 树可以是哪些空间结构？** —— 四叉树、八叉树、k-d 树、均匀/非均匀网格，甚至隐式瓦片；只要求空间相干性（子瓦片完全在父包围体内）。
13. **什么是隐式瓦片（implicit tiling）？** —— 用 `subdivisionScheme` + 模板 URI + subtree 文件表达规则四叉/八叉树，免去逐瓦片写包围盒，支持随机访问与空间查询。
14. **倾斜摄影 OSGB 怎么转成 3D Tiles？** —— ContextCapture/大疆智图产出 OSGB → 用 `fanvanzh/3dtiles`（开源、跨平台）转 b3dm/glb 并生成 `tileset.json`；注意顶层节点合并与坐标系。
15. **为什么 OSGB 转换前要合并顶层节点？** —— 根节点 children 过多会导致首屏请求数暴增、draw call 过多、调度开销大；合并后可显著提速。

### C. 性能优化

16. **10 万点怎么渲染？** —— 用 `PointPrimitiveCollection`（或 `BufferPointCollection`）批量提交，全部点合并为**一次 draw call**；绝不要用 10 万个 Entity。
17. **Entity 和 Primitive 的性能差异在哪？** —— Entity 是高层封装，每帧需把 `Property` 求值并同步到图形层，易产生大量小批次；Primitive 直接对应 GPU 批次，可复用几何与外观，静态海量数据下快数倍。
18. **什么时候必须用 Entity？** —— 需要时间动态（轨迹回放）、属性绑定、拾取交互、快速原型时；数据量小（数百到数千）时 Entity 开发效率更高。
19. **`requestRenderMode` 是什么？有什么用？** —— 按需渲染：仅在场景变化时出帧，静态态势大屏下 GPU 占用可降到接近 0，大幅降低功耗与发热。
20. **开了 `requestRenderMode` 后画面不刷新怎么办？** —— 主动调用 `scene.requestRender()`；异步数据到位、材质变化、图层增删后都要手动请求；再配 `maximumRenderTimeChange` 控制最大等待。
21. **Cesium 内存泄漏怎么排查和避免？** —— 移除后必须 `destroy()`：`primitives.remove(p)` + `p.destroy()`、`dataSources.remove(ds, true)`、`imageryLayers.remove(layer, true)`；自定义 Primitive 释放 GL 资源；事件监听成对解绑；用 Chrome Memory 快照反复进出场景对比。
22. **3D Tiles 加载慢 / 内存爆怎么调？** —— 调 `maximumScreenSpaceError`（放宽则少加载）、`maximumMemoryUsage`、`cacheBytes`、`maximumNumberOfLoadedTiles`；再配合 Draco 压缩、合并瓦片、减少根节点数量。
23. **瓦片 404 或黑屏怎么排查？** —— Network 面板看请求 URL 与状态码 → 核对 url 模板与瓦片行列号范围 → 检查 TMS/XYZ 与 `TilingScheme` 是否匹配 → 检查坐标系与层级越界 → CORS 跨域 → 服务端切片是否缺失。
24. **内网离线部署要准备什么？** —— 离线影像瓦片服务 + 离线地形（quantized-mesh）+ 3D Tiles 静态服务 + 前端资源本地化；替换 Ion 默认资源为本地 URL 或关闭 Ion，配置正确的 `basePath`/`rootUrl`。

### D. 坐标系

25. **`Cartesian3`、`Cartographic`、WGS84、Web Mercator 的关系？** —— `Cartesian3` 是 ECEF 空间直角坐标（米）；`Cartographic` 是经纬高（弧度）；WGS84 是基准椭球（EPSG:4326）；Web Mercator 是基于 WGS84 的**投影平面坐标**（EPSG:3857）。
26. **CGCS2000 和 WGS84 有什么区别？** —— 椭球参数几乎一致，同一点坐标差异在**厘米级**，工程上常近似等同；但 CGCS2000 是中国法定基准，严格场景应保留 EPSG:4490 标识并正确转换。
27. **GCJ-02 是什么？为什么需要纠偏？** —— 国测局加密坐标系（高德/腾讯底图使用）；原始 WGS84 的 GPS 数据不转 GCJ-02 就在底图上偏移数百米，需用 `gcoord` 等库纠偏（百度底图则是再偏移的 BD-09）。
28. **为什么国内底图上叠加的 GPS 点会整体偏移？** —— 底图是 GCJ-02、数据是 WGS84，基准不一致；统一到同一坐标系后即可对齐。

### E. Mapbox 与 WebGL

29. **Mapbox GL JS 的渲染流程是怎样的？** —— 解析 style → 按 source 管理矢量瓦片缓存 → Worker 池解析 MVT 并做布局/碰撞检测 → 主线程按 layer 顺序用 WebGL 绘制。
30. **矢量瓦片 MVT 相比栅格瓦片有什么优势？** —— 一套瓦片可派生多种样式（换肤无需重切）、体积更小、支持要素级查询与交互、可客户端动态改样式。
31. **Mapbox expression 是做什么的？** —— 声明式表达式语法（`interpolate`/`step`/`match`/`get` 等），实现数据驱动样式与随缩放级别变化的效果。
32. **Mapbox 的点聚合（cluster）原理？** —— GeoJSON source 开启 `cluster: true`，在客户端按 `clusterRadius` 网格聚合，用 `point_count` 做数据驱动样式，避免渲染海量独立点。
33. **Mapbox 的 custom layer 怎么用？** —— `addLayer` 传 `type: 'custom'` 并实现 `render(gl, matrix)`，直接用 WebGL 绘制，可与 Mapbox 共用上下文（three.js 集成同此原理）。
34. **为什么 GIS 选 WebGL 而不是 Canvas 2D？** —— GPU 硬件加速、顶点常驻显存、可一次 draw call 绘制海量要素、着色器可编程、支持实例化；Canvas 在万级图形时即不可用。
35. **写自定义 Primitive 至少需要哪些 WebGL 知识？** —— Buffer/VertexArray 组织顶点、Shader 编译链接、attribute/uniform/varying 传参、MVP 矩阵变换、`drawElements` 索引绘制、资源 `destroy` 释放。
36. **Mapbox 和 Cesium 怎么选？** —— 二维业务、矢量样式驱动、大数据量点选 Mapbox；真三维、地形、倾斜摄影、3D Tiles 流式加载选 Cesium；实际项目常做二三维联动（Mapbox 做底图与二维分析，Cesium 做三维态势）。

---

## 附：结合「三维城市态势平台」的学习顺序

| 阶段 | 重点资料 | 对应项目模块 |
|---|---|---|
| 1 | 第 1.1 节官方 API + Quickstart + Sandcastle | 搭起可运行工程 |
| 2 | 第 2.1 节规范正文 + 章末字段表 + 2.2 节 Essentials | **3D Tiles 加载** |
| 3 | 第 3.1 节 requestRenderMode 官方博客 + 3.2 节海量点 | **10 万点渲染 + 性能优化对比** |
| 4 | 第 3.4 节中文实战 + 3.5 节销毁清单 | 性能对比与内存治理 |
| 5 | 第 4 章坐标系 + gcoord | **历史轨迹回放**的坐标正确性 |
| 6 | 第 5 章 Mapbox + 第 6 章 WebGL | 二三维联动与自定义渲染 |
| 7 | 第 7 章自测题 + 上一节速查 | 知识查漏 |
