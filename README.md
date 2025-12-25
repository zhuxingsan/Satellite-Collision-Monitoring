# 🛰️ Satellite Collision Monitoring System
# 🛰️ 卫星碰撞预警监测系统 (HOLO-SYS)

> **A High-Fidelity 3D Orbital Visualization & Conjunction Assessment Platform**
> **基于高保真 3D 渲染的实时轨道监测与碰撞风险评估平台**

![Status](https://img.shields.io/badge/Status-Release-success?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square)
![Stack](https://img.shields.io/badge/Tech-Python_%7C_CesiumJS_%7C_Flask-blue?style=flat-square)
![License](https://img.shields.io/badge/License-Commercial_Prohibited-red?style=flat-square)

![Main Dashboard](https://via.placeholder.com/800x450.png?text=Please+Replace+This+With+Your+Software+Screenshot)

---

## 📖 Overview / 项目概述

**This System** is a professional satellite monitoring platform designed to visualize orbital mechanics and assess collision risks in real-time. Built with a high-performance **Python backend** (Flask + Scipy) and a **CesiumJS-based frontend**, it delivers a cinematic sci-fi user interface while performing rigorous orbital propagation (SGP4) and conjunction analysis.

The system is engineered to bridge the gap between complex astrodynamics data and intuitive visualization, providing operators with immediate situational awareness of space assets.

**本系统** 是一款专业的卫星监测与碰撞预警平台，旨在实时可视化轨道力学并评估空间物体碰撞风险。项目采用高性能 **Python 后端** (Flask + Scipy) 与 **CesiumJS 前端** 架构，在提供电影级科幻 UI 的同时，执行严谨的 SGP4 轨道推演与交会分析。

该系统的核心目标是消除复杂的航天动力学数据与直观可视化之间的鸿沟，为操作者提供即时的空间资产态势感知能力。

---

## ✨ Key Features / 核心功能

* **🌍 Real-time 3D Visualization**: Powered by **CesiumJS**, rendering thousands of satellites, debris, and space stations with high-fidelity Earth textures.
    * **实时 3D 可视化**：基于 **CesiumJS** 引擎，高保真渲染地球纹理及数千颗卫星、空间站与碎片。

* **🚀 SGP4 Orbit Propagation**: Implements industry-standard SGP4 algorithms to calculate real-time satellite positions from TLE (Two-Line Element) data.
    * **SGP4 轨道推演**：集成工业级 SGP4 算法，基于 TLE 数据实时解算卫星位置与速度。

* **⚠️ Conjunction Assessment**: Automated analysis of collision risks between space objects, calculating minimum distance and collision probability.
    * **碰撞预警分析**：自动评估空间物体间的碰撞风险，计算最小交会距离与碰撞概率。

* **📡 Live Data Synchronization**: Integrated with **CelesTrak API** to auto-fetch and categorize the latest orbital data (Active, Stations, Debris).
    * **实时数据同步**：对接 **CelesTrak API**，自动获取并分类最新的轨道数据（现役卫星、空间站、太空垃圾）。

* **💻 Portable Deployment**: Fully packaged as a standalone **Windows Executable (.exe)**, requiring no Python environment setup.
    * **便携式部署**：封装为独立的 **Windows 可执行文件 (.exe)**，无需配置 Python 环境，即插即用。

---

## 📥 Download & Usage / 下载与使用

This project is distributed as a portable executable. **No installation required.**
本项目以绿色免安装包形式发布，**无需安装**。

### Step 1: Download & Unzip (下载与解压)
1.  Go to the [**Releases Page**](../../releases) and download the latest `.zip` file.
    * 前往 [**Releases 页面**](../../releases) 下载最新的 `.zip` 压缩包。
2.  Unzip the entire folder to a local directory (e.g., Desktop). **Keep the `processed_data` folder alongside the `.exe`.**
    * 将压缩包完整解压到本地（如桌面）。**请务必确保 `processed_data` 文件夹与 `.exe` 在同一目录下。**

### Step 2: Launch Server (启动服务)
3.  Double-click `SatelliteSystem.exe`. A command line window (black box) will appear.
    * 双击运行 `SatelliteSystem.exe`。此时会弹出一个黑色命令行窗口。
4.  Wait until you see the message: `Running on http://127.0.0.1:8000`.
    * 等待窗口中显示 `Running on http://127.0.0.1:8000` 字样。

### Step 3: Access Interface (访问界面)
5.  **Keep the command window open.** Open your web browser (Chrome/Edge) and visit:
    * **保持黑色窗口开启**（不要关闭）。打开浏览器（推荐 Chrome 或 Edge），访问以下地址：
    > **http://127.0.0.1:8000**

---

## 📸 Screenshots / 界面展示

| Orbit Visualization (轨道可视化) | Collision Analysis (碰撞分析) |
|:---:|:---:|
| ![Orbit](https://via.placeholder.com/400x250.png?text=Please+Upload+Screenshot) | ![Analysis](https://via.placeholder.com/400x250.png?text=Please+Upload+Screenshot) |

---

## ⚖️ License & Disclaimer / 许可与免责声明

### 🔴 Commercial Use Prohibited / 严禁商用
**This software is proprietary.** The source code, algorithms, and binary distributions are protected by copyright laws.
**本软件为专有软件。** 其源代码、核心算法及编译后的二进制文件均受版权法保护。

1.  **Non-Commercial Use Only**: This software is permitted for **personal study, academic research, and non-profit demonstration only**.
    * **仅限非商业用途**：本软件仅允许用于个人学习、学术研究及非营利性演示。
2.  **No Authorization**: Any commercial use, redistribution, or modification without explicit written permission from the author is **strictly prohibited**.
    * **未授权禁止使用**：未经作者书面许可，**严禁**将本软件用于任何商业活动、二次分发或修改。
3.  **No Warranty**: This software is provided "as is", without warranty of any kind. The author is not responsible for any issues caused by the use of this software.
    * **免责说明**：本软件按“原样”提供，不提供任何形式的担保。作者不对因使用本软件而产生的任何后果负责。

* **Data Source Note**: Satellite TLE data is sourced from public APIs (CelesTrak / Space-Track).
* **Security Note**: Core logic is protected by **PyArmor**. Reverse engineering is prohibited.

---
*© 2025 Development Team. All Rights Reserved.*
