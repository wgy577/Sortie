     1|# Sortie | 舰载机调度可视化
     2|
     3|基于 **FJSP（柔性作业车间调度）** 研究舰载机从航空母舰上出动调度的可视化。
     4|
     5|核心问题：**多架舰载机、多个弹射器、各种保障设备——如何调度让所有飞机在最短时间内无冲突地出动？**
     6|
     7|我们用 **PPO（近端策略优化）** 训练一个 Agent 来学习做调度决策，下文将完整展示过程。
     8|
     9|---
    10|
    11|## 一、训练过程 — Training
    12|
    13|### ① 训练曲线 — Training Curve
    14|
    15|PPO 训练 reward 曲线。纵坐标是每次调度episode的得分，横坐标是训练步数。逐渐上升并收敛 —— 表示 Agent 学会了更高效的调度，减少了冲突和空闲等待。
    16|
    17|PPO training reward curve. Vertical: score per scheduling episode. Horizontal: training steps. Rising then converging agent is learning to schedule more efficiently.
    18|
    19|![Training Curve](assets/1_training_curve.png)
    20|<video src="https://wgy577.github.io/sortie-videos/videos/1_training_curve.mp4" width="800" controls></video>
    21|
    22|🎬 [1_training_curve.mp4](https://wgy577.github.io/sortie-videos/videos/1_training_curve.mp4)
    23|
    24|### ② 训练 Episode -> 甘特图 — Episode to Gantt Chart
    25|
    26|一个训练 episode 压缩成甘特图。每行是一架飞机，每个彩色块是一个工序（滑行到弹射位、弹射起飞等）。可以看到 Agent 如何安排飞机在各时间轴上的工序序列。
    27|
    28|A single training episode compressed into Gantt chart. Each row is an aircraft, each colored block is an operation. You can see how the agent arranges operation sequences.
    29|
    30|![Training Gantt](assets/2_training_gantt.png)
<video src="https://wgy577.github.io/sortie-videos/videos/2_training_gantt.mp4" width="800" controls></video>
    31|
    32|---
    33|
    34|## 二、小规模演示：理解调度原理 — Small-scale Demos
    35|
    36|### ③ 单架出动 — Single Aircraft Sortie
    37|
    38|只有一架舰载机：牵引车定位飞机 -> 拖车拉到弹射器 -> 弹射起飞 -> 飞机离场。基线场景，所有复杂协调都由此衍生。
    39|
    40|Only one aircraft: tractor positions aircraft -> tows to catapult -> launches -> leaves. Baseline scenario.
    41|
    42|![Single Sortie](assets/3_sortie1.png)
<video src="https://wgy577.github.io/sortie-videos/videos/3_sortie1.mp4" width="800" controls></video>
    43|
    44|### ④ 双机并行 — Two Aircraft Parallel
    45|
    46|两架飞机同时出动。问题出现了：弹射器有限、牵引车有限 —— 谁先走？如何避免等待？FJSP 的价值就在这里。
    47|
    48|Two aircraft launch simultaneously. Limited catapults, limited tractors who goes first? FJSP's value appears here.
    49|
    50|![Two Parallel](assets/4_sortie2_parallel.png)
<video src="https://wgy577.github.io/sortie-videos/videos/4_sortie2_parallel.mp4" width="800" controls></video>
    51|
    52|## 三、全规模：20架飞机 — Full Scale: 20 Aircraft
    53|
    54|这是完整的问题规模 —— 20架飞机竞争 4 个弹射器和各种保障设备。复杂度指数级上升。
    55|
    56|The full problem — 20 aircraft competing for 4 catapults and support equipment. Exponential complexity.
    57|
    58|### ⑤ 20架快速演示 — 20 Aircraft Fast Demo
    59|
    60|低帧率快速版，看整体调度节奏。可以看到 Agent 如何把飞机分批并分配到不同弹射位，形成流水线。
    61|
    62|Low-frame-rate fast version for overall dispatch rhythm. See how agent batches aircraft into different catapults.
    63|
    64|![20 Fast](assets/5_sortie20_fast.png)
<video src="https://wgy577.github.io/sortie-videos/videos/5_sortie20_fast.mp4" width="800" controls></video>
    65|
    66|### ⑥ 20架高清 1.5x — 20 Aircraft HD 1.5x
    67|
    68|高清细节版（1.5倍速）。飞机运动、拖曳轨迹、弹射起飞瞬间清晰可见。
    69|
    70|HD detail version (1.5x speed). Aircraft movements, towing trajectories, launch moments clearly visible.
    71|
    72|![20 HD 1.5x](assets/6_sortie20_hd_1.5x.png)
<video src="https://wgy577.github.io/sortie-videos/videos/6_sortie20_hd_1.5x.mp4" width="800" controls></video>
    73|
    74|### ⑦ 20架高清 1x — 20 Aircraft HD 1x
    75|
    76|高清细节版（正常速度）。可以逐帧观看每架飞机的完整运动路径。
    77|
    78|HD detail version (normal speed). Watch each aircraft's complete motion path frame by frame.
    79|
    80|![20 HD 1x](assets/8_sortie20_hd_1x.png)
<video src="https://wgy577.github.io/sortie-videos/videos/8_sortie20_hd_1x.mp4" width="800" controls></video>
    81|
    82|## 四、小编队场景：8架飞机 — Small Package: 8 Aircraft
    83|
    84|实际任务并非全部出动，常选择一个子集出击。下面展示8架飞机小编队任务。
    85|
    86|Real missions often deploy a subset. Below shows 8 selected aircraft in small package.
    87|
    88|### ⑧ 8架快速演示 — 8 Aircraft Fast Demo
    89|
    90|8架被选中的舰载机，低帧率快速版，快速展示小编队出动调度场景。
    91|
    92|8 selected aircraft, fast version showing small package dispatch scenario.
    93|
    94|![8 Fast](assets/9_sortie8_fast.png)
<video src="https://wgy577.github.io/sortie-videos/videos/9_sortie8_fast.mp4" width="800" controls></video>
    95|
    96|### ⑨ 8架高清完整版 — 8 Aircraft HD Complete
    97|
    98|高清完整版。从牵引车定位到出动全过程，每架飞机每个步骤都精细渲染。
    99|
   100|HD complete version. From tractor positioning to launch, every step rendered in detail.
   101|
   102|![8 HD](assets/10_sortie8_hd.png)
<video src="https://wgy577.github.io/sortie-videos/videos/10_sortie8_hd.mp4" width="800" controls></video>
   103|
   104|---
   105|
   106|*注：视频截图（封面图）将在仓库公开后补充添加。*
   107|
   108|*Screenshots will be added after repo goes public.*
   109|
   110|---
   111|
   112|README 视频总览：
   113|
   114|| # | File | Description |
   115||---|------|-------------|
   116|| 1 | [1_training_curve.mp4](https://wgy577.github.io/sortie-videos/videos/1_training_curve.mp4) | PPO 训练 reward 曲线 |
   117|| 2 | [2_training_gantt.mp4](https://wgy577.github.io/sortie-videos/videos/2_training_gantt.mp4) | 训练 Episode -> 甘特图 |
   118|| 3 | [3_sortie1.mp4](https://wgy577.github.io/sortie-videos/videos/3_sortie1.mp4) | 单架出动基线场景 |
   119|| 4 | [4_sortie2_parallel.mp4](https://wgy577.github.io/sortie-videos/videos/4_sortie2_parallel.mp4) | 双机并行调度 |
   120|| 5 | [5_sortie20_fast.mp4](https://wgy577.github.io/sortie-videos/videos/5_sortie20_fast.mp4) | 20架飞机调度快速演示 |
   121|| 6 | [6_sortie20_hd_1.5x.mp4](https://wgy577.github.io/sortie-videos/videos/6_sortie20_hd_1.5x.mp4) | 20架出动高清 1.5x |
   122|| 7 | [7_sortie20_hd_1.5x_alt.mp4](https://wgy577.github.io/sortie-videos/videos/7_sortie20_hd_1.5x_alt.mp4) | 同⑥ 备选 |
   123|| 8 | [8_sortie20_hd_1x.mp4](https://wgy577.github.io/sortie-videos/videos/8_sortie20_hd_1x.mp4) | 20架出动高清原速 |
   124|| 9 | [9_sortie8_fast.mp4](https://wgy577.github.io/sortie-videos/videos/9_sortie8_fast.mp4) | 8架小编队快速演示 |
   125|| 10 | [10_sortie8_hd.mp4](https://wgy577.github.io/sortie-videos/videos/10_sortie8_hd.mp4) | 8架出动高清完整过程 |
   126|