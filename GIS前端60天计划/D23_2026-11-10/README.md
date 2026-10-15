# Day 23｜2026-11-10 周二｜M2 页面与交互

## 今日主题：轨迹回放：数据与插值

**今天预算 1–1.5 小时。** 切法：5min 找回上下文 → 70min 主线 → 15min 记录。

---

## 一、今日任务（按顺序做）

1. 准备轨迹数据（经纬度 + 时间戳序列）
2. 实现时间插值：给定时刻算出位置（这个逻辑后面要给 Rust 做）
3. 实现回放控制：播放/暂停/倍速/进度条

### 轨迹数据从哪来（三条任选）

**① 自己造 —— 最推荐**（公开 GPS 轨迹要么需申请、要么涉及隐私、要么是 GCJ-02 得纠偏）
```bash
node -e "
const fs=require('fs'), N=100000, pts=[], t0=Date.now();
const lon0=120.15, lat0=30.25;           // 杭州西湖附近
for(let i=0;i<N;i++){
  const t=i/N*Math.PI*4, r=0.01+Math.sin(t*3)*0.004;
  pts.push([
    120.15+Math.cos(t)*r+(Math.random()-0.5)*1e-5,
    30.25+Math.sin(t)*r+(Math.random()-0.5)*1e-5,
    20+Math.sin(t*10)*5,
    t0+i*1000                          // 每点间隔 1 秒
  ]);
}
fs.writeFileSync('data/raw/track-100k.json', JSON.stringify(pts));
console.log('生成', N, '个带时间戳的点');
"
```
带时间戳（第 4 个字段）才能做插值回放，也是后面给 Rust 做抽稀的输入。

**② OpenStreetMap GPS 轨迹**（真实、免注册）
- https://www.openstreetmap.org/traces —— 公开 GPS traces，按区域下载 `.gpx`
- Cesium 可直接用 `Cesium.GpxDataSource.load()` 加载

**③ 移动端自己录**（最真实，但要花时间）
- 手机装 GPS Logger / GPX Viewer，走一段路导出 GPX
- **注意坐标系**：手机输出是 WGS84，若叠在高德/腾讯底图上必须纠偏（回到 D5）

> 更多数据源见 [`公开数据下载清单.md`](../../公开数据下载清单.md)

## 二、产出（必须留下，否则等于没做）

- [ ] 轨迹回放功能（能播放）

> 今天不是算法日（算法固定在 **周二 / 周四 / 周日**）。

## 三、参考资料

📖 [Cesium 文档](https://cesium.com/learn/cesiumjs/ref-doc/) · 📺 B站搜「Cesium 轨迹回放」

## 四、验收标准（怎么证明今天真做完了）

✅ 轨迹能动起来，进度条能拖动

---

## 今日记录（自己填）

```
## D23 复盘
实际投入：__h
产出是否可演示：是/否 —— 链接或文件：
卡住的点（具体到技术名词）：
明天第一件事：
精力（1-5）：
```
