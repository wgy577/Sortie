# Sortie | 舰载机调度可视化

基于 **FJSP（柔性作业车间调度）** 研究舰载机从航空母舰上出动调度的可视化。

核心问题：**多架舰载机、多个弹射器、各种保障设备——如何调度让所有飞机在最短时间内无冲突地出动？**

我们用 **PPO（近端策略优化）** 训练一个 Agent 来学习做调度决策，下文将完整展示过程。

---

## 一、训练过程 — Training

### ① 训练曲线 — Training Curve

PPO 训练 reward 曲线。纵坐标是每次调度episode的得分，横坐标是训练步数。逐渐上升并收敛 —— 表示 Agent 学会了更高效的调度，减少了冲突和空闲等待。

PPO training reward curve. Vertical: score per scheduling episode. Horizontal: training steps. Rising then converging agent is learning to schedule more efficiently.

<video src="videos/1_training_curve.mp4" width="800" controls></video>

🎬 [videos/1_training_curve.mp4](videos/1_training_curve.mp4)

### ② 训练 Episosde -> 甘特图 — Episode to Gantt Chart

一个训练 episode 压缩成甘特图。每行是一架飞机，每个彩色块是一个工序（滑行到弹射位、弹射起飞等）。可以看到 Agent 如何安排飞机在各时间轴上的工序序列。

A single training episode compressed into Gantt chart. Each row is an aircraft, each colored block is an operation. You can see how the agent arranges operation sequences.

<video src="videos/2_training_gantt.mp4" width="800" controls></video>

---

## 二、小规模演示：理解调度原理 — Small-scale Demos

### ③ 单架出动 — Single Aircraft Sortie

只有一架舰载机：牵引车定位飞机 -> 拖车拉到弹射器 -> 弹射起飞 -> 飞机离场。基线场景，所有复杂协调都由此衍生。

Only one aircraft: tractor positions aircraft -> tows to catapult -> launches -> leaves. Baseline scenario.

<video src="videos/3_sortie1.mp4" width="800" controls></video>

### ④ 双机并行 — Two Aircraft Parallel

两架飞机同时出动。问题出现了：弹射器有限、牵引车有限 —— 谁先走？如何避免等待？FJSP 的价值就在这里。

Two aircraft launch simultaneously. Limited catapults, limited tractors who goes first? FJSP's value appears here.

<video src="videos/4_sortie2_parallel.mp4" width="800" controls></video>

## 三、全规模：20架飞机 — Full Scale: 20 Aircraft

这是完整的问题规模 —— 20架飞机竞争 4 个弹射器和各种保障设备。复杂度指数级上升。

The full problem — 20 aircraft competing for 4 catapults and support equipment. Exponential complexity.

### ⑤ 20架快速演示 — 20 Aircraft Fast Demo

低帧率快速版，看整体调度节奏。可以看到 Agent 如何把飞机分批并分配到不同弹射位，形成流水线。

Low-frame-rate fast version for overall dispatch rhythm. See how agent batches aircraft into different catapults.

<video src="videos/5_sortie20_fast.mp4" width="800" controls></video>

### ⑥ 20架高清 1.5x — 20 Aircraft HD 1.5x

高清细节版（1.5倍速）。飞机运动、拖曳轨迹、弹射起飞瞬间清晰可见。

HD detail version (1.5x speed). Aircraft movements, towing trajectories, launch moments clearly visible.

<video src="videos/6_sortie20_hd_1.5x.mp4" width="800" controls></video>

### ⑦ 20架高清 1x — 20 Aircraft HD 1x

高清细节版（正常速度）。可以逐帧观看每架飞机的完整运动路径。

HD detail version (normal speed). Watch each aircraft's complete motion path frame by frame.

<video src="videos/8_sortie20_hd_1x.mp4" width="800" controls></video>

## 四、小编队场景：8架飞机 — Small Package: 8 Aircraft

实际任务并非全部出动，常选择一个子集出击。下面展示8架飞机小编队任务。

Real missions often deploy a subset. Below shows 8 selected aircraft in small package.

### ⑧ 8架快速演示 — 8 Aircraft Fast Demo

8架被选中的舰载机，低帧率快速版，快速展示小编队出动调度场景。

8 selected aircraft, fast version showing small package dispatch scenario.

<video src="videos/9_sortie8_fast.mp4" width="800" controls></video>

### ⑨ 8架高清完整版 — 8 Aircraft HD Complete

高清完整版。从牵引车定位到出动全过程，每架飞机每个步骤都精细渲染。

HD complete version. From tractor positioning to launch, every step rendered in detail.

<video src="videos/10_sortie8_hd.mp4" width="800" controls></video>

---

*注：视频截图（封面图）将在仓库公开后补充添加。*

*Screenshots will be added after repo goes public.*

---

README 视频总览：

| # | File | 文件 | Description |
|---|------|------|-------------|
| 1 | `videos/1_training_curve.mp4` | 训练曲线 | PPO 训练 reward 曲线 |
| 2 | `videos/2_training_gantt.mp4` | 训练甘特 | 训练 Episode -> 甘特图 |
| 3 | `videos/3_sortie1.mp4` | 单架出动 | 单架出动基线场景 |
| 4 | `videos/4_sortie2_parallel.mp4` | 双机出动 | 双机并行调度 |
| 5 | `videos/5_sortie20_fast.mp4` | 20架出动（调度） | 20架飞机调度快速演示 |
| 6 | `videos/6_sortie20_hd_1.5x.mp4` | 20架出动（高质量 1.5x） | 20架出动高清 1.5x |
| 7 | `videos/7_sortie20_hd_1.5x_alt.mp4` | 20架出动（高质量 1.5x 备选） | 同⑥ 备选 |
| 8 | `videos/8_sortie20_hd_1x.mp4` | 20架出动（高质量 原速） | 20架出动高清原速 |
| 9 | `videos/9_sortie8_fast.mp4` | 8架出动（调度） | 8架小编队快速演示 |
| 10 | `videos/10_sortie8_hd.mp4` | 8架出动（高质量完整版） | 8架出动高清完整过程 |
