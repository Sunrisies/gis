# GIS 前端学习资料清单（视频优先版）

> 配套文件：[`总表.md`](GIS前端60天计划/总表.md) · [`GIS前端60天作战计划.md`](GIS前端60天作战计划.md)
>
> **用法标签：**
> - 📺 **看视频** —— 通勤、午休、睡前看，**视频接收最快**
> - 📖 **碎片读** —— 文档类，工作空闲扫一眼
> - ⌨️ **必须动手** —— 只能整块时间做，看不会

**⚠️ 关于 B站链接：** 视频会失效、UP 主会删稿，而且视频质量差异极大。所以这里给的是**搜索关键词 + 筛选标准**，而不是具体链接——具体链接今天能用，三个月后就 404 了。

---

## 怎么判断一个视频值不值得看

搜索出来一堆结果时，按这四条筛：

| 标准 | 说明 |
|---|---|
| **播放量 1 万以上**，或**收藏/点赞比高** | 收藏多说明真有用，不是标题党 |
| **发布时间在 1 年内** | Cesium / Mapbox 版本更新快，老教程 API 对不上 |
| **有系列合集**，不是单个视频 | 说明系统讲过，不是临时录的 |
| **评论区有人问「代码在哪」且 UP 主回复了** | 说明作者还在维护 |

**看视频的三条纪律（很重要，否则你会看一整天什么都没做出来）：**
1. **1.5–2 倍速，只看你当下卡住的那一节。** 不要「从头看完一个系列」——那是娱乐。
2. **看 15 分钟必须暂停动手。** 视频里敲一遍、你跟着敲一遍。**看完不敲等于没看。**
3. **白天看视频是「预热」，晚上动手才是「消化」。** 两者不能互相替代。

---

## 一、M0 数据处理与工具链（D1–D7）

> 这块**视频远胜文档**，因为全是界面操作，文字说不清。

### 📺 按这些关键词搜
```
QGIS 入门教程          （首选，界面操作必须看视频）
QGIS 坐标系 教程
GDAL ogr2ogr 教程
shp GeoJSON 格式转换
Web墨卡托 原理
坐标系 WGS84 GCJ02 区别      （有图才好懂）
CGCS2000 与 WGS84 区别
```

### 📖 文字只留这些（当字典查，不要通读）
- [ogr2ogr 官方文档](https://gdal.org/programs/ogr2ogr.html) —— `-t_srs` 重投影、`-clipsrc` 裁剪，查参数用
- [GDAL 官方文档](https://gdal.org/) —— 权威参考
- [QGIS 官方文档](https://docs.qgis.org/) —— 重点看「坐标系选择」和「导出数据」
- [proj4js 官网](https://proj4js.org/) —— JS 重投影标准库
- [3D Tiles 官方规范](https://github.com/CesiumGS/3d-tiles) —— 后面 M1 要用

### ⌨️ 必须动手
- [QGIS 下载](https://qgis.org/) —— **Windows 上装 LTR 版**（Mac 装 arm64 版）
- [gcoord](https://github.com/hujiulong/gcoord) —— 国内坐标系纠偏（WGS84 / GCJ-02 / BD-09 互转）

### 公开数据集（M1 要用，提前下好）
- [OpenTopography](https://portal.opentopography.org/dataCatalog) —— **免费 DEM / 点云**，切片首选
- [Cesium ion](https://cesium.com/platform/cesium-ion/) —— 免费额度，上传自动切片，**切完可下载本地部署**
- [Cesium ion 3D Buildings](https://cesium.com/learn/3d-tiling/ion-tile-3d-buildings/) —— 官方示例 3D Tiles 建筑
- [OSGeo 中国](https://www.osgeo.cn/) —— 中文 GIS 资料与数据入口

---

## 二、M1 切片与 3D Tiles（D8–D14）

> 切片是**纯操作**，看视频照着做最快。

### 📺 按这些关键词搜
```
3D Tiles 原理
3D Tiles 切片 教程
Cesium 加载 3D Tiles
倾斜摄影 OSGB 转 3DTiles
点云 切片 3DTiles
gdal2tiles 影像切片
tippecanoe 矢量瓦片
Cesium 从入门到实战       （找系列合集）
```

> **为什么搜不到「CesiumLab」**：那是闭源商业软件，本项目不用它（理由见下）。
> 搜开源方案的关键词，视频少但每一条都能落到命令行上。

### 📖 文字
- [3D Tiles 官方规范](https://github.com/CesiumGS/3d-tiles) —— `boundingVolume` / `geometricError` / refine 的权威定义
- [Cesium 官方 3D Tiling 教程](https://cesium.com/learn/3d-tiling/) —— 官方讲切片
- [glTF 规范](https://www.khronos.org/gltf/) —— 3D Tiles 内部的模型格式
- [**公开数据下载清单**](公开数据下载清单.md) —— **切片前先来这里选数据**，每个环节 3 条以上下载路径

### ⌨️ 必须动手
- [fanvanzh/3dtiles](https://github.com/fanvanzh/3dtiles) —— **本项目切片主力**：OSGB/SHP/FBX → 3D Tiles，**Mac + Windows + Docker 全平台**，开源
- [py3dtiles（GitLab）](https://gitlab.com/py3dtiles/py3dtiles) —— 点云 LAS → 3D Tiles，纯 Python，**Apple Silicon 免编译**
- [3d-tiles-tools](https://github.com/CesiumGS/3d-tiles-tools) —— 官方 Node 工具链，Mac 可用
- [3d-tiles-validator](https://github.com/CesiumGS/3d-tiles-validator) —— **切片产出后必跑**，能揪出「Cesium 空白但控制台不报错」的问题
- [gdal2tiles](https://manpages.debian.org/testing/gdal-bin/gdal2tiles.1.en.html) —— GeoTIFF → XYZ 影像瓦片，GDAL 自带
- [Cesium Sandcastle](https://sandcastle.cesium.com/) —— **你这 63 天用得最多的资源**，几乎所有功能都有可跑示例
- [glTF Viewer](https://gltf-viewer.donmccurdy.com/) —— 打开模型看结构

> **不用 CesiumLab 的原因**：闭源商业软件，免费版有功能限制，切片参数不透明。
> **面试时你只能回答「我点了这个按钮」**，答不出 `geometricError` 怎么定、LOD 怎么分。
> 换成开源命令行方案后，每个参数你都能解释——这才是这个项目要沉淀的东西。

---

## 三、M2 Vue3 × Cesium（D15–D28）

### 📺 按这些关键词搜
```
Cesium 组件封装 Vue
Cesium 态势标绘
Cesium 绘制 点线面
Cesium 贴地 clampToGround
Vue3 响应式原理            （有动画演示依赖收集，比读文档快）
Vue3 源码解析
Vue3 Composition API 封装
Cesium 图层管理
```

### 📖 文字
- [Vue3 · 深入响应式系统](https://cn.vuejs.org/guide/extras/reactivity-in-depth.html) —— **中文官方，M2 第一份材料**
- [Vue3 · 渲染机制](https://cn.vuejs.org/guide/extras/rendering-mechanism.html) —— Block Tree / patchFlag / 静态提升
- [Vue3 · Composition API FAQ](https://cn.vuejs.org/guide/extras/composition-api-faq.html) —— 抽 composable 前必读
- [CesiumJS 官方文档](https://cesium.com/learn/cesiumjs/ref-doc/) —— API 字典

### ⌨️ 必须动手
- [Cesium Sandcastle](https://sandcastle.cesium.com/) —— 找 Drawing / Picking 相关示例
- [geojson.io](https://geojson.io/) —— **验证你导出的 GeoJSON 是否合法**（M2 验收要用）

---

## 四、M3 性能优化（D29–D42）

> **这块视频说服力最强**，因为能直接看到帧率变化。

### 📺 按这些关键词搜
```
Cesium 性能优化
Cesium requestRenderMode
Cesium 海量点 渲染
Cesium 点聚合
Cesium Entity Primitive 区别
Cesium 内存泄漏
Cesium CustomShader
Chrome Performance 性能分析
```

### 📖 文字
- [Cesium 官方 · requestRenderMode](https://cesium.com/learn/cesiumjs/ref-doc/Viewer.html) —— 按需渲染说明
- [CustomShader 官方文档](https://cesium.com/learn/cesiumjs/ref-doc/CustomShader.html)
- [Chrome Performance 面板指南](https://developer.chrome.com/docs/devtools/performance/) —— **性能数据怎么测才可信**
- [web.dev · Core Web Vitals](https://web.dev/articles/vitals) —— LCP / INP / CLS

### ⌨️ 必须动手
- [Scene Rendering Performance 官方示例](https://cesium.com/downloads/cesiumjs/releases/1.134/Apps/Sandcastle/gallery/Scene%20Rendering%20Performance.html) —— **M3 直接拿来改**

---

## 五、M4 Mapbox（D43–D49）

### 📺 按这些关键词搜
```
Mapbox GL JS 教程
Mapbox 矢量瓦片 原理
Mapbox 数据驱动样式 expression
Mapbox 点聚合 cluster
Mapbox 自定义图层 WebGL
Cesium Mapbox 选型 对比
```

### 📖 文字
- [Mapbox GL JS 官方文档](https://docs.mapbox.com/mapbox-gl-js/api/)
- [Mapbox Style 规范](https://docs.mapbox.com/style-spec/guides/) —— Style JSON 与 expression
- [Mapbox 矢量瓦片介绍](https://docs.mapbox.com/data/tilesets/guides/vector-tiles-introduction/) —— MVT 原理

### ⌨️ 必须动手
- [Mapbox 官方示例库](https://docs.mapbox.com/mapbox-gl-js/example/) —— custom layer / cluster 示例
- [Mapbox custom layer 示例](https://docs.mapbox.com/mapbox-gl-js/example/custom-style-layer/)

---

## 六、M5 Rust / WASM（D50–D56）

> **只看这几条，不要扩展到「系统学 Rust」。** Rust 在这个项目里是**一个故事**，不是一门要学完的技能。

### 📺 按这些关键词搜
```
Rust 入门 所有权 借用        （只看这三章）
WebAssembly 实战
wasm-bindgen 教程
Rust 前端 性能优化
wasm-pack 打包
```

### 📖 文字
- [Rust 程序设计语言（中文版）](https://kaisery.github.io/trpl-zh-cn/) —— 只看所有权 / 借用 / 生命周期三章
- [Rust and WebAssembly 官方书](https://rustwasm.github.io/docs/book/) —— **WASM 主线教材**
- [wasm-bindgen 指南](https://rustwasm.github.io/docs/wasm-bindgen/) —— `Float64Array` 传参看这
- [JS 与 Rust 共享内存的真实讨论](https://github.com/wasm-bindgen/wasm-bindgen/issues/2456) —— **M5 讲边界成本的素材**
- [Douglas-Peucker 算法](https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm) —— 轨迹抽稀算法

### ⌨️ 必须动手
- [wasm-pack 官方文档](https://rustwasm.github.io/docs/wasm-pack/) —— 工具链（⚠️ 注意：旧地址 `rustwasm.github.io/wasm-pack/` 已 404，必须带 `/docs/`）
- [**Number Slices（`&[f64]` ↔ `Float64Array`）**](https://rustwasm.github.io/docs/wasm-bindgen/reference/types/number-slices.html) —— **M5 最重要的一页**：真正的零拷贝传参。注意它返回的是**视图**，只在调用期间有效，JS 不能长期持有
- [BoxedNumberSlice（`Box<[f64]>`）](https://rustwasm.github.io/docs/wasm-bindgen/reference/types/boxed-number-slices.html) —— 所有权移交 JS，**可长期持有**，代价是一次分配（决定你用哪个）
- [Calls between JS and WebAssembly are finally fast](https://hacks.mozilla.org/2018/10/calls-between-javascript-and-webassembly-are-finally-fast-%F0%9F%8E%89/) —— 结论：**别在循环里频繁跨界，要批量化**
- [How to NOT WebAssembly](https://mcyoung.xyz/2023/08/01/wasm-wtf/) —— 「编译到 wasm 后反而更慢」的具体机制，M5 边界成本的素材

---

## 七、M6 工程化与部署（D57–D63）

### 📺 按这些关键词搜
```
Vite 构建优化 拆包
Vite 插件开发
前端性能优化 首屏
3D Tiles 部署 服务器
nginx 发布 瓦片服务
```

### 📖 文字
- [Vite 构建文档](https://cn.vitejs.dev/guide/build.html) —— 拆包与产物
- [Vite 静态部署](https://cn.vitejs.dev/guide/static-deploy.html) —— 各平台配置
- [**Vercel 文件大小限制**](https://vercel.com/docs/limits) —— **部署 3D Tiles 前必看**，避免白忙

### ⌨️ 必须动手
- [rollup-plugin-visualizer](https://github.com/btd/rollup-plugin-visualizer) —— 体积分析，Cesium 巨包必用

**⚠️ 部署坑（提前知道能省一天）：** 3D Tiles 动辄几百 MB 到几 GB，**Vercel / Netlify 有体积限制**。预案：瓦片走对象存储（OSS / S3）+ CDN，前端页面单独部署；或整体自建 nginx。

---

## 八、算法（零基础，M0–M6 全程）

> 你几乎没写过算法，**只走一条主线，不要多头并进**。

### 📺 按这些关键词搜
```
代码随想录              （有官方视频，跟着刷）
Hello 算法              （有配套动画，最适合碎片看）
LeetCode 新手 刷题路线
labuladong 算法小抄
双指针 滑动窗口 模板
二叉树 递归 套路
动态规划 入门
```

### 📖 / ⌨️
- [代码随想录](https://programmercarl.com/) —— **首选主线**。按专题组织、有刷题顺序、有 JS 版本
- [Hello 算法](https://www.hello-algo.com/) —— **最适合白天碎片读**，图解友好
- [LeetCode 中文站](https://leetcode.cn/) —— 刷题平台
- [labuladong 算法小抄](https://labuladong.online/) —— 讲套路框架，模板很好
- [CodeTop](https://codetop.cc/) —— 按公司/频率排序的高频题

**具体 40 题清单见 [`总表.md`](GIS前端60天计划/总表.md) 第三节。**

**JS 写算法题的三个坑（先记住，能省你几小时）：**
1. `arr.sort()` 默认按**字符串字典序**，数字排序必须 `sort((a, b) => a - b)`
2. `Array(n).fill([])` 填的是**同一个引用**，会互相污染，要用 `Array.from({length: n}, () => [])`
3. 深拷贝用 `structuredClone()`，别手写 JSON 转换（会丢 `undefined` / `Date` / 循环引用）

---

## 九、全部搜索关键词（一次性复制去搜）

```
QGIS 入门教程
QGIS 坐标系
GDAL ogr2ogr 教程
坐标系 WGS84 GCJ02
CGCS2000 WGS84 区别
Web墨卡托 原理
3D Tiles 原理
倾斜摄影 3DTiles 切片
点云 切片 3DTiles
gdal2tiles 影像切片
Cesium 从入门到实战
Cesium 组件封装 Vue
Cesium 态势标绘
Cesium 性能优化
Cesium 海量点
Cesium CustomShader
Vue3 响应式原理
Vue3 源码解析
Mapbox GL JS 教程
Mapbox 矢量瓦片
Mapbox 自定义图层
Rust 入门 所有权
WebAssembly 实战
wasm-bindgen 教程
Vite 构建优化
代码随想录
Hello 算法
前端 三维可视化
GIS 前端 项目复盘
```
