/**
 * 生成项目用的合成数据（固定随机种子，保证可复现）
 *
 * 用法： node scripts/gen-data.js
 * 输出： data/raw/points-100k.json   10 万个点，D22 海量点渲染用
 *       data/raw/track-100k.json    10 万个带时间戳的轨迹点，D23 轨迹回放用
 *
 * 为什么自己造而不用真实数据：
 *   M3 性能对比需要「同一份数据反复测 5 次」，固定种子才能跨机器复现。
 *   公开 GPS 轨迹需申请、涉及隐私、且多是 GCJ-02 还得先纠偏。
 */
const fs = require('fs');
const path = require('path');

// 线性同余伪随机 —— 固定种子，每次生成结果完全一致
function makeRnd(seed) {
  return () => { seed = (seed * 1103515245 + 12345) % 2147483648; return seed / 2147483648; };
}

const outDir = path.join(__dirname, '..', 'raw');
fs.mkdirSync(outDir, { recursive: true });

// ---------- ① 10 万个点（高程 0~500m）----------
{
  const rnd = makeRnd(42);
  const N = 100000, pts = [];
  for (let i = 0; i < N; i++) {
    pts.push([
      +(118 + rnd() * 8).toFixed(6),
      +(28 + rnd() * 8).toFixed(6),
      +(rnd() * 500).toFixed(2),
    ]);
  }
  fs.writeFileSync(path.join(outDir, 'points-100k.json'), JSON.stringify(pts));
  console.log(`points-100k.json   ${N} 个点`);
}

// ---------- ② 10 万个带时间戳的轨迹点（杭州西湖附近绕圈）----------
{
  const rnd = makeRnd(7);
  const N = 100000, t0 = Date.UTC(2026, 0, 1), pts = [];
  for (let i = 0; i < N; i++) {
    const t = i / N * Math.PI * 4;          // 绕 2 圈
    const r = 0.01 + Math.sin(t * 3) * 0.004;
    pts.push([
      +(120.15 + Math.cos(t) * r + (rnd() - 0.5) * 1e-5).toFixed(6),
      +(30.25 + Math.sin(t) * r + (rnd() - 0.5) * 1e-5).toFixed(6),
      +(20 + Math.sin(t * 10) * 5).toFixed(2),
      t0 + i * 1000,                        // 每点间隔 1 秒
    ]);
  }
  fs.writeFileSync(path.join(outDir, 'track-100k.json'), JSON.stringify(pts));
  console.log(`track-100k.json    ${N} 个带时间戳的点`);
}
