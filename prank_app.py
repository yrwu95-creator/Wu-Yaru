import streamlit as st
import time
import random
from datetime import datetime

# ── 页面配置 ──────────────────────────────────────────────────
st.set_page_config(
    page_title="基于深度学习的人类颜值与前途预测系统",
    page_icon="🤖",
    layout="centered",
)

# ── 高级深蓝色科技感 CSS ─────────────────────────────────────
st.markdown(
    """
    <style>
    /* 基础背景 - 深邃科技蓝 */
    .main {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f1629 100%);
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    }

    /* 标题样式 - 科技蓝发光效果 */
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #00d4ff;
        text-align: center;
        margin-bottom: 1.5rem;
        text-shadow: 0 0 10px #00d4ff, 0 0 20px #0099cc;
        letter-spacing: 2px;
    }

    .subtitle {
        font-size: 1rem;
        color: #7ec8e3;
        text-align: center;
        margin-bottom: 2rem;
        font-style: italic;
    }

    /* 上传区域样式 */
    .upload-area {
        border: 2px dashed #00d4ff;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        background: rgba(0, 212, 255, 0.05);
        margin: 1.5rem 0;
    }

    /* 扫描进度条 */
    .progress-text {
        color: #00d4ff;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        text-align: center;
    }

    /* 结果卡片 */
    .result-card {
        background: linear-gradient(135deg, #1e3a5f 0%, #0f2744 100%);
        border: 2px solid #00d4ff;
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
    }

    .result-emoji {
        font-size: 4rem;
        text-align: center;
        margin: 1rem 0;
    }

    .result-text {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ff6b6b;
        text-align: center;
        margin: 1rem 0;
        text-shadow: 0 0 10px rgba(255, 107, 107, 0.5);
    }

    .result-subtext {
        font-size: 1.1rem;
        color: #7ec8e3;
        text-align: center;
        font-style: italic;
    }

    /* 彩蛋按钮容器 - 相对定位用于随机移动 */
    #eggy-btn-container {
        position: relative;
        height: 120px;
        margin: 2rem 0;
        background: rgba(255, 107, 107, 0.1);
        border-radius: 15px;
        border: 2px dashed #ff6b6b;
    }

    /* 彩蛋按钮 */
    .eggy-btn button {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a5a 100%) !important;
        color: white !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        border-radius: 15px !important;
        border: none !important;
        padding: 1rem 2rem !important;
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4) !important;
        transition: all 0.2s ease !important;
    }

    .eggy-btn button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 8px 30px rgba(255, 107, 107, 0.6) !important;
    }

    /* 损话标签 */
    .roast-tag {
        display: inline-block;
        background: rgba(255, 107, 107, 0.2);
        color: #ff6b6b;
        padding: 0.3rem 0.8rem;
        border-radius: 8px;
        font-size: 0.9rem;
        margin: 0.2rem;
        border: 1px solid #ff6b6b;
    }

    /* 隐藏 Streamlit 默认元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* 文件上传器文字颜色 */
    .css-1cpxqw2 e1b2p5ww1 {
        color: #00d4ff !important;
    }

    /* 按钮通用样式覆盖 */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── 损话库 ─────────────────────────────────────────────────────
ROASTS = [
    ("🤖", "检测到此人智商欠费，建议多喝热水。"),
    ("💡", "颜值超过全国 0.01% 的电线杆。"),
    ("⚠️", "发际线预警：未来三年将成为中国最闪亮的灯泡。"),
    ("🧬", "基因检测显示：适合去火星开拓新世界。"),
    ("📊", "根据大数据分析，建议购买防脱发洗发水。"),
    ("🍜", "面相分析：最近有吃泡面的运势。"),
    ("🎭", "命运判定：适合从事演员行业（群演）。"),
    ("💼", "事业预测：三年内有望成为小区保安队长。"),
    ("🏠", "财运分析：建议把钱包挂在狗身上。"),
    ("☕", "精神状态：像极了周一早上的我。"),
    ("🌟", "幸运值：出门记得带伞（防柠檬精）。"),
    ("📱", "社交指数：和手机的感情最稳定。"),
    ("🧮", "数学能力：计算器都嫌你算得太慢。"),
    ("🎮", "游戏天赋：建议把'菜'字刻在墓碑上。"),
    ("🍀", "桃花运：单身狗抱团取暖吧。"),
]

# ── 标题 ───────────────────────────────────────────────────────
st.markdown('<p class="main-title">🤖 基于深度学习的人类颜值与前途预测系统</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">✨ 采用 128 维面部特征分析 + 量子计算机级算力 ✨</p>', unsafe_allow_html=True)

# ── 侧边栏 ─────────────────────────────────────────────────────
st.sidebar.markdown("### 📊 系统状态")
st.sidebar.success("✅ AI 模型已加载")
st.sidebar.success("✅ 超算中心已连接")
st.sidebar.warning("⚠️ 当前预测准确率：0.0001%")
st.sidebar.info("💡 本系统仅供娱乐，如有雷同纯属巧合")

# ── 照片上传 ───────────────────────────────────────────────────
st.markdown("### 📸 第一步：上传您的照片")
uploaded_file = st.file_uploader(
    "支持 JPG、PNG 格式",
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed",
)

if uploaded_file is not None:
    # 显示上传的照片
    st.image(uploaded_file, caption="✅ 照片上传成功", use_container_width=True)

    # AI 扫描按钮
    st.markdown("### 🔍 第二步：开始 AI 深度扫描")
    if st.button("🚀 开始 AI 深度扫描", use_container_width=True):
        # 扫描文案序列
        scan_messages = [
            "正在分析 128 维面部特征...",
            "对比日本牛郎店平均水平...",
            "正在连接东京大学超算中心...",
            "正在分���发际线高度...",
            "计算颜值与财富相关性...",
            "正在咨询日本整形医院报价...",
            "分析面相与运势关联...",
            "量子计算加速中...",
        ]

        # 创建进度条
        progress_bar = st.progress(0)
        status_text = st.empty()

        # 模拟扫描过程
        for i, msg in enumerate(scan_messages):
            status_text.markdown(f"<div class='progress-text'>{msg}</div>", unsafe_allow_html=True)
            progress = (i + 1) / len(scan_messages)
            progress_bar.progress(progress)
            time.sleep(0.4)  # 每步 0.4 秒

        time.sleep(1)  # 最后停顿一下

        # 清除进度条和文字
        progress_bar.empty()
        status_text.empty()

        # ── 随机结果展示 ────────────────────────────────────────
        emoji, roast = random.choice(ROASTS)

        st.markdown("### 📋 AI 分析报告")
        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-emoji">{emoji}</div>
                <div class="result-text">{roast}</div>
                <div class="result-subtext">
                    分析时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
                    模型版本：DeepRoast v2.0.2027<br>
                    算力消耗：∞  TFLOPS
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # 添加一些随机标签增加趣味
        tags = random.sample([
            "💔 单身预兆", "🍜 泡面命", "📱 手机依赖", "😴 睡不醒",
            "🧠 脑细胞活跃", "💸 财运平平", "🍀  random 幸运",
        ], 3)
        st.markdown("**🔖 运势标签：**")
        for tag in tags:
            st.markdown(f"<span class='roast-tag'>{tag}</span>", unsafe_allow_html=True)

        # ── 彩蛋按钮 ──────────────────────────────────────────
        st.markdown("---")
        st.markdown("### 🥚 想要获取真实评价？")

        # 创建按钮容器
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            # 使用 session state 跟踪按钮位置
            if "btn_x" not in st.session_state:
                st.session_state.btn_x = 0
                st.session_state.btn_y = 0
                st.session_state.show_btn = True

            # 容器用于定位按钮
            btn_container = st.container()

            # 如果按钮应该显示
            if st.session_state.show_btn:
                with btn_container:
                    # 使用自定义 HTML 和 JavaScript 实现移动效果
                    st.markdown(
                        f"""
                        <div id="eggy-btn-wrapper" style="position: relative; height: 120px;">
                            <button id="eggy-real-btn"
                                    style="position: absolute; left: {st.session_state.btn_x}px; top: {st.session_state.btn_y}px;
                                           background: linear-gradient(135deg, #ff6b6b 0%, #ee5a5a 100%);
                                           color: white; border: none; padding: 1rem 2rem;
                                           border-radius: 15px; font-size: 1.2rem; font-weight: 700;
                                           cursor: pointer; box-shadow: 0 6px 20px rgba(255,107,107,0.4);
                                           transition: all 0.2s ease;">
                                🙏 求饶并获取真实评价
                            </button>
                        </div>
                        <script>
                            // 按钮点击事件
                            document.getElementById('eggy-real-btn').addEventListener('click', function(e) {{
                                alert('想得美！😛');
                                this.style.transform = 'scale(0.8)';
                                setTimeout(() => {{
                                    this.style.transform = 'scale(1)';
                                }}, 200);
                            }});
                        </script>
                        """,
                        unsafe_allow_html=True,
                    )

            # Streamlit 按钮作为备用（当 JavaScript 被禁用时）
            if st.button("🙏 求饶并获取真实评价", key="eggy_backup"):
                st.error("想得美！😛")

else:
    st.info("👆 请先上传一张照片，开始 AI 扫描~")

# ── 页脚 ───────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #7ec8e3; font-size: 0.9rem; padding: 1rem;">
        🤖 System v2.0.2027 | Powered by 东京大学超算中心<br>
        ⚠️ 本系统纯属娱乐，预测结果不具任何科学依据，请勿当真~
    </div>
    """,
    unsafe_allow_html=True,
)
