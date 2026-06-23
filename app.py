import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


plt.rcParams['font.family'] = 'Noto Sans CJK SC'
plt.rcParams['axes.unicode_minus'] = False




from model import predict_parameters
from simulator import simulate
from safety import assess


# ======================
# 页面配置
# ======================
st.set_page_config(page_title="AI医疗激光决策系统", layout="centered")

st.title("🏆 AI医疗激光智能决策系统")
st.caption("AI辅助医学决策模拟系统 | 教学 / 科研 / 比赛演示")


# ======================
# 模式系统（3模式）
# ======================
mode = st.radio("选择系统模式", ["医生模式", "教学模式", "研究模式"])

if mode == "医生模式":
    st.info("⚠ 严格风险控制模式（偏保守）")
elif mode == "教学模式":
    st.info("📘 解释增强模式（可视化+讲解）")
else:
    st.info("🔬 参数研究模式（偏实验分析）")


# ======================
# 输入区
# ======================
st.markdown("## 📥 输入参数")

lesion_size = st.slider("病灶大小(mm)", 1.0, 20.0, 5.0)
depth = st.slider("病灶深度(mm)", 1.0, 30.0, 5.0)


# ======================
# 历史记录
# ======================
if "history" not in st.session_state:
    st.session_state.history = []


# ======================
# AI报告
# ======================
def generate_report(power, duration, temperature, damage, risk):

    return f"""
🧠 AI医疗分析报告

-------------------------
📌 激光参数：
- 功率：{power:.2f}
- 时间：{duration:.2f}

🌡 组织反应：
- 温度：{temperature:.2f}
- 损伤：{damage:.2f}

⚠ 风险等级：{risk}

📊 结论：
{"❌ 高风险操作" if risk=="DANGER" else "⚠ 中风险" if risk=="WARNING" else "✅ 安全可用"}
"""


# ======================
# ⭐雷达图（修复稳定版）
# ======================
def draw_radar(power, duration, damage, temperature):

  
    plt.rcParams["axes.unicode_minus"] = False

    labels = ["Power", "Duration", "Damage", "Temperature"]

    values = np.array([power, duration, damage, temperature], dtype=float)

    # ⭐归一化（防止图畸形）
    values = values / (np.max(values) + 1e-6)

    values = values.tolist()
    values += values[:1]

    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    fig = plt.figure()
    ax = plt.subplot(111, polar=True)

    ax.plot(angles, values, linewidth=3, label="Risk Intensity")
    ax.fill(angles, values, alpha=0.25)

    ax.set_thetagrids(np.degrees(angles[:-1]), labels)

    # ⭐图例修复
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))

    plt.tight_layout()
    st.pyplot(fig)


# ======================
# ⭐饼图（升级4维风险模型）
# ======================
def draw_pie(power, duration, damage, temperature):

   
    plt.rcParams["axes.unicode_minus"] = False

    labels = [
        "Energy Risk",
        "Exposure",
        "Tissue Damage",
        "Heat"
    ]

    values = [
        power / 100,
        duration / 10,
        damage / 50,
        temperature / 100
    ]

    # 防止异常
    if sum(values) == 0:
        values = [1, 1, 1, 1]

    fig, ax = plt.subplots()

    wedges, texts, autotexts = ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
        textprops={'fontsize': 10}
    )

    ax.set_title("Risk Composition Analysis")

    # ⭐图例（关键）
    ax.legend(wedges, labels, loc="center left", bbox_to_anchor=(1, 0.5))

    plt.tight_layout()
    st.pyplot(fig)


# ======================
# 风险解释
# ======================
def explain(risk):

    if risk == "DANGER":
        st.error("❌ 高风险：可能造成不可逆损伤")
    elif risk == "WARNING":
        st.warning("⚠ 中风险：需优化参数")
    else:
        st.success("✅ 安全范围内")


# ======================
# 主运行
# ======================
if st.button("🚀 开始AI分析（比赛演示）"):

    power, duration = predict_parameters(lesion_size, depth)

    temperature, damage = simulate(power, duration)

    risk = assess(damage, temperature)

    # ======================
    # 输出
    # ======================
    st.markdown("## 📊 AI分析结果")

    col1, col2, col3 = st.columns(3)
    col1.metric("功率", f"{power:.2f}")
    col2.metric("时间", f"{duration:.2f}")
    col3.metric("风险", risk)

    col4, col5 = st.columns(2)
    col4.metric("温度", f"{temperature:.2f}")
    col5.metric("损伤", f"{damage:.2f}")

    # ======================
    # 图表
    # ======================
    st.markdown("## 📈 多维分析图")

    draw_radar(power, duration, damage, temperature)
    draw_pie(power, duration, damage, temperature)

    # ======================
    # AI报告
    # ======================
    st.markdown("## 🧠 AI决策报告")

    st.text(generate_report(power, duration, temperature, damage, risk))

    explain(risk)

    # ======================
    # 历史
    # ======================
    st.session_state.history.append({
        "power": power,
        "duration": duration,
        "temperature": temperature,
        "damage": damage,
        "risk": risk
    })


# ======================
# 历史记录
# ======================
st.markdown("## 📚 历史记录")

for i, h in enumerate(st.session_state.history):
    st.write(
        f"{i+1}. 功率={h['power']:.2f}, 时间={h['duration']:.2f}, "
        f"温度={h['temperature']:.2f}, 损伤={h['damage']:.2f}, 风险={h['risk']}"
    )


# ======================
# 底部
# ======================
st.markdown("---")
st.caption("🏆 比赛终极版本 | AI医疗模拟系统 | 非真实临床用途")
