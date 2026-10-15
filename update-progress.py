#!/usr/bin/env python3
"""
进度更新脚本 —— 每天做完后跑一次，避免手改 progress.json 出错。

用法：
    python3 update-progress.py done 2        # 标记 Day 2 完成，自动推进到 Day 3
    python3 update-progress.py done 2 --note "GDAL 装好了"
    python3 update-progress.py show          # 只看当前进度
    python3 update-progress.py set 5         # 手动跳到 Day 5（比如补做了几天）
"""
import json
import sys
import os
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
PROGRESS = os.path.join(HERE, "progress.json")

# 计划起点：Day N 的日期 = START + (N-1) 天
START = date(2026, 10, 19)


def day_date(n):
    return START + timedelta(days=n - 1)


def day_dir(n):
    """找到 Day n 对应的文件夹名"""
    prefix = f"D{n:02d}_"
    for d in sorted(os.listdir(os.path.join(HERE, "GIS前端60天计划"))):
        if d.startswith(prefix):
            return d
    return None


def load():
    with open(PROGRESS, encoding="utf-8") as f:
        return json.load(f)


def save(d):
    with open(PROGRESS, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")


def milestone_of(day):
    """根据天数推算里程碑"""
    for lo, hi, mid in [(1, 7, "M0"), (8, 14, "M1"), (15, 28, "M2"),
                        (29, 42, "M3"), (43, 49, "M4"), (50, 56, "M5"),
                        (57, 63, "M6")]:
        if lo <= day <= hi:
            return mid
    return "?"


def show(d):
    cur = d["current_day"]
    folder = day_dir(cur)
    print(f"当前：Day {cur}｜{day_date(cur)}｜{milestone_of(cur)}")
    print(f"主题：{d['next_task']['theme']}")
    print(f"文件：GIS前端60天计划/{folder}/README.md")
    if d["next_task"].get("prerequisite"):
        print(f"前置：{d['next_task']['prerequisite']}")
    done = d["completed_days"]
    print(f"已完成 {len(done)}/63 天" + (f"（最近：{done[-3:]}）" if done else ""))


def main():
    if len(sys.argv) < 2:
        show(load())
        return

    action = sys.argv[1]
    d = load()

    if action == "show":
        show(d)

    elif action == "done":
        if len(sys.argv) < 3:
            print("用法：python3 update-progress.py done <天数>")
            sys.exit(1)
        n = int(sys.argv[2])
        if n not in d["completed_days"]:
            d["completed_days"].append(n)
            d["completed_days"].sort()

        # 推进到下一天：往上找第一个未完成的天
        nxt = n + 1
        while nxt in d["completed_days"] and nxt <= 63:
            nxt += 1

        d["current_day"] = nxt
        d["current_date"] = day_date(nxt).isoformat()

        folder = day_dir(nxt)
        if folder:
            # 从文件夹 README 里抓主题
            rp = os.path.join(HERE, "GIS前端60天计划", folder, "README.md")
            theme = ""
            if os.path.exists(rp):
                for line in open(rp, encoding="utf-8"):
                    if line.startswith("## 今日主题："):
                        theme = line.replace("## 今日主题：", "").strip()
                        break
            d["next_task"] = {"day": nxt, "theme": theme,
                              "readme": f"GIS前端60天计划/{folder}/README.md"}

        # 更新里程碑状态
        cur_m = milestone_of(nxt)
        for m in d["milestones"]:
            if m["id"] < cur_m:
                m["status"] = "done"
            elif m["id"] == cur_m:
                m["status"] = "in_progress"
            else:
                m["status"] = "not_started"

        # 可选备注
        if "--note" in sys.argv:
            note = sys.argv[sys.argv.index("--note") + 1]
            d.setdefault("notes", []).append(f"D{n}: {note}")

        save(d)
        print(f"✅ Day {n} 已完成")
        show(d)

    elif action == "set":
        n = int(sys.argv[2])
        d["current_day"] = n
        d["current_date"] = day_date(n).isoformat()
        folder = day_dir(n)
        if folder:
            d["next_task"]["readme"] = f"GIS前端60天计划/{folder}/README.md"
        save(d)
        show(d)
        print("（完成天数未变，如需同步请手动调整 completed_days）")

    else:
        print(f"未知操作：{action}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
