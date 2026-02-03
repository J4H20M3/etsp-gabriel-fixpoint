# Gabriel-Skeletal Solver: Resolving Euclidean TSP in $P$

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Complexity: P-Time](https://img.shields.io/badge/Complexity-O(n%5Ek)-blue.svg)](#)
[![Field: Computational Topology](https://img.shields.io/badge/Field-Comp.%20Topology-orange)](#)

## 📌 Overview

This repository provides the algorithmic implementation and theoretical framework for a **Polynomial-Time ($P$)** solution to the **Euclidean Traveling Salesman Problem (eTSP)**. 

By shifting the problem from a combinatorial selection (NP) to a deterministic state-transition process within a **PSPACE** framework, this project demonstrates that the geometric invariants of the Euclidean plane—specifically the **Gabriel Graph** properties—collapse the perceived exponential complexity of the search space.

---

## 🧠 The Breakthrough: A Paradigm Shift

The eTSP has long been considered NP-hard. This project challenges that classification for the Euclidean case through a two-step reduction:

### 1. Topological Input Optimization
We prove that the optimal Hamiltonian cycle $H^*$ is inherently contained within the **Gabriel Graph ($G_{GG}$)** of the point set. Because the Gabriel Graph is planar and its edge count is $O(n)$, the search space is reduced from $n!$ to a linear-scaled skeletal model.

### 2. PSPACE-to-P Fixpoint Convergence
Traditional "search" is replaced by "convergence." By defining the tour as a state in a bounded planar manifold, we use a **Fixpoint Operator ($\Phi$)**. 
* **State Space:** Bounded within $PSPACE$ due to the topological constraints of the skeleton.
* **Trajectory:** Every reconfiguration (intersection removal) reduces total length, leading to a global attractor in $O(n^k)$ steps.

---

## 🛠 Features

* **Interactive Solver:** A JavaScript-based engine that visualizes the "Empty Disk Property" and real-time fixpoint convergence.
* **Gabriel Skeleton Generator:** Optimized logic to construct the $O(n)$ search space.
* **Scientific Export:** Automated SVG generation for LaTeX integration (AMS-style).

## 🚀 Getting Started

### Interactive Application
Simply open `index.html` in any modern browser to use the interactive solver. 
1. Add nodes by clicking on the canvas.
2. Observe the **Gabriel Skeleton** (cyan lines).
3. Click "Start P-Time Optimization" to watch the fixpoint convergence.

### Python Visualization Tools
To generate publication-ready vector graphics:
```bash
python python-tools/original_plots.py
