# 前端工程师三块学习资料清单（算法零基础 / Vue3 原理 / Rust-WASM）

> **链接核验说明**：本文所有链接均用 `curl` 实测（`web_fetch` 在本机被本地代理拦截，无法使用）。
> `✅` = 实测 HTTP 200 可访问；`⚠️` = 站点真实存在但本机 DNS/代理被拦截或触发反爬（403/429），**请在浏览器里自行确认一次**。
> 题号与题名已用 LeetCode 全量题目数据集（4082 题，`frontend_id`/`title_slug`/`difficulty` 字段）逐条比对，**40 题全部准确**。

**你的约束**：每周 3 次 × 40 分钟、同一题做 3 遍 ⇒ 40 题 ≈ **13–14 周（约 3 个月）**。下面所有资料都按「能砍就砍」的原则标了 P0/P1/P2，**只做 P0 就够**。

---

## A. 算法（零基础 · JS · 40 题）

### A.1 刷题平台

- [LeetCode 中文站（力扣）](https://leetcode.cn/problemset/) ⚠️ —— 主战场，题目 + 讨论区 + 官方题解（平台 | P0）
- [力扣「热题 100」题单](https://leetcode.cn/studyplan/top-100-liked/) ⚠️ —— 面试高频题官方聚合页，本文题单基本是它的子集（题单 | P1）
- [代码随想录 · 在线站](https://programmercarl.com/) ✅ —— 中文零基础第一站，每个专题都有「理论基础 → 实战题 → 总结」三步走（教程 | P0）
- [代码随想录 · 卡码网](https://kamacoder.com/) ⚠️ —— 配套的在线判题站，含 ACM 输入输出模式练习；本机被 DNS 拦截，**能打开就用，打不开就跳过**（平台 | P2）
- [Hello 算法](https://www.hello-algo.com/) ⚠️（429 限流）—— 动画图解 + 可运行代码，**当字典查，不要通读**（教程 | P1）
- [Hello 算法 · GitHub 仓库](https://github.com/krahets/hello-algo) ✅ —— 上面站点的仓库版（教程 | P1）
- [labuladong 的算法小抄（新站）](https://labuladong.online/algo/) ✅ —— 「框架思维」最强，模板讲得最好；缺点是不适合零基础第一周（教程 | P1）
- [labuladong · GitHub 仓库（旧版）](https://github.com/labuladong/fucking-algorithm) ✅ —— 纯 Markdown、无广告，离线可读（教程 | P2）
- [CodeTop](https://codetop.cc/home) ⚠️ —— 按**公司 + 部门**统计高频题的频度榜，找工作时用来定向复习（平台 | P2）
- [洛谷](https://www.luogu.com.cn/) ✅ —— OI 竞赛向，题目偏难、偏数学，**对「面试 + 零基础」不适合，不推荐**（平台 | P2 不用）
- [OI Wiki](https://oi-wiki.org/) ✅ —— 算法知识百科，需要查某个概念的严谨定义时用（参考 | P2）
- [NeetCode](https://neetcode.io/practice) ✅ —— 英文，按「模式」分类并配视频，英文还行可作补充（平台 | P2）

### A.2 零基础路线：哪个最适合你

| 资料 | 适合谁 | 结论 |
|---|---|---|
| **代码随想录** | 零基础、时间碎片化 | ✅ **你的主路线**。专题顺序就是刷题顺序，每题有文字 + 视频，不用自己排计划 |
| **Hello 算法** | 想先懂「为什么」 | 图解最好，但**全书太厚**。只用来查：链表/树/栈/二分/DP 这 5 章的开头 2 页 |
| **labuladong** | 已会写基础题、想提速 | 「回溯/DP/滑动窗口」的框架模板最省脑子，**第 4 周之后再上** |

**代码随想录推荐专题顺序（前 9 个专题就是本文题单顺序）**：
数组 → 链表 → 哈希表 → 字符串 → 双指针 → 栈与队列 → 二叉树 → 回溯 → 贪心 → 动态规划 → 单调栈 → 图论。
零基础 + 时间少，**只做前 9 个里的「数组/哈希/双指针/滑动窗口/链表/二叉树/栈/二分/DP/回溯」即可，图论和贪心直接跳过。**

- [代码随想录 · 数组理论基础](https://programmercarl.com/%E6%95%B0%E7%BB%84%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html) ✅ —— 感受一下它的行文风格，这就是你未来 3 个月的教材（教程 | P0）
- [代码随想录 · 知识星球/学习路线](https://programmercarl.com/other/kstar.html) ✅ —— 官方学习路线与学习方法（教程 | P2）

### A.3 JS 专用：API 速查 + 常见坑

**API 速查（只看这几页，别背）**

- [MDN · Array（中文）](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array) ✅ —— 重点 `push/pop/shift/unshift/slice/splice/sort/fill/map/filter/reduce/includes/indexOf/lastIndexOf/join/reverse`（速查 | P0）
- [MDN · Map（中文）](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Map) ✅ —— `set/get/has/delete/size/keys/values/entries`；**哈希题首选**（速查 | P0）
- [MDN · Set（中文）](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Set) ✅ —— `add/has/delete/size`；去重一行 `[...new Set(arr)]`（速查 | P0）
- [MDN · String（中文）](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String) ✅ —— 重点 `charCodeAt/split/slice/substring/substring/padStart/repeat/startsWith`（速查 | P1）

**JS 写算法题的 8 个坑（按踩坑概率排序）**

1. **`sort()` 默认按字典序**，`[10, 9, 1].sort()` → `[1, 10, 9]`。**永远写 `arr.sort((a, b) => a - b)`**。
   - [MDN · Array.prototype.sort()（中文）](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) ✅
2. **二维数组初始化**：`new Array(m).fill([])` 会让 m 行**共享同一个数组引用**！正确写法：
   ```js
   const dp = Array.from({ length: m }, () => new Array(n).fill(0));
   ```
3. **浮点数**：`0.1 + 0.2 !== 0.3`。比较用 `Math.abs(a - b) < 1e-9`；`x ** 0.5` 求平方根后要 `Math.floor` 再验证。
   - [0.30000000000000004.com](https://0.30000000000000004.com/) ✅ ｜ [MDN · Number.EPSILON](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON) ✅
4. **深浅拷贝**：浅拷贝 `[...arr]` / `arr.slice()` / `Object.assign({}, o)`；深拷贝 `structuredClone(obj)`。回溯题 `path.slice()` 再 `push`，否则答案全是同一个数组的引用。
   - [MDN · structuredClone](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/structuredClone) ✅
5. **`Map.get` 取不到返回 `undefined`**，值可能是 `0` 或 `''`，判断存在要用 `map.has(k)`，不要 `if (map.get(k))`。
6. **位运算会截断为 32 位有符号整数**。`(l + r) >> 1` 对数组下标安全；但涉及大数要用 `Math.floor((l + r) / 2)`。超过 `2^53 - 1` 用 `BigInt`。
   - [MDN · Number.MAX_SAFE_INTEGER](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER) ✅
7. **字符串不可变**：`s[i] = 'x'` 无效。要么 `s.split('')` 改数组，要么直接用 `+` 拼。
8. **递归栈深度**约 1 万层。LeetCode 的树够用，但**长链表递归（如 #206 反转链表）要写迭代版**，别在面试时爆栈。

### A.4 35–40 题精选题单（共 40 题，无困难题）

> 使用方式：**同一题做 3 遍**。
> **第 1 遍**（当天 25 min）：想 10 分钟，不会就看题解，然后**合上题解重写一遍**。
> **第 2 遍**（2–3 天后）：不看题解写出来，卡住只看一眼关键思路。
> **第 3 遍**（1–2 周后）：白板/空白文件从零默写模板并跑通。
> 每次 40 min 的分配建议：**1 道新题（25 min）+ 1 道旧题的第 2/3 遍（15 min）**。

| 序号 | 题号 | 题名 | 专题 | 难度 | 为什么值得做 |
|---|---|---|---|---|---|
| 1 | 1 | 两数之和 | 哈希 | 简单 | 哈希表第一课，第一次体会「用空间换时间」 |
| 2 | 217 | 存在重复元素 | 哈希 | 简单 | Set 判重的最小用例，3 分钟能写完，建立信心 |
| 3 | 242 | 有效的字母异位词 | 哈希计数 | 简单 | 「数组当哈希表」的标准范式（26 个字母） |
| 4 | 349 | 两个数组的交集 | 哈希 | 简单 | Set 的 `has` 用法，JS 里一行式写法值得记 |
| 5 | 49 | 字母异位词分组 | 哈希计数 | 中等 | 把「计数结果」当 key，哈希从会用变成会设计 |
| 6 | 26 | 删除有序数组中的重复项 | 双指针 | 简单 | 快慢指针原地去重，第一次理解双指针为什么快 |
| 7 | 27 | 移除元素 | 双指针 | 简单 | #26 的更短版本，同一天连着做加深印象 |
| 8 | 283 | 移动零 | 双指针 | 简单 | #26/#27 的变体，练「原地 + 交换」 |
| 9 | 15 | 三数之和 | 双指针 | 中等 | 排序 + 对撞 + 去重，双指针集大成，**本文档最重要的一题** |
| 10 | 3 | 无重复字符的最长子串 | 滑动窗口 | 中等 | 可变窗口求**最长**，滑动窗口模板源头 |
| 11 | 209 | 长度最小的子数组 | 滑动窗口 | 中等 | 可变窗口求**最短**，和 #3 配对记忆 |
| 12 | 643 | 子数组最大平均数 I | 滑动窗口 | 简单 | 定长窗口最简单一题，先搞懂「进窗/出窗」 |
| 13 | 438 | 找到字符串中所有字母异位词 | 滑动窗口 + 哈希 | 中等 | 定长窗口 + 计数，滑动窗口收官题 |
| 14 | 203 | 移除链表元素 | 链表 | 简单 | 虚拟头结点 `dummy` 的入门，链表的第一个坎 |
| 15 | 206 | 反转链表 | 链表 | 简单 | 双指针改指针方向，**必须能默写** |
| 16 | 21 | 合并两个有序链表 | 链表 | 简单 | `dummy` + 双指针，链表题最通用的套路 |
| 17 | 141 | 环形链表 | 链表 | 简单 | Floyd 快慢指针判圈，思维方式很有启发 |
| 18 | 142 | 环形链表 II | 链表 | 中等 | 判环 + 找入口，纯逻辑推导，面试常考 |
| 19 | 94 | 二叉树的中序遍历 | 二叉树递归 | 简单 | 递归三部曲的最小样例 |
| 20 | 144 | 二叉树的前序遍历 | 二叉树递归 | 简单 | 和 #94 对照，理解前/中/后序只是「访问位置」不同 |
| 21 | 104 | 二叉树的最大深度 | 二叉树递归 | 简单 | 后序「自底向上返回值」范式，树题的地基 |
| 22 | 226 | 翻转二叉树 | 二叉树递归 | 简单 | 交换左右孩子，验证你是否真的会递归 |
| 23 | 102 | 二叉树的层序遍历 | 二叉树递归 | 中等 | BFS + 按层分组，树的另一半江山 |
| 24 | 20 | 有效的括号 | 栈 | 简单 | 栈的入门题，「后进先出」匹配类问题原型 |
| 25 | 1047 | 删除字符串中的所有相邻重复项 | 栈 | 简单 | 和 #20 同一个脑子，代码更短，用来巩固 |
| 26 | 496 | 下一个更大元素 I | 单调栈 | 简单 | 单调栈最简单的形态，先建立直觉 |
| 27 | 739 | 每日温度 | 单调栈 | 中等 | 单调栈模板题，「找下一个更大值」标准解 |
| 28 | 704 | 二分查找 | 二分查找 | 简单 | 二分的**唯一正确写法**，边界必须背下来 |
| 29 | 35 | 搜索插入位置 | 二分查找 | 简单 | 练「找不到时返回 `l`」，左边界思想 |
| 30 | 34 | 在排序数组中查找元素的第一个和最后一个位置 | 二分查找 | 中等 | 左右边界一套写完，二分进阶必做 |
| 31 | 69 | x 的平方根 | 二分查找 | 简单 | 对「答案空间」二分而非对数组二分，换脑子 |
| 32 | 70 | 爬楼梯 | DP 入门 | 简单 | 从递归到 DP 的第一题，理解「重叠子问题」 |
| 33 | 746 | 使用最小花费爬楼梯 | DP 入门 | 简单 | 带权重的爬楼梯，练「状态定义」 |
| 34 | 198 | 打家劫舍 | DP 入门 | 中等 | 「选 / 不选」模型，DP 入门核心 |
| 35 | 121 | 买卖股票的最佳时机 | DP 入门 | 简单 | 一维状态压缩，整个股票系列的门 |
| 36 | 53 | 最大子数组和 | DP 入门 | 中等 | Kadane 算法，DP 与贪心的分界点 |
| 37 | 77 | 组合 | 回溯入门 | 中等 | 回溯模板第一题，理解「做选择 → 递归 → 撤销」 |
| 38 | 78 | 子集 | 回溯入门 | 中等 | 每个节点都收集答案，建立「回溯树」视角 |
| 39 | 46 | 全排列 | 回溯入门 | 中等 | 排列 vs 组合的区别，`used` 数组 |
| 40 | 17 | 电话号码的字母组合 | 回溯入门 | 中等 | 回溯 + 字符串拼接，多集合组合的通用型 |

**可选加餐（做完上面 40 题、还有余力再看，题号题名均已核验，全部简单/中等）**

| 题号 | 题名 | 专题 | 难度 |
|---|---|---|---|
| 167 | 两数之和 II - 输入有序数组 | 双指针 | 中等 |
| 11 | 盛最多水的容器 | 双指针 | 中等 |
| 125 | 验证回文串 | 双指针 | 简单 |
| 1456 | 定长子串中元音的最大数目 | 滑动窗口 | 中等 |
| 567 | 字符串的排列 | 滑动窗口 | 中等 |
| 24 | 两两交换链表中的节点 | 链表 | 中等 |
| 19 | 删除链表的倒数第 N 个结点 | 链表 | 中等 |
| 160 | 相交链表 | 链表 | 简单 |
| 101 | 对称二叉树 | 二叉树递归 | 简单 |
| 111 | 二叉树的最小深度 | 二叉树递归 | 简单 |
| 700 | 二叉搜索树中的搜索 | 二叉树递归 | 简单 |
| 98 | 验证二叉搜索树 | 二叉树递归 | 中等 |
| 236 | 二叉树的最近公共祖先 | 二叉树递归 | 中等 |
| 232 | 用栈实现队列 | 栈 | 简单 |
| 150 | 逆波兰表达式求值 | 栈 | 中等 |
| 155 | 最小栈 | 栈 | 中等 |
| 367 | 有效的完全平方数 | 二分查找 | 简单 |
| 153 | 寻找旋转排序数组中的最小值 | 二分查找 | 中等 |
| 33 | 搜索旋转排序数组 | 二分查找 | 中等 |
| 509 | 斐波那契数 | DP 入门 | 简单 |
| 213 | 打家劫舍 II | DP 入门 | 中等 |
| 122 | 买卖股票的最佳时机 II | DP 入门 | 中等 |
| 39 | 组合总和 | 回溯入门 | 中等 |
| 216 | 组合总和 III | 回溯入门 | 中等 |
| 128 | 最长连续序列 | 哈希 | 中等 |

> **刻意排除的困难题**（知道它们存在就行，本文档阶段不要碰）：76 最小覆盖子串、239 滑动窗口最大值、23 合并 K 个升序链表、42 接雨水、72 编辑距离、300 最长递增子序列、51 N 皇后。

### A.5 模板速查（JS）

**① 双指针 —— 快慢指针（原地删除，`#26 / #27 / #283`）**
```js
function removeElement(nums, val) {
  let slow = 0;                                  // slow = 结果数组的写指针
  for (let fast = 0; fast < nums.length; fast++) {
    if (nums[fast] !== val) nums[slow++] = nums[fast];
  }
  return slow;                                   // slow 就是新长度
}
```

**② 双指针 —— 对撞指针（`#167 / #15 / #11`）**
```js
function twoSumSorted(nums, target) {           // #167
  let l = 0, r = nums.length - 1;
  while (l < r) {
    const s = nums[l] + nums[r];
    if (s === target) return [l + 1, r + 1];
    s < target ? l++ : r--;                      // 小了左移，大了右移
  }
  return [-1, -1];
}

function threeSum(nums) {                        // #15 排序 + 固定一位 + 对撞 + 去重
  const res = [];
  nums.sort((a, b) => a - b);                    // ⚠️ 必须给比较函数
  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] > 0) break;                      // 剪枝：最小的都 > 0 就没救了
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let l = i + 1, r = nums.length - 1;
    while (l < r) {
      const s = nums[i] + nums[l] + nums[r];
      if (s === 0) {
        res.push([nums[i], nums[l], nums[r]]);
        while (l < r && nums[l] === nums[l + 1]) l++;   // 左去重
        while (l < r && nums[r] === nums[r - 1]) r--;   // 右去重
        l++; r--;
      } else if (s < 0) l++;
      else r--;
    }
  }
  return res;
}
```

**③ 滑动窗口 —— 可变长（求最短，`#209`）**
```js
function minSubArrayLen(target, nums) {
  let l = 0, sum = 0, ans = Infinity;
  for (let r = 0; r < nums.length; r++) {
    sum += nums[r];                              // 右边界扩张
    while (sum >= target) {                      // 满足条件就收缩
      ans = Math.min(ans, r - l + 1);
      sum -= nums[l++];
    }
  }
  return ans === Infinity ? 0 : ans;
}
```

**④ 滑动窗口 —— 可变长（求最长，`#3`）**
```js
function lengthOfLongestSubstring(s) {
  const last = new Map();                        // 字符 -> 上次出现的下标
  let l = 0, ans = 0;
  for (let r = 0; r < s.length; r++) {
    const c = s[r];
    if (last.has(c) && last.get(c) >= l) l = last.get(c) + 1;  // 左边界跳到重复字符之后
    last.set(c, r);
    ans = Math.max(ans, r - l + 1);
  }
  return ans;
}
```

**⑤ 滑动窗口 —— 定长（`#643 / #438 / #567`）**
```js
// 定长 k：右边界进窗 → 若超出长度则左边界出窗 → 判断答案
function fixedWindow(s, k) {
  const cnt = new Map();                          // 窗口内字符计数
  let ans = 0;
  for (let r = 0; r < s.length; r++) {
    cnt.set(s[r], (cnt.get(s[r]) || 0) + 1);      // 进窗
    if (r >= k) {                                 // 出窗
      const out = s[r - k], v = cnt.get(out) - 1;
      v === 0 ? cnt.delete(out) : cnt.set(out, v);
    }
    if (r >= k - 1) { /* 用 cnt 判断是否命中，更新 ans */ }
  }
  return ans;
}
```

**⑥ 二叉树递归三部曲（`#104 / #226 / #94`）**
```js
// 三部曲：1) 定参数与返回值  2) 定终止条件  3) 定单层逻辑
// (a) 后序：自底向上，靠返回值合并
function maxDepth(root) {                        // #104
  if (!root) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}

// (b) 前序：自顶向下，靠参数传状态 + 手动回溯
function dfs(node, path, res) {                  // #257 二叉树的所有路径
  if (!node) return;
  path.push(node.val);
  if (!node.left && !node.right) res.push(path.join('->'));
  dfs(node.left, path, res);
  dfs(node.right, path, res);
  path.pop();                                    // ⚠️ 回溯：进递归前 push，出递归后 pop
}

// (c) 层序 BFS + 按层分组
function levelOrder(root) {                      // #102
  if (!root) return [];
  const res = [], q = [root];
  while (q.length) {
    const n = q.length, level = [];              // ⚠️ 先固定本层长度
    for (let i = 0; i < n; i++) {
      const node = q.shift();
      level.push(node.val);
      if (node.left) q.push(node.left);
      if (node.right) q.push(node.right);
    }
    res.push(level);
  }
  return res;
}
```

**⑦ 二分查找 —— 一套三种写法**

| 写法 | 区间 | 循环条件 | 返回 |
|---|---|---|---|
| 精确查找 | `[l, r]` 闭 | `l <= r` | 下标或 `-1` |
| 左边界（第一个 `>= target`） | `[l, r)` 左闭右开 | `l < r` | `l`（可能是 `length`） |
| 右边界（最后一个 `<= target`） | `[l, r)` 左闭右开 | `l < r` | `l - 1` |

```js
function search(nums, target) {                  // #704 精确查找
  let l = 0, r = nums.length - 1;                // 闭区间
  while (l <= r) {
    const m = l + ((r - l) >> 1);
    if (nums[m] === target) return m;
    nums[m] < target ? (l = m + 1) : (r = m - 1);
  }
  return -1;
}

function lowerBound(nums, target) {              // 第一个 >= target，对应 #35 / #34 左边界
  let l = 0, r = nums.length;                    // 左闭右开
  while (l < r) {
    const m = (l + r) >> 1;
    nums[m] < target ? (l = m + 1) : (r = m);
  }
  return l;
}

function upperBoundIndex(nums, target) {         // 最后一个 <= target，对应 #34 右边界
  let l = 0, r = nums.length;
  while (l < r) {
    const m = (l + r) >> 1;
    nums[m] <= target ? (l = m + 1) : (r = m);
  }
  return l - 1;
}
```
> **记忆口诀**：写 `m` 时永远 `l + ((r - l) >> 1)`；用闭区间就 `l <= r` 且 `±1`，用左闭右开就 `l < r` 且 `r = m`（不 `-1`）。**一套写出边界 bug 的根源就是混用这两种。**

**⑧ 回溯模板（`#77 / #78 / #46 / #17`）**
```js
function backtrack(路径, 选择列表) {
  if (满足结束条件) { 结果集.push(路径.slice()); return; }   // ⚠️ 必须 slice 拷贝
  for (const 选择 of 选择列表) {
    路径.push(选择);            // 做选择
    backtrack(路径, 新选择列表); // 递归
    路径.pop();                 // 撤销选择
  }
}

// 组合型（#77）：用 startIndex 保证不重复、只往后选
function combine(n, k) {
  const res = [], path = [];
  (function dfs(start) {
    if (path.length === k) { res.push(path.slice()); return; }
    for (let i = start; i <= n; i++) {
      path.push(i); dfs(i + 1); path.pop();
    }
  })(1);
  return res;
}

// 排列型（#46）：用 used 标记
function permute(nums) {
  const res = [], path = [], used = new Array(nums.length).fill(false);
  (function dfs() {
    if (path.length === nums.length) { res.push(path.slice()); return; }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      used[i] = true; path.push(nums[i]);
      dfs();
      path.pop(); used[i] = false;
    }
  })();
  return res;
}
```

---

## B. Vue3 原理

> 顺序建议：**官方文档两章（响应式基础 + 深入响应式系统）→ 手写 mini-vue → 官方渲染机制 → 编译优化与 diff → 八股**。一共约 15–20 小时，2–3 周业余时间。

### B.1 官方文档关键章节（先读这两章，性价比最高）

- [响应式基础](https://cn.vuejs.org/guide/essentials/reactivity-fundamentals) ✅ —— `ref` / `reactive` 的边界与使用场景（官方 | P0）
- [深入响应式系统](https://cn.vuejs.org/guide/extras/reactivity-in-depth) ✅ —— **官方手写简化版 reactive，把 `track/trigger` 讲透，本章是理解源码的钥匙**（官方 | P0）
- [渲染机制](https://cn.vuejs.org/guide/extras/rendering-mechanism) ✅ —— 虚拟 DOM、渲染管线、编译时优化的整体视图（官方 | P0）
- [性能优化](https://cn.vuejs.org/guide/best-practices/performance) ✅ —— `v-memo` / `v-once` / 计算属性缓存 / 浅层响应式的正确用法（官方 | P0）
- [响应式 API：核心](https://cn.vuejs.org/api/reactivity-core) ✅ —— `reactive` / `ref` / `computed` / `watch` / `watchEffect`（官方 | P0）
- [响应式 API：进阶](https://cn.vuejs.org/api/reactivity-advanced) ✅ —— **`shallowRef` / `triggerRef` / `customRef` / `effectScope` 都在这一页**（官方 | P0）
- [响应式 API：工具](https://cn.vuejs.org/api/reactivity-utilities) ✅ —— `isRef` / `unref` / `toRef` / `toValue`（官方 | P1）
- [内置指令 · `v-memo`](https://cn.vuejs.org/api/built-in-directives) ✅ —— 拉到底找 `v-memo`，理解它和 `patchFlag` 的关系（官方 | P1）
- [计算属性](https://cn.vuejs.org/guide/essentials/computed) ✅ —— 理解 `computed` 的脏值标记与惰性求值（官方 | P1）
- [侦听器](https://cn.vuejs.org/guide/essentials/watchers) ✅ —— `flush: 'pre' | 'post' | 'sync'` 是调度器 `scheduler` 的入口（官方 | P1）
- [深入组件 · 注册](https://cn.vuejs.org/guide/components/registration) ✅ —— 组件注册与解析（官方 | P1）
- [深入组件 · Props](https://cn.vuejs.org/guide/components/props) ✅ —— 单向数据流（官方 | P1）
- [深入组件 · 事件](https://cn.vuejs.org/guide/components/events) ✅ —— `emit` 与 `v-model` 的编译产物（官方 | P1）
- [深入组件 · 组件 v-model](https://cn.vuejs.org/guide/components/v-model) ✅ —— 编译后是 `modelValue` + `update:modelValue`（官方 | P1）
- [内置组件 · KeepAlive](https://cn.vuejs.org/guide/built-ins/keep-alive) ✅ —— 组件缓存，面试常问（官方 | P2）
- [渲染函数 & JSX](https://cn.vuejs.org/guide/extras/render-function) ✅ —— `h()` 与 VNode 结构，读 diff 源码前必须懂（官方 | P1）
- [组合式函数](https://cn.vuejs.org/guide/reusability/composables) ✅ —— 逻辑复用的正确姿势（官方 | P2）
- [vuejs/core 源码仓库](https://github.com/vuejs/core) ✅ —— 对照读：`packages/reactivity/src/` 与 `packages/runtime-core/src/renderer.ts`（源码 | P0）
- [DeepWiki · vuejs/core 编译优化章节](https://deepwiki.com/vuejs/core/8.3-compilation-optimizations) ⚠️（429 限流）—— AI 生成的源码结构图，用来快速定位文件（源码 | P1）

### B.2 响应式源码讲解（reactive / ref / effect / track / trigger / scheduler / stop / effectScope）

- [Vue 3 响应式系统 Reactivity 源码深度解析：从 ref 到 effect 的完整链路](https://juejin.cn/post/7617277836148015130) ✅ —— **一条链路把 `ref → ReactiveEffect → track/trigger` 串起来，本文档首推**（文章 | P0）
- [深入 vue3 源码解读 · 1、响应式的基础概念](https://juejin.cn/post/7652180405778087946) ✅ —— 系列第一篇，概念铺得最平，适合零基础起步（文章 | P0）
- [vue3 源码解析：响应式机制](https://juejin.cn/post/7524229392039936038) ✅ —— 聚焦 `reactive` 的 Proxy handler 与依赖图（文章 | P0）
- [深入 Vue 3 源码：响应式系统的精妙设计与编译优化](https://juejin.cn/post/7657833280844333082) ✅ —— 响应式 + 编译优化一起讲，适合做总复习（文章 | P1）
- [KieSun/vue-interpretation](https://github.com/KieSun/vue-interpretation) ✅ —— **带中文注释的 Vue 源码 fork**，读源码时对着看，比自己啃快 3 倍（源码 | P0）
- [cuixiaorui/mini-vue](https://github.com/cuixiaorui/mini-vue) ✅ —— 从零手写 mini-vue（TDD 驱动，含 `effect` / `scheduler` / `stop` / `effectScope`）**动手一遍 > 读十篇文章**（实战 | P0）
- [heycn/mini-vue3](https://github.com/heycn/mini-vue3) ✅ —— 另一个从零实现版本，可作为 mini-vue 的对照答案（实战 | P1）
- [57code/vue-interview](https://github.com/57code/vue-interview) ✅ —— 源码向 Vue 面试题库，含 reactivity / diff 专题（八股 | P1）

### B.3 编译优化与 diff

- [多图讲解 Vue3 的 diff 算法最长递增子序列实现原理](https://juejin.cn/post/7341007339217354764) ✅ —— **LIS 讲得最清楚的一篇，配图逐步走 `getSequence`**（文章 | P0）
- [Vue3 虚拟 DOM 计算 diff —— 最长递增子序列](https://juejin.cn/post/7130881819024556068) ✅ —— 上一题的补充，从算法角度推 LIS（文章 | P0）
- [vue3 中静态提升和 patchFlag 实现](https://juejin.cn/post/7627830826197221426) ✅ —— 静态提升 / `patchFlag` / 靶向更新（文章 | P0）
- [带你精通 Vue 中的虚拟 DOM 和 DIFF 算法](https://juejin.cn/post/7647054541486915620) ✅ —— 双端对比 → 乱序对比的完整推演（文章 | P1）
- [渲染机制（官方）](https://cn.vuejs.org/guide/extras/rendering-mechanism) ✅ —— Block Tree / `patchFlag` / 静态提升的官方权威定义，**先看官方再看文章**（官方 | P0）

> **背诵要点**：`patchFlag`（靶向更新）+ Block Tree（`dynamicChildren` 摊平动态节点）→ 跳过静态子树 diff；静态提升（hoistStatic）把静态 VNode 提到 render 外只创建一次；`v-memo` 手动跳过子树；乱序 diff 用**最长递增子序列**求出「不需要移动」的最长序列，从而把 DOM 移动次数降到最少（`O(n log n)`）。

### B.4 面试向 Vue3 八股

- [febobo/web-interview（前端面试题宝典）](https://github.com/febobo/web-interview) ✅ —— 中文、Vue 专题成体系，覆盖响应式/diff/生命周期/`nextTick`（八股 | P0）
- [57code/vue-interview](https://github.com/57code/vue-interview) ✅ —— 偏源码、带源码片段，适合答「为什么这么设计」（八股 | P0）
- [yangshun/front-end-interview-handbook](https://github.com/yangshun/front-end-interview-handbook) ✅ —— 中英双语，前端整体复习时用作补充（八股 | P2）
- [Vue3：模板瘦身教练](https://juejin.cn/post/7486300578735177728) ✅ —— 用「模板编译产物」的视角讲清 Vue3 性能提升，面试前 30 分钟速过（八股 | P1）
- [Vue 3 的效率提升主要表现在哪些方面（阿里云开发者社区）](https://developer.aliyun.com/article/1410650) ⚠️ —— 本机 DNS 被拦截无法核验；内容是一页纸总结 Vue3 vs Vue2 的性能提升点，能打开就值得读（八股 | P2）
- 官方文档本身就是最好的八股源 —— 先能用人话讲清 [深入响应式系统](https://cn.vuejs.org/guide/extras/reactivity-in-depth) ✅ 和 [渲染机制](https://cn.vuejs.org/guide/extras/rendering-mechanism) ✅，再去看八股，会发现 80% 的答案你已经会了。

> **注意**：`vue3js.cn`（曾是最流行的 Vue3 中文社区/面试题库）与 `hcysun.me/vue-design`（霍春阳《Vue.js 设计与实现》配套站）在本机 DNS 被拦截，**本次无法核验其存活性**。请你在浏览器里自行打开确认；如果打不开，用上面的 `febobo/web-interview` 和官方文档替代即可。

---

## C. Rust / WASM

> 你 Rust 只写过一点、且聚焦「坐标批量转换 + 轨迹抽稀」这个明确场景 ⇒ **不要通读 The Book**。走：The Book 前 10 章（所有权/借用/结构体/枚举/泛型/trait/集合/错误处理）→ Rustlings 前 60 题 → 直接上 `wasm-pack` 跑通一个导出 `&[f64]` 的函数。

### C.1 Rust 入門

- [《Rust 程序设计语言》中文版（The Book · kaisery 译本）](https://kaisery.github.io/trpl-zh-cn/) ✅ —— 官方书中文译本，**读第 1–10 章即可**，后面章节当字典（教程 | P0）
- [The Book · 英文原版](https://doc.rust-lang.org/book/) ✅ —— 中文版有疑问时对照原文（教程 | P1）
- [Rust 官方书中文镜像（rustwiki）](https://rustwiki.org/zh-CN/book/) ✅ —— 上面译本打不开时的备用入口（教程 | P1）
- [Rustlings（官方练习题仓库）](https://github.com/rust-lang/rustlings) ✅ —— 100+ 小题，**编译报错驱动学习，最适合你这种没时间的人**（实战 | P0）
- [Rustlings 官网 / 安装引导](https://rustlings.cool/) ✅ —— 安装与使用说明（实战 | P0）
- [Rustlings 简体中文翻译版](https://github.com/fan2goa1/rustlings) ✅ —— 题目说明中文化（实战 | P1）
- [Rust 语言圣经 / Rust Course](https://github.com/sunface/rust-course) ✅ —— 中文，**专门有「JS 程序员关注的 WASM、Deno」专题**，比 The Book 更贴近你的来路（教程 | P1）
  - 官网 `https://course.rs/` ⚠️：本机 DNS 被拦截无法核验，请自行打开；打不开就用上面 GitHub 仓库。
- [《Rust 和 WebAssembly》官方书中译本](https://github.com/pearzl/rustwasm-book-zh) ✅ —— 官方 rustwasm 书的中文翻译（教程 | P1）

### C.2 wasm-pack / wasm-bindgen / Rust+WASM 官方书

- [Rust and WebAssembly 官方书（rustwasm.github.io/docs/book）](https://rustwasm.github.io/docs/book/) ✅ —— **权威教程**，从「为什么用 Rust+WASM」到发布 npm 包全流程（官方 | P0）
- [官方书 · 为什么用 Rust 和 WebAssembly](https://rustwasm.github.io/docs/book/why-rust-and-webassembly.html) ✅ —— 先读这页判断该不该上 WASM（官方 | P0）
- [官方书 · Game of Life 实战（implementing 章节）](https://rustwasm.github.io/docs/book/game-of-life/implementing.html) ✅ —— 手把手把 Rust 编译进浏览器，**先跟着跑通一遍**（实战 | P0）
- [wasm-bindgen 指南](https://rustwasm.github.io/docs/wasm-bindgen/) ✅ —— `#[wasm_bindgen]` 的完整参考，**互操作的核心文档**（官方 | P0）
- [wasm-bindgen 新版文档站](https://wasm-bindgen.github.io/wasm-bindgen/) ✅ —— 与上面同一份文档的新域名，路径更好记（官方 | P0）
- [wasm-pack 官方文档](https://rustwasm.github.io/docs/wasm-pack/) ✅ —— 打包、发布 npm、`--target web/nodejs/bundler` 的差异（官方 | P0）
- [wasm-pack 仓库 / README](https://github.com/rustwasm/wasm-pack) ✅ —— 命令速查与常见问题（官方 | P0）
- [wasm-bindgen 仓库](https://github.com/wasm-bindgen/wasm-bindgen) ✅ —— issue 区是排查坑的最佳去处（源码 | P1）
- [wasm-bindgen · 不用打包器（without-a-bundler）](https://rustwasm.github.io/docs/wasm-bindgen/examples/without-a-bundler.html) ✅ —— 前端工程师最关心的「怎么在 Vite 里用」（实战 | P0）
- [MDN 中文 · 编译 Rust 为 WebAssembly](https://developer.mozilla.org/zh-CN/docs/WebAssembly/Guides/Rust_to_Wasm) ✅ —— 中文、篇幅短、最快上手路径（教程 | P0）
- [MDN 中文 · WebAssembly 概念](https://developer.mozilla.org/zh-CN/docs/WebAssembly/Guides/Concepts) ✅ —— Module / Instance / Memory / Table 四个概念的权威定义（官方 | P0）

> **踩坑提示**：`wasm-pack` 的旧地址 `https://rustwasm.github.io/wasm-pack/` 与 `https://rustwasm.github.io/wasm-pack/book/` 实测 **404**（已迁移），请用上面 `rustwasm.github.io/docs/wasm-pack/`。`https://wasm-bindgen.github.io/wasm-pack/` 也可访问。

### C.3 【重点】内存共享 / 零拷贝 / 互操作开销 / 什么时候不该用 WASM

**零拷贝与 `Float64Array`（这是你做坐标批量转换的命门）**

- [wasm-bindgen · Number Slices（`&[f64]` ↔ `Float64Array`）](https://rustwasm.github.io/docs/wasm-bindgen/reference/types/number-slices.html) ✅ —— **本文档 C 部分最重要的一页**。`&[f64]`/`&mut [f64]` 映射为 JS 的 `Float64Array` **视图**，是真正的零拷贝；但它只在函数调用期间有效，**不能在 JS 里长期持有**（除非用 `wasm_bindgen::memory()` + `Memory` 手动管理）
- [wasm-bindgen · BoxedNumberSlice（`Box<[f64]>`）](https://rustwasm.github.io/docs/wasm-bindgen/reference/types/boxed-number-slices.html) ✅ —— 把 slice 的所有权移交给 JS，**可以长期持有**，代价是一次分配（对比上一页，决定你该用哪个）
- [wasm-bindgen · `slice_to_array` 属性](https://wasm-bindgen.github.io/wasm-bindgen/reference/attributes/on-js-imports/slice_to_array.html) ✅ —— 显式控制「视图 vs 拷贝」，性能调优时用（官方 | P0）
- [wasm-bindgen · `getter`/`setter` on Rust exports](https://rustwasm.github.io/docs/wasm-bindgen/reference/attributes/on-rust-exports/getter-and-setter.html) ✅ —— 导出结构体字段时的互操作细节（官方 | P2）
- [MDN 中文 · WebAssembly.Memory](https://developer.mozilla.org/zh-CN/docs/WebAssembly/JavaScript_interface/Memory) ✅ —— `memory.buffer` 是 `ArrayBuffer`，**buffer 在内存增长后会 detach**，这是零拷贝方案最常见的翻车点（官方 | P0）
- [MDN 中文 · 使用 JavaScript API](https://developer.mozilla.org/zh-CN/docs/WebAssembly/Guides/Using_the_JavaScript_API) ✅ —— `WebAssembly.instantiate` / 导入导出对象 / `memory.grow`（官方 | P0）
- [docs.rs · js_sys::WebAssembly::Memory](https://docs.rs/js-sys/latest/js_sys/WebAssembly/struct.Memory.html) ✅ —— Rust 侧操作 `Memory` 的 API（参考 | P1）
- [wasm-bindgen issue #2456 · 在 JS 和 Rust 之间共享内存的真实例子](https://github.com/wasm-bindgen/wasm-bindgen/issues/2456) ✅ —— **官方维护者的直接回答，读这一条胜过读十篇博客**（讨论 | P0）
- [wasm-bindgen issue #2402](https://github.com/wasm-bindgen/wasm-bindgen/issues/2402) ✅ —— 同类内存/切片问题的补充（讨论 | P2）

**互操作开销分析**

- [Calls between JavaScript and WebAssembly are finally fast 🎉（Mozilla Hacks）](https://hacks.mozilla.org/2018/10/calls-between-javascript-and-webassembly-are-finally-fast-%F0%9F%8E%89/) ✅ —— **JS↔WASM 调用开销的经典分析**，结论：别在循环里频繁跨界，要批量化（文章 | P0）
- [web.dev · Loading WebAssembly](https://web.dev/articles/loading-wasm) ✅ —— 编译/实例化/加载的启动开销，以及大模块为什么卡首屏（官方 | P0）
- [WebAssembly 设计文档 · FAQ](https://github.com/WebAssembly/design/blob/main/FAQ.md) ✅ —— 「WASM 什么时候不如 JS」的官方回答（官方 | P0）
- [得物技术 · 基于 IM 场景下的 Wasm 初探：提升 Web 应用性能](https://cloud.tencent.cn/developer/article/2463786) ✅ —— 中文实战，含真实数据与「为什么最后没全用 WASM」的取舍（文章 | P0）
- [How to NOT WebAssembly / wasm-wtf（mcyoung）](https://mcyoung.xyz/2023/08/01/wasm-wtf/) ✅ —— 英文长文，讲清「编译到 wasm 后反而更慢」的具体机制（文章 | P0）
- [Surma · JS to ASC / WASM](https://surma.dev/things/js-to-asc/) ✅ —— 前端工程师视角的性能对比与心智模型（文章 | P1）
- [cwasm（aransentin）](https://aransentin.github.io/cwasm/) ✅ —— 把 C 编到 wasm 后，**去掉 wasm 反而更快**的真实案例复盘（文章 | P1）
- [Making WebAssembly a first-class language on the Web（Mozilla Hacks）](https://hacks.mozilla.org/2026/02/making-webassembly-a-first-class-language-on-the-web/) ✅ —— Web 平台侧对 WASM 限制的官方视角（文章 | P1）
- [Lobsters 讨论 · WebAssembly: Yes, but for What?](https://lobste.rs/s/cyxkzl/webassembly_yes_for_what) ✅ —— **「什么时候不该用 WASM」的从业者讨论串**，正反观点都全（讨论 | P1）
- [InfoWorld · What tech teams need to know about WebAssembly](https://www.infoworld.com/article/3621615/what-tech-teams-need-to-know-about-webassembly.html) ✅ —— 决策向清单：适合/不适合的场景（文章 | P2）

> **给你场景的结论（可直接用）**：坐标批量转换 + 轨迹抽稀是 WASM 的**甜区**——纯计算、数据规整（`Float64Array`）、一次调用处理上万点。关键是**别把点一个个传过去**，而是：JS 侧 `Float64Array` 一次性写入 → 调一次 Rust 函数 → Rust 原地改写 `&mut [f64]` → JS 直接读同一块内存。任何「循环里调用 wasm 函数」或「返回 `Vec<f64>` 触发拷贝」的写法都会把收益吃光。

### C.4 坐标批量转换 / 轨迹抽稀（Douglas-Peucker）参考实现

- [道格拉斯-普克算法 · 维基百科（中文）](https://zh.wikipedia.org/zh-cn/%E9%81%93%E6%A0%BC%E6%8B%89%E6%96%AF-%E6%99%AE%E5%85%8B%E7%AE%97%E6%B3%95) ✅ —— 算法定义、递归流程、复杂度（参考 | P0）
- [道格拉斯-普克抽稀算法（图解 + 源码 · 中文）](https://cloud.tencent.com.cn/developer/article/2537223) ✅ —— 有流程图解 + 完整实现 + 注释，**中文里最好懂的一篇**（文章 | P0）
- [mourner/simplify-js](https://github.com/mourner/simplify-js) ✅ —— **JS 版 DP 最经典的实现，源码约 60 行，先读它再写 Rust 版**（实现 | P0）
- [LiuTangLei/trajectory-simplification-js](https://github.com/LiuTangLei/trajectory-simplification-js) ✅ —— 集合了多种**轨迹抽稀**算法（DP、SQUISH、Dead Reckoning 等）的 JS 库，正好对上你的场景（实现 | P0）
- [GeoRust · geo 仓库](https://github.com/georust/geo) ✅ —— Rust 几何库，坐标计算的主力（实现 | P0）
- [docs.rs · geo::algorithm::simplify::Simplify](https://docs.rs/geo/latest/geo/algorithm/simplify/trait.Simplify.html) ✅ —— **Rust 侧的 DP 抽稀直接调用 `simplify(&tolerance)`**，别自己从头写（实现 | P0）
- [geo · simplify.rs 源码](https://github.com/georust/geo/blob/main/geo/src/algorithm/simplify.rs) ✅ —— 读官方实现，理解 Rust 迭代式（非递归）DP 怎么写（源码 | P0）
- [docs.rs · rdp crate](https://docs.rs/rdp/latest/rdp/) ✅ —— 另一个轻量 `rdp` crate，接口更简单，适合直接搬进 wasm（实现 | P1）
- [3liz/proj4rs](https://github.com/3liz/proj4rs) ✅ —— **Rust 版 Proj4**（坐标转换/投影），纯 Rust、可编译到 wasm 的坐标转换方案（实现 | P0）

> ⚠️ `crates.io` 在本机被代理拦截（返回 404），所以上面 Rust crate 一律给 **docs.rs** 链接（已实测 200）。`lib.rs` 同样被拦（403）。

---

## 附：一页纸行动清单

| 周次 | 算法（每周 3 次 × 40 min） | Vue3（每周 2h） | Rust/WASM（每周 2h） |
|---|---|---|---|
| W1 | 题 1–5（哈希） | 官方「响应式基础」+「深入响应式系统」 | The Book 第 1–4 章 + Rustlings 前 20 题 |
| W2 | 题 6–9（双指针） | 手写 mini-vue：`reactive` + `effect` | The Book 5–7 章（结构体/枚举/集合）+ Rustlings 21–40 |
| W3 | 题 10–13（滑动窗口） | 手写 mini-vue：`track/trigger/scheduler/stop` | The Book 8–10 章 + Rustlings 41–60 |
| W4–5 | 题 14–18（链表） | 官方「渲染机制」+ `patchFlag` / 静态提升 | wasm-pack 跑通 Game of Life |
| W6–7 | 题 19–23（二叉树） | diff 双端对比 + LIS（两篇文章） | 写第一个 `&mut [f64]` 原地改写函数 |
| W8–9 | 题 24–27（栈 / 单调栈） | 官方 reactivity-advanced（`effectScope`） | 把 DP 抽稀搬进 wasm，对比 JS 版耗时 |
| W10–11 | 题 28–31（二分） | 读 `packages/reactivity/src/` 源码 | `proj4rs` / `geo::simplify` 接进项目 |
| W12–13 | 题 32–36（DP） | 八股：febobo + 57code | 用 `Number Slices` + `Memory` 做零拷贝优化 |
| W14 | 题 37–40（回溯）+ 全部第 3 遍复盘 | 模拟面试自述 | 写一份「什么时候不该用 WASM」的结论 |

**唯一的硬性要求**：算法那 40 题，**每题必须做满 3 遍**。做 40 题 × 1 遍，不如做 20 题 × 3 遍。
