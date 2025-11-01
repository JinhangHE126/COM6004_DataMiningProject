# 🏥 Medical Appointment Scheduling System — Data Mining Project

[🇬🇧 English Version](./README.md)

## 一、数据集简介

**链接**： [Medical Appointment Scheduling System (Kaggle)](https://www.kaggle.com/datasets/carogonzalezgaltier/medical-appointment-scheduling-system)

**数据内容大致包括：**

- 患者 ID、性别、年龄
- 就诊日期、预约日期
- 医生 ID、科室
- 是否按时到诊 (`No-show` 或 `Attended`)
- 健康状况（如慢性病、有无保险等）
- 预约类型（急诊 / 普通门诊）
- 地理位置信息（城市、诊所）

> 💡 虽然该数据集是模拟生成的（synthetic），但其结构与真实世界的医疗调度系统非常接近，非常适合进行数据挖掘实验。

---

## 🔍 二、数据挖掘可做的方向（非常丰富）

可以从以下 **三个层次** 进行挖掘分析：

---

### 1️⃣ 预测类任务（Supervised Learning）

**目标**：预测病人是否会按时就诊 (`No-show`)

**应用意义**：提前预测爽约率，帮助医院优化资源调度（如减少空闲时段、合理安排医生）。

**可用算法：**

- Logistic Regression
- Random Forest / XGBoost
- Decision Tree / LightGBM

**可用特征：**

- 提前预约天数（就诊日期 − 预约日期）
- 患者年龄、性别、慢性病情况
- 历史出勤率
- 时间段（早上、下午）

🎯 **研究亮点**：

> 设计一个模型来“动态预测爽约概率”，并与优化算法结合做“资源重分配”。

---

### 2️⃣ 聚类与模式发现（Unsupervised Learning）

**目标**：找出不同类型的患者或就诊模式

**可行方向：**

- 聚类患者：根据年龄、就诊频率、疾病类型、爽约率等划分患者群体。
- 聚类医生 / 科室：根据工作负载、就诊量、患者满意度模式分组。
- 发现季节性规律：利用时间序列聚类或频繁模式挖掘找出“高峰期”。

**📊 示例输出：**

- 患者类型 A：年轻、常预约、爽约率高
- 患者类型 B：老年、慢性病、就诊规律性强

> → 可以据此调整不同人群的预约策略（如提前短信提醒、分时段预约）。

---

### 3️⃣ 优化与调度（Optimization + Simulation）

**目标**：优化医院的预约分配与资源利用

**策略思路：**

- 输入预测模型的结果（爽约概率）
- 使用优化算法（如线性规划、遗传算法、强化学习）进行资源分配

**调度问题可包括：**

- 医生排班优化
- 挂号时间分配优化
- 门诊负载均衡

**🧮 方法示例：**

- 用 `PuLP` 或 `Pyomo` 建模线性规划：最大化就诊人数、最小化等待时间。
- 用 `SimPy` 模拟不同预约策略（如 overbooking、double booking）的效果。

---

## 🧠 三、可作为数据挖掘项目的主题

| 方向       | 题目示例                                                                   | 技术关键词                            |
| ---------- | -------------------------------------------------------------------------- | ------------------------------------- |
| **预测**   | Predicting Patient No-Show in Medical Appointments                         | Logistic Regression, XGBoost          |
| **聚类**   | Discovering Appointment Behavior Patterns in Healthcare Systems            | K-Means, DBSCAN                       |
| **优化**   | Optimization of Medical Resource Scheduling Based on Attendance Prediction | Linear Programming, Genetic Algorithm |
| **可视化** | Temporal Analysis of Appointment and Attendance Trends                     | Time Series Plot, Heatmap             |
| **综合型** | Data-Driven Appointment Scheduling Optimization in Healthcare              | ML + Optimization                     |

---

## 🧩 四、总结建议

| 评估维度    | 表现                                 |
| ----------- | ------------------------------------ |
| ✅ 数据质量 | 清晰、干净（适合初学和项目使用）     |
| ✅ 隐私风险 | 模拟数据，无隐私问题                 |
| ✅ 可扩展性 | 可加入时间序列或 GIS 数据            |
| ✅ 学术潜力 | 高，可用于医疗资源调度优化研究       |
| 🚫 局限     | 无真实医院操作日志，部分变量随机生成 |

---

## 🚀 推荐组合方案（非常适合做课程项目或论文）

1. **Step 1**：使用数据挖掘算法预测患者爽约率
2. **Step 2**：基于预测结果构建调度优化模型（如最大化资源利用率）
3. **Step 3**：用可视化展示不同策略下的预约效率与患者满意度

最终可以形成一个完整的研究主题：

> 🎯 **“Data-Driven Medical Appointment Scheduling Optimization”**

---

# COM6004_DataMiningProject
