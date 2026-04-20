import streamlit as st
from datetime import datetime, date
import time

# ── 页面配置 ──────────────────────────────────────────────────
st.set_page_config(
    page_title="小毋 的留日时光信箱 🇯🇵❤️🇨🇳",
    page_icon="🇯🇵",
    layout="centered",
)

# ── 暖黄色调自定义 CSS ────────────────────────────────────────
st.markdown(
    """
    <style>
    /* 基础背景和字体 */
    .main {
        background: linear-gradient(135deg, #fff9e6 0%, #fff5d6 50%, #ffe8b6 100%);
        font-family: 'Microsoft YaHei', 'PingFang SC', sans-serif;
    }

    /* 增大全局字体 */
    html, body, [class*="css"] {
        font-size: 18px !important;
    }

    /* 标题样式 - 温暖的大字 */
    .title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #d45500;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(212, 85, 0, 0.2);
    }

    /* 倒计时卡片 - 温馨橙色 */
    .countdown-card {
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
        border: 2px solid #ffb74d;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 8px 24px rgba(255, 152, 0, 0.2);
    }

    .countdown-days {
        font-size: 4rem;
        font-weight: 700;
        color: #e65100;
        margin: 0.5rem 0;
        text-shadow: 2px 2px 0px #fff;
    }

    .countdown-label {
        font-size: 1.2rem;
        color: #f57c00;
        font-weight: 600;
    }

    /* 互动按钮 - 大而可爱的按钮 */
    .stButton > button {
        width: 100%;
        height: 100px;
        font-size: 2rem;
        font-weight: 700;
        border-radius: 20px;
        border: none;
        margin: 0.8rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }

    .stButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
    }

    /* 不同按钮的颜色 */
    .eat-btn button {
        background: linear-gradient(135deg, #ff8a65 0%, #ff5722 100%);
        color: white;
    }

    .sleep-btn button {
        background: linear-gradient(135deg, #90caf9 0%, #2196f3 100%);
        color: white;
    }

    .study-btn button {
        background: linear-gradient(135deg, #a5d6a7 0%, #4caf50 100%);
        color: white;
    }

    /* 可爱提示框 */
    .cute-message {
        font-size: 1.8rem;
        font-weight: 600;
        color: #ff6f00;
        text-align: center;
        padding: 1.5rem;
        background: #fff8e1;
        border-radius: 15px;
        border: 2px dashed #ffc107;
        margin: 1rem 0;
        animation: bounce 0.6s ease-in-out;
    }

    @keyframes bounce {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }

    /* 侧边栏样式 */
    .sidebar-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #e65100;
        margin-bottom: 1rem;
    }

    .weather-card {
        background: #fff8e1;
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid #ffc107;
        margin: 0.8rem 0;
    }

    .weather-icon {
        font-size: 2.5rem;
        text-align: center;
    }

    .weather-text {
        font-size: 1.1rem;
        color: #f57c00;
        text-align: center;
        font-weight: 600;
    }

    .status-card {
        background: #f1f8e9;
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid #aed581;
        margin: 0.8rem 0;
    }

    .status-icon {
        font-size: 2.5rem;
        text-align: center;
    }

    .status-text {
        font-size: 1.1rem;
        color: #388e3c;
        text-align: center;
        font-weight: 600;
    }

    /* 隐藏 Streamlit 默认元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ── 侧边栏：心情同步 ───────────────────────────────────────────
st.sidebar.markdown('<p class="sidebar-title">🌤️ 日本实时心情</p>', unsafe_allow_html=True)

# 模拟天气（实际应用中可以接入天气 API）
import random
weather_conditions = [
    ("☀️", "晴天", "适合出门收集美好！"),
    ("🌤️", "多云", "微风正好，学习也美好~"),
    ("☁️", "阴天", "宅家学习编程，舒适又专注"),
    ("🌧️", "雨天", "听雨声，写代码，静心"),
    ("⛅", "雾天", "朦胧中也有清晰的思路"),
]
weather_emoji, weather_name, weather_desc = random.choice(weather_conditions)

st.sidebar.markdown(
    f"""
    <div class="weather-card">
        <div class="weather-icon">{weather_emoji}</div>
        <div class="weather-text">{weather_name}</div>
        <div style="font-size: 0.95rem; color: #f57c00; text-align: center; margin-top: 0.5rem;">
            {weather_desc}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 学习状态（根据时间和随机因素变化）
study_statuses = [
    ("💻", "正在编程中", "代码写得很顺利！"),
    ("📚", "啃书中", "今天学了新知识~"),
    ("🎨", "创意时间", "在做有趣的项目！"),
    ("☕", "休息中", "喝杯茶，继续加油"),
    ("🏃", "运动时间", "劳逸结合最棒了"),
]
status_emoji, status_title, status_desc = random.choice(study_statuses)

st.sidebar.markdown(
    f"""
    <div class="status-card">
        <div class="status-icon">{status_emoji}</div>
        <div class="status-text">{status_title}</div>
        <div style="font-size: 0.95rem; color: #388e3c; text-align: center; margin-top: 0.5rem;">
            {status_desc}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.info("💡 注：天气和学习状态每日随机更新，给你惊喜~")

# ── 主标题 ────────────────────────────────────────────────────
st.markdown('<p class="title">小毋 的留日时光信箱 🇯🇵❤️🇨🇳</p>', unsafe_allow_html=True)

# ── 倒计时模块 ────────────────────────────────────────────────
# 2027年春节是 2027-01-29（农历正月初一）
spring_festival_2027 = date(2027, 1, 29)
today = date.today()
days_left = (spring_festival_2027 - today).days

st.markdown(
    f"""
    <div class="countdown-card">
        <div class="countdown-label">📅 距离 2027 年春节还有</div>
        <div class="countdown-days">{days_left}</div>
        <div class="countdown-label">天 🌸</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── 互动按钮区域 ──────────────────────────────────────────────
st.markdown("### 💌 给爸妈的互动留言")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="eat-btn">', unsafe_allow_html=True)
    if st.button("🍜 好好吃饭", use_container_width=True):
        st.success("✨ 收到！要吃嘛嘛香，营养均衡~")
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="sleep-btn">', unsafe_allow_html=True)
    if st.button("😴 好好睡觉", use_container_width=True):
        st.success("✨ 收到！早点休息，做个好梦~")
        st.snow()
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="study-btn">', unsafe_allow_html=True)
    if st.button("📚 加油学习", use_container_width=True):
        st.success("✨ 收到！努力的同时别忘了休息~")
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# ── 温馨寄语 ─────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; font-size: 1.1rem; color: #e65100; padding: 1rem;">
        🌸 爸妈请放心，我在日本一切都好<br>
        💙 记得按时吃饭，早点睡觉，别太想我哦~<br>
        <br>
        <span style="font-size: 0.9rem; color: #888;">
            爱你们的 小毋 🇯🇵❤️🇨🇳
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)
