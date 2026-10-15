# Day 14｜2026-11-01 周日｜M1 切片与链路

## 今日主题：切片实战：自己切出 3D Tiles → Cesium 加载

**今天是大块日：4–6 小时。** 中途不要切任务，一鼓作气做完。

> **重要**：今天**全程在 Mac 上就能完成**，不需要 Windows。
> 用的是开源命令行方案（`fanvanzh/3dtiles` / `py3dtiles`），不是 CesiumLab。

---

> 📦 **数据已下载好**：见 [`data/数据使用说明.md`](../../data/数据使用说明.md)

## 一、先看数据（**已下载好，不用再下**）

```bash
cd data/raw
ls 3d-tiles-samples/ *.las
```
- `3d-tiles-samples/` —— 官方样例瓦片（10 个 tileset，含 b3dm / pnts）
- `*.las` —— 4 个真实激光点云（**这就是你 D14 要切的原始数据**）

<details><summary>如果还想下别的数据（点开看）</summary>


### 路线 A：官方示例瓦片（**最省事，推荐先用它跑通**）

```bash
git clone https://github.com/CesiumGS/3d-tiles-samples.git
# 单个体积很小，含 1.0 与 1.1 两版样例
```
- 地址：https://github.com/CesiumGS/3d-tiles-samples
- **优点**：免注册、秒下、自带 `tileset.json`，能立刻验证前端链路
- **用途**：先确认「Cesium 能加载 3D Tiles」这件事没问题，再去折腾切片

### 路线 B：Cesium ion 免费资产（**要真实倾斜摄影就用它**）

```bash
# 登录后在 Asset Depot 里「Add to my assets」
open https://ion.cesium.com/assetdepot
```
- 地址：https://ion.cesium.com/assetdepot
- **免费领取**：Cesium OSM Buildings（全球建筑白模）、Cesium World Terrain（全球地形）、
  **Aerometrex 旧金山/丹佛倾斜摄影**（真实倾斜摄影数据）
- **额度**（已核实）：存储 10 GB、流量 15 GB/月、Asset Depot 裁剪 10 次/月
- **注意**：需要用 ion 的 assetId 加载，或下载后本地发布

### 路线 C：点云数据自己切（**想练「真·切片」就用它**）

```bash
git clone https://github.com/PDAL/data.git
# 里面全是几 MB 的 LAS/LAZ，免注册
```
- 地址：https://github.com/PDAL/data
- **用途**：用 `py3dtiles` 把 LAS 切成 `pnts`，这是**你自己产出的第一份 3D Tiles**

> 更多数据源（DEM / 影像）见 [`公开数据下载清单.md`](../../公开数据下载清单.md)。

</details>

---

## 二、今日任务（按顺序做）

### 第一步：装工具（约 40 分钟）

```bash
# 1) 点云切片（纯 Python，Apple Silicon 免编译）
pip install py3dtiles

# 2) OSGB/SHP → 3D Tiles（Mac 可用，也可用 Docker）
brew install fanvanzh/3dtiles/3dtiles
# 或者用 Docker（推荐，省去编译）
docker run --rm -v $(pwd):/data fanvanzh/3dtiles:latest

# 3) 官方校验器（切片产出后必跑）
npm install -g 3d-tiles-tools
```

### 第二步：切片（约 60 分钟）

```bash
# 点云路线：LAS → 3D Tiles
py3dtiles convert data/raw/pointcloud.las --out data/tiles/

# 或者 shp 白模路线（如果有建筑轮廓 + 高度字段）
3dtiles -f Shapefile -i buildings.shp -o data/tiles/
```

**切片时必须想清楚这三个参数**（面试会问）：
- **坐标系**：输出用 EPSG:4326 还是 4490？为什么？
- **最大层级 / geometricError**：怎么定的？定大了会怎样？
- **是否压缩**：Draco 开了吗？代价是什么？

### 第三步：校验（约 20 分钟）

```bash
npx 3d-tiles-validator --tilesetFile data/tiles/tileset.json
```
**这一步不能跳。** 切片工具的产物经常有结构问题，直接丢给 Cesium 会「一片空白但控制台不报错」。

### 第四步：发布 + 加载（约 60 分钟）

```bash
cd data/tiles && python3 -m http.server 8080
# ⚠️ 必须用 HTTP，不能用 file://（CORS 会拦死）
```
浏览器验证：`http://localhost:8080/tileset.json` 应返回 JSON。

Cesium 里加载：
```js
const tileset = await Cesium.Cesium3DTileset.fromUrl('http://localhost:8080/tileset.json')
viewer.scene.primitives.add(tileset)
viewer.zoomTo(tileset)
```

### 第五步：验证（约 20 分钟）

打开 Network 面板，**确认 `tileset.json` 返回 200**，并截图。

## 三、产出（必须留下，否则等于没做）

- [ ] `data/tiles/tileset.json`（自己切出来的，不是拷的）
- [ ] 校验器通过的输出记录
- [ ] 本地瓦片服务
- [ ] Cesium 能加载显示的页面
- [ ] Network 截图（`tileset.json` = 200）
- [ ] 三个参数的取值与理由（写进 `docs/01-切片流程.md`）

> 今天不是算法日（算法固定在 **周二 / 周四 / 周日**）。

## 四、参考资料

📺 B站搜「3D Tiles 切片」「点云 切片 3DTiles」「倾斜摄影 OSGB 转 3DTiles」
📖 [公开数据下载清单](../../公开数据下载清单.md) · [fanvanzh/3dtiles](https://github.com/fanvanzh/3dtiles) · [py3dtiles](https://gitlab.com/py3dtiles/py3dtiles) · [3d-tiles-samples](https://github.com/CesiumGS/3d-tiles-samples)

## 五、验收标准（怎么证明今天真做完了）

✅ Network 里 `tileset.json` 是 200
✅ 三维模型可见且不糊
✅ 能讲清 `geometricError` 和 `refine`
✅ **能说出切片时三个参数为什么这么定**
⚠️ 如果切片卡住：**先用路线 A 的公开数据集跑通前端**，切片挪到下周日

---

## 今日记录（自己填）

```
## D14 复盘
用了哪条数据路线：A / B / C
切片参数（坐标系 / geometricError / 压缩）：
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
