<div align="center">

# Sortie

### 面向舰载机出动调度的复杂约束 HFSP
### Complex-Constrained HFSP for Carrier Aircraft Sortie Scheduling

舰载机出动决策、强化学习与调度过程可视化<br>
Carrier-aircraft dispatching, reinforcement learning, and schedule visualization

![Problem](https://img.shields.io/badge/Problem-Complex--Constrained_HFSP-17324D?style=flat-square)
![Method](https://img.shields.io/badge/Method-PPO-2F6B5F?style=flat-square)
![Objective](https://img.shields.io/badge/Objective-Makespan-C47C3C?style=flat-square)

[**项目仓库 · Project**](https://github.com/wgy577/Sortie) · [**3D 交互演示 · 3D Demo**](https://wgy-carrier-operations-demo.wgy577-sortie.workers.dev/) · [**视频中心 · Videos**](https://github.com/wgy577/sortie-videos)

</div>

---

## 项目说明 · Project statement

本项目由 **大连理工大学吴光宇在导师与师兄指导下完成**，作为相关论文研究工作的可视化展示 Demo，用于呈现复杂约束 HFSP 舰载机出动调度的建模、训练与调度结果。

This project was developed by **Guangyu Wu at Dalian University of Technology under the guidance of his academic advisor and senior lab colleagues** as a visual demonstration for the associated research paper. It presents the modeling, training process, and scheduling results of complex-constrained HFSP for carrier-aircraft sortie operations.

## 项目概览 · Overview

Sortie 将舰载机出动调度建模为带有复杂作业约束的 **HFSP（Hybrid Flow Shop Scheduling Problem，混合流水车间调度）**。每架舰载机依次经过保障、转运与弹射等作业阶段；每个阶段配置多个并行资源，调度器需要在满足工序先后关系、资源容量、甲板空间与安全要求的条件下，协调舰载机、牵引车、保障位和弹射器。

Sortie formulates carrier-aircraft launch scheduling as a **complex-constrained Hybrid Flow Shop Scheduling Problem (HFSP)**. Each aircraft passes through ordered preparation, transfer, and launch stages. Multiple parallel resources are available at each stage, while the scheduler coordinates aircraft, tractors, preparation spots, and catapults subject to precedence, capacity, deck-space, and operational-safety constraints.

项目使用基于 **PPO（Proximal Policy Optimization，近端策略优化）** 的智能体进行序贯派工与资源分配，以缩短整体出动完工时间（makespan），同时保持调度可行且资源无冲突。

A **PPO (Proximal Policy Optimization)** agent performs sequential dispatching and resource assignment. The objective is to reduce the overall sortie makespan while maintaining a feasible, conflict-free schedule.

## 航空母舰三维交互演示 · Interactive carrier 3D demo

三维 Demo 直接复用项目中的甲板坐标、设备位置以及 MATLAB 牵引轨迹，以完整航母、
舰载机与牵引车模型展示单架舰载机工序 1–8，包括牵引车接近、挂接、牵引、进入弹射器、
弹射离舰和持续攀升。页面支持绕航母观察、环境亮度调整、完整流程和单独出动演示。

“甲板机”按钮可选择 6、10、16、24 或 31 架静态舰载机；为了控制 GPU 负载并防止设备发热，默认为 10 架，31 架用于展示完整停机布局。展示结束后请务必点击“结束并停止”或关闭 Demo 标签页，以停止后台三维渲染并释放 WebGL 资源。

The interactive demo reuses the deck coordinates, equipment locations, and MATLAB towing trajectories from this project. It presents the complete operation 1–8 sequence for one aircraft, from tractor approach and towing to catapult launch and sustained climb.

The deck-aircraft selector provides 6, 10, 16, 24, or all 31 static aircraft. Ten is the default heat-management setting; 31 displays the complete parking layout. After viewing, always select **End and Stop** or close the Demo tab to stop background 3D rendering and release WebGL resources.

[![航空母舰三维交互演示 · Interactive carrier 3D demo](assets/11_carrier_3d_demo.png)](https://wgy-carrier-operations-demo.wgy577-sortie.workers.dev/)

▶ [**打开 3D Demo · Open interactive demo**](https://wgy-carrier-operations-demo.wgy577-sortie.workers.dev/)

接口 · API: [`GET /api/demo`](https://wgy-carrier-operations-demo.wgy577-sortie.workers.dev/api/demo)

完整 Demo 源码保存在独立的 GitHub 私有仓库；本公开仓库仅提供成果介绍、访问入口和接口信息。<br>
The complete demo source is maintained in a separate private GitHub repository; this public repository contains only the research showcase and access points.

## 调度模型 · Scheduling model

| 要素 · Element | 调度含义 · Role in the scheduling system |
|:--|:--|
| 作业 · Jobs | 任务中选定的舰载机 · Carrier aircraft selected for a sortie |
| 阶段 · Stages | 按顺序执行的保障、转运与弹射作业 · Ordered preparation, transfer, and launch operations |
| 并行资源 · Parallel resources | 各阶段可用的牵引车、保障位与弹射器 · Tractors, preparation spots, and catapults available at each stage |
| 复杂约束 · Complex constraints | 工序优先级、资源互斥、容量、甲板空间与作业安全 · Precedence, exclusive use, capacity, deck space, and operational safety |
| 优化目标 · Objective | 在保持可行、无冲突的同时最小化 makespan · Minimize makespan while maintaining a feasible, conflict-free schedule |
| 决策策略 · Policy | 基于 PPO 的序贯派工与资源分配 · PPO-based sequential dispatching and resource assignment |

## 训练过程 · Training

> 点击任意预览图可在线播放带水印视频；每个展示位置同时提供明确的视频链接，文末另有完整汇总。<br>
> Click any preview to play the watermarked video. Each section also provides a direct link, followed by a complete index at the end.

### PPO 学习过程 · PPO learning process

训练曲线记录策略学习过程中的 makespan。原始序列与平滑趋势共同展示策略如何逐渐获得更稳定、更高效的调度能力。

The learning curve tracks makespan throughout training. The raw series and smoothed trend show how the policy gradually develops more stable and efficient scheduling behavior.

[![PPO 训练曲线 · PPO training curve](assets/1_training_curve.png)](https://wgy577.github.io/sortie-videos/videos/1_training_curve.mp4)

▶ [在线播放 · Play](https://wgy577.github.io/sortie-videos/videos/1_training_curve.mp4)

### 异步训练与甘特图演化 · Asynchronous episodes and Gantt evolution

视频首先展示 PPO 网络的训练过程：不同舰载机数量的并行环境异步运行并结束，采集到的轨迹持续汇入 rollout buffer。训练完成后，使用训练后的网络依次输出选机与资源分配决策，并将最终调度结果呈现为甘特图，从而直观展示各阶段的资源占用、作业顺序与完成时间。

The video first presents PPO network training: parallel environments with different aircraft counts run and terminate asynchronously while their trajectories are collected in the rollout buffer. After training, the trained network sequentially produces aircraft-selection and resource-assignment decisions, and the resulting schedule is rendered as a Gantt chart to visualize resource occupation, operation order, and completion time.

[![训练甘特图演化 · Training Gantt evolution](assets/2_training_gantt.png)](https://wgy577.github.io/sortie-videos/videos/2_training_gantt.mp4)

▶ [在线播放 · Play](https://wgy577.github.io/sortie-videos/videos/2_training_gantt.mp4)

## 调度演示 · Scheduling demonstrations

### 从单机到双机并行 · From one aircraft to parallel dispatch

| 单机基准 · Single-aircraft baseline | 双机并行 · Two-aircraft parallel scheduling |
|:--:|:--:|
| [![单机出动 · Single aircraft](assets/3_sortie1.png)](https://wgy577.github.io/sortie-videos/videos/3_sortie1.mp4) | [![双机并行 · Two aircraft](assets/4_sortie2_parallel.png)](https://wgy577.github.io/sortie-videos/videos/4_sortie2_parallel.mp4) |
| 无机间竞争的顺序作业<br>Ordered operations without inter-aircraft competition | 共享资源引入排序与协同决策<br>Shared resources introduce sequencing and coordination decisions |
| [在线播放 · Play](https://wgy577.github.io/sortie-videos/videos/3_sortie1.mp4) | [在线播放 · Play](https://wgy577.github.io/sortie-videos/videos/4_sortie2_parallel.mp4) |

### 全规模场景：20 架舰载机 · Full-scale scenario: 20 aircraft

20 机场景展示完整的多阶段协调问题：多架舰载机竞争有限的阶段资源，局部派工决策会持续影响后续作业和最终 makespan。

The 20-aircraft case exposes the complete multi-stage coordination problem. Aircraft compete for limited resources, and each local dispatching choice propagates through downstream operations and the final makespan.

| 快速总览 · Fast overview | 高清细节 1.5× · HD 1.5× | 高清原速 · HD 1× |
|:--:|:--:|:--:|
| [![20 机快速演示 · 20 aircraft fast](assets/5_sortie20_fast.png)](https://wgy577.github.io/sortie-videos/videos/5_sortie20_fast.mp4) | [![20 机高清演示 · 20 aircraft HD](assets/6_sortie20_hd_1.5x.png)](https://wgy577.github.io/sortie-videos/videos/6_sortie20_hd_1.5x.mp4) | [![20 机高清原速 · 20 aircraft normal speed](assets/8_sortie20_hd_1x.png)](https://wgy577.github.io/sortie-videos/videos/8_sortie20_hd_1x.mp4) |
| [在线播放 · Play](https://wgy577.github.io/sortie-videos/videos/5_sortie20_fast.mp4) | [在线播放 · Play](https://wgy577.github.io/sortie-videos/videos/6_sortie20_hd_1.5x.mp4) | [在线播放 · Play](https://wgy577.github.io/sortie-videos/videos/8_sortie20_hd_1x.mp4) |

备选高清渲染 · Alternative HD rendering: [在线播放 · Play](https://wgy577.github.io/sortie-videos/videos/7_sortie20_hd_1.5x_alt.mp4)

### 任务编队：8 架舰载机 · Mission package: 8 aircraft

选机出动场景展示该方法对部分任务编队的调度能力，无需假设甲板上的全部舰载机同时出动。

The selected-aircraft scenario demonstrates scheduling for a partial mission package without assuming that every aircraft on deck must launch.

| 快速总览 · Fast overview | 高清完整过程 · HD complete process |
|:--:|:--:|
| [![8 机快速演示 · 8 aircraft fast](assets/9_sortie8_fast.png)](https://wgy577.github.io/sortie-videos/videos/9_sortie8_fast.mp4) | [![8 机高清演示 · 8 aircraft HD](assets/10_sortie8_hd.png)](https://wgy577.github.io/sortie-videos/videos/10_sortie8_hd.mp4) |
| [在线播放 · Play](https://wgy577.github.io/sortie-videos/videos/9_sortie8_fast.mp4) | [在线播放 · Play](https://wgy577.github.io/sortie-videos/videos/10_sortie8_hd.mp4) |

## 视频链接汇总 · Video index

下列在线视频均带有画面内缓慢移动水印与右下角固定署名。<br>
Every online video below contains a slow-moving in-frame watermark and a fixed lower-right signature.

| # | 场景 · Scenario | 在线播放 · Play |
|--:|:--|:--:|
| 01 | PPO 训练曲线 · PPO training curve | [播放 · Play](https://wgy577.github.io/sortie-videos/videos/1_training_curve.mp4) |
| 02 | 异步训练与甘特图演化 · Asynchronous training and Gantt evolution | [播放 · Play](https://wgy577.github.io/sortie-videos/videos/2_training_gantt.mp4) |
| 03 | 单机出动基准 · Single-aircraft baseline | [播放 · Play](https://wgy577.github.io/sortie-videos/videos/3_sortie1.mp4) |
| 04 | 双机并行调度 · Two-aircraft parallel dispatch | [播放 · Play](https://wgy577.github.io/sortie-videos/videos/4_sortie2_parallel.mp4) |
| 05 | 20 机快速总览 · 20-aircraft fast overview | [播放 · Play](https://wgy577.github.io/sortie-videos/videos/5_sortie20_fast.mp4) |
| 06 | 20 机高清 1.5× · 20-aircraft HD 1.5× | [播放 · Play](https://wgy577.github.io/sortie-videos/videos/6_sortie20_hd_1.5x.mp4) |
| 07 | 20 机高清 1.5× 备选 · 20-aircraft HD 1.5× alternate | [播放 · Play](https://wgy577.github.io/sortie-videos/videos/7_sortie20_hd_1.5x_alt.mp4) |
| 08 | 20 机高清原速 · 20-aircraft HD normal speed | [播放 · Play](https://wgy577.github.io/sortie-videos/videos/8_sortie20_hd_1x.mp4) |
| 09 | 8 机快速总览 · 8-aircraft fast overview | [播放 · Play](https://wgy577.github.io/sortie-videos/videos/9_sortie8_fast.mp4) |
| 10 | 8 机高清完整过程 · 8-aircraft HD complete process | [播放 · Play](https://wgy577.github.io/sortie-videos/videos/10_sortie8_hd.mp4) |

---

<div align="center">
大连理工大学吴光宇（导师与师兄指导） · Guangyu Wu at Dalian University of Technology, under the guidance of his academic advisor and senior lab colleagues
</div>
