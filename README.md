# Sortie — Carrier Aircraft Scheduling Visualization

Based on **FJSP (Flexible Job Shop Scheduling)**, studying the dispatching problem of carrier-based aircraft launching from aircraft carriers.

The core question: **Multiple aircraft, multiple catapults, various support equipment — how to schedule them so all aircraft launch in the shortest time without conflict?**

We use **PPO (Proximal Policy Optimization)** to train an agent that learns to make these scheduling decisions, and visualize the complete animation below.

---

## 1. Training Process

First, look at how the algorithm learns.

### ① Training Curve

PPO training reward curve. The vertical axis represents the score obtained per scheduling episode, and the horizontal axis is the training steps. As training progresses, the reward gradually increases and converges — meaning the agent is learning to schedule more efficiently, wasting less time on conflicts and idle waits.

<video src="https://raw.githubusercontent.com/wgy577/Sortie/main/videos/1_training_curve.mp4" width="800" controls></video>

### ② Training Episode → Gantt Demo

A single training episode compressed into a Gantt chart. Each row is an aircraft, each colored block is an operation (taxi to catapult, launch, etc.). You can see how the agent arranges the sequence of operations on the time axis and which aircraft are being served by which catapults at any given moment.

<video src="https://raw.githubusercontent.com/wgy577/Sortie/main/videos/2_training_gantt.mp4" width="800" controls></video>

---

## 2. Small-scale Demos: Understanding How Scheduling Works

Before showing the full-scale scenario, let's start with the simplest cases to understand "what is carrier aircraft scheduling."

### ③ Single Aircraft Sortie

When there is only one aircraft: the tractor positions the aircraft → tractor tows it to the catapult → catapult launches → aircraft leaves. The baseline scenario. All complex coordination stems from this simple process.

<video src="https://raw.githubusercontent.com/wgy577/Sortie/main/videos/3_sortie1.mp4" width="800" controls></video>

### ④ Two Aircraft Parallel

Two aircraft launch simultaneously. The problem begins: **limited catapults, limited tractors** — who goes first? How to avoid waiting? This is where the value of FJSP lies, and the agent must make optimal decisions for such resource competition.

<video src="https://raw.githubusercontent.com/wgy577/Sortie/main/videos/4_sortie2_parallel.mp4" width="800" controls></video>

---

## 3. Full Scale: All 20 Aircraft

This is the complete problem scale — 20 aircraft on the carrier deck, competing for 4 catapults and various support equipment. The complexity increases exponentially.

### ⑤ 20 Aircraft Fast Demo

Low-frame-rate fast version, for a quick overview of the entire dispatch rhythm. You can see how the agent batches aircraft and assigns them to different catapults, flowing continuously rather than one by one.

<video src="https://raw.githubusercontent.com/wgy577/Sortie/main/videos/5_sortie20_fast.mp4" width="800" controls></video>

### ⑥ 20 Aircraft HD (1.5× Speed)

High-definition detail version (1.5× speed). Aircraft movements, towing trajectories, and the catapult launch moment are all clearly visible — you can see every aircraft being towed into position, the catapult firing, and the aircraft departing.

<video src="https://raw.githubusercontent.com/wgy577/Sortie/main/videos/6_sortie20_hd_1.5x.mp4" width="800" controls></video>

### ⑦ 20 Aircraft HD (1× Speed, Full Details)

High-definition detail version at normal speed. For frame-by-frame observation of each aircraft's complete motion path and handoff timing.

<video src="https://raw.githubusercontent.com/wgy577/Sortie/main/videos/8_sortie20_hd_1x.mp4" width="800" controls></video>

---

## 4. Small Package Scenario: 8 Selected Aircraft

Real task are often not launched with all aircraft, but a subset is selected. The following shows 8 aircraft being selected for a small package mission.

### ⑧ 8 Aircraft Fast Demo

8 selected aircraft, low-frame-rate fast version. Quickly demonstrating the dispatch scenario when a small package launches.

<video src="https://raw.githubusercontent.com/wgy577/Sortie/main/videos/9_sortie8_fast.mp4" width="800" controls></video>

### ⑨ 8 Aircraft HD (Full Process)

High-definition complete process version. From tractor positioning the aircraft, towing to the catapult, to launch — every step of every aircraft is rendered in detail.

<video src="https://raw.githubusercontent.com/wgy577/Sortie/main/videos/10_sortie8_hd.mp4" width="800" controls></video>

---

## File Overview

| # | File | Description |
|---|------|-------------|
| 1 | `videos/1_training_curve.mp4` | PPO training reward curve |
| 2 | `videos/2_training_gantt.mp4` | Training episode → Gantt chart |
| 3 | `videos/3_sortie1.mp4` | Single aircraft sortie (baseline) |
| 4 | `videos/4_sortie2_parallel.mp4` | Two aircraft parallel |
| 5 | `videos/5_sortie20_fast.mp4` | 20 aircraft fast demo |
| 6 | `videos/6_sortie20_hd_1.5x.mp4` | 20 aircraft HD (1.5× speed) |
| 7 | `videos/8_sortie20_hd_1x.mp4` | 20 aircraft HD (normal speed) |
| 8 | `videos/9_sortie8_fast.mp4` | Aircraft fast demo |
| 9 | `videos/10_sortie8_hd.mp4` | Aircraft HD complete process |
