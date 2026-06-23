# 🔬 激光医学AI辅助决策系统

---

## 🧠 项目简介

本项目是一个基于人工智能与物理模拟的激光医学辅助决策系统。

系统通过输入病灶大小和组织深度，自动预测激光治疗参数，并模拟激光对组织的物理作用，最终输出安全等级评估结果。

---

## 🚀 功能介绍

- AI自动预测激光功率与照射时间
- 激光作用物理模拟（温度 & 损伤）
- 安全等级判断（SAFE / WARNING / DANGER）
- 可视化界面展示（Streamlit）
- 医生/学生模式切换
- 历史记录保存

---

## 🏗️ 系统流程

输入病灶参数  
↓  
AI模型预测（model.py）  
↓  
物理模拟（simulator.py）  
↓  
安全评估（safety.py）  
↓  
UI界面展示（app.py）

---

## 📦 模块说明

### model.py（A模块）
- 输入：病灶大小、深度
- 输出：power（功率）、duration（时间）

---

### simulator.py
- 输入：power、duration
- 输出：temperature、damage

---

### safety.py
- 输入：damage
- 输出：risk等级

---

### app.py
- 系统UI界面
- 调用所有模块

---

## ⚙️ 安装依赖

```bash
pip install streamlit numpy matplotlib