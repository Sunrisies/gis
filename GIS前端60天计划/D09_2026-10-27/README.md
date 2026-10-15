# Day 9｜2026-10-27 周二｜M1 切片与链路

## 今日主题：3D Tiles 字段精读：tileset.json

**今天预算 1–1.5 小时。** 切法：5min 找回上下文 → 70min 主线 → 15min 记录。

---

## 一、今日任务（按顺序做）

> 📦 **样例瓦片已下载好**：`data/raw/3d-tiles-samples/`，详见 [`data/数据使用说明.md`](../../data/数据使用说明.md)

### 今天就读这个文件

```bash
cd data/raw/3d-tiles-samples/TilesetWithDiscreteLOD
python3 -m json.tool tileset.json | head -40
```

这份样例**刚好覆盖你要学的全部字段**：

| 字段 | 值 | 要想清楚的问题 |
|---|---|---|
| `asset.version` | `1.0` | 1.0 和 1.1 差在哪 |
| `geometricError`（根） | `500` | |
| `root.geometricError` | `1` | **为什么根是 500、root 只有 1？** |
| `root.refine` | `REPLACE` | 换成 ADD 会怎样 |
| `root.boundingVolume` | `{box: [...]}` | box 是 12 个数，分别代表什么 |
| `root.content.uri` | `dragon_low.b3dm` | 为什么是 low 而不是 high |
| `root.children` | 1 个 | 顺着往下看，一共几级 |

1. 读官方规范，搞清 `boundingVolume`（三种：box / region / sphere）
2. 搞清 `geometricError` 的含义：它决定什么时候加载下一级
3. 搞清 `refine`：ADD 和 REPLACE 的区别（**高频考点**）
4. **对照上面这个真实文件逐字段验证**，写进 `docs/01-切片流程.md`

> 换一个再看：`TilesetWithRequestVolume/`（含 `viewerRequestVolume`）、
> `TilesetWithFullMetadata/`（3D Tiles 1.1 的元数据）

## 二、产出（必须留下，否则等于没做）

- [ ] `docs/01-切片流程.md` 的 3D Tiles 字段详解段落

> 今天不是算法日（算法固定在 **周二 / 周四 / 周日**）。

## 三、参考资料

📖 [3D Tiles 规范](https://github.com/CesiumGS/3d-tiles) · ⌨️ [3d-tiles-tools](https://github.com/CesiumGS/3d-tiles-tools)

## 四、验收标准（怎么证明今天真做完了）

✅ 指着 `tileset.json` 能说出每个字段干什么，能讲清 ADD vs REPLACE

---

## 今日记录（自己填）

```
## D9 复盘
实际投入：__h
产出是否可演示：是/否 —— 链接或文件：
卡住的点（具体到技术名词）：
明天第一件事：
精力（1-5）：
```
