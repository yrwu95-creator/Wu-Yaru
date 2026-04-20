import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# ── 页面基础配置 ──────────────────────────────────────────────
st.set_page_config(
    page_title="回国生活成本计算器 🇨🇳",
    page_icon="🇨🇳",
    layout="centered",
)

# ── 自定义样式 ─────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* 隐藏 Streamlit 默认的 footer & 菜单 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* 主标题样式 */
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    /* 汇总卡片样式 */
    .summary-card {
        background: linear-gradient(135deg, #1f77b4 0%, #4a90e2 100%);
        color: white;
        padding: 1.2rem;
        border-radius: 12px;
        text-align: center;
        margin: 0.8rem 0;
        box-shadow: 0 4px 12px rgba(31, 119, 180, 0.25);
    }
    .summary-label { font-size: 0.9rem; opacity: 0.85; }
    .summary-value {
        font-size: 1.8rem;
        font-weight: 700;
        margin: 0.2rem 0 0 0;
    }

    /* 侧边栏标题 */
    .sidebar-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── 侧边栏：输入区 ────────────────────────────────────────────
st.sidebar.markdown('<p class="sidebar-title">📝 请输入你的月消费信息</p>', unsafe_allow_html=True)

# 城市预设数据（2024年参考数据）
CITY_PRESETS = {
    "上海": {"monthly_rent": 7000, "hotpot_price": 180},
    "成都": {"monthly_rent": 4000, "hotpot_price": 120},
    "深圳": {"monthly_rent": 6000, "hotpot_price": 150},
}

# 城市预设下拉框
selected_preset = st.sidebar.selectbox(
    "🏙️ 城市预设（可选）",
    options=["请选择城市预设..."] + list(CITY_PRESETS.keys()),
    help="选择一个城市预设，租金和火锅价格将自动填入，之后仍可手动修改",
)

# 城市名称输入（可手动修改）
city = st.sidebar.text_input(
    "🏙️ 所在城市",
    value="上海",
    help="例如：北京、上海、广州、深圳",
)

# 根据预设设置初始值
if selected_preset != "请选择城市预设...":
    preset_data = CITY_PRESETS[selected_preset]
    rent_help = f"💡 {selected_preset} 2024年平均房租参考：约 ¥{preset_data['monthly_rent']:,} 元"
    hotpot_help = f"💡 {selected_preset} 2024年火锅均价参考：约 ¥{preset_data['hotpot_price']} 元/顿"
else:
    preset_data = None
    rent_help = "💡 参考：一线城市平均 5000-8000 元/月"
    hotpot_help = "💡 参考：一线城市平均 120-200 元/顿"

monthly_rent = st.sidebar.number_input(
    "🏠 每月房租（元）",
    min_value=0,
    max_value=50000,
    value=preset_data["monthly_rent"] if preset_data else 5000,
    step=100,
    format="%d",
    help=rent_help,
)

hotpot_price = st.sidebar.number_input(
    "🍲 平均每顿火锅价格（元）",
    min_value=0,
    max_value=1000,
    value=preset_data["hotpot_price"] if preset_data else 150,
    step=10,
    format="%d",
    help=hotpot_help,
)

milk_tea_count = st.sidebar.number_input(
    "🧋 每月奶茶杯数",
    min_value=0,
    max_value=100,
    value=10,
    step=1,
    format="%d",
)

# ── 计算逻辑 ──────────────────────────────────────────────────
# 假设每月其他饮食开销 = 10 顿火锅 + 30 杯奶茶 + 其余日常饮食
# 这里简化：将奶茶价格按平均 15 元/杯 估算，其余饮食按 2000 元/月 估算
milk_tea_unit_price = 15  # 每杯奶茶均价（元）
milk_tea_cost = milk_tea_count * milk_tea_unit_price

hotpot_monthly_meals = 2  # 假设每月吃 2 顿火锅
hotpot_cost = hotpot_monthly_meals * hotpot_price

other_food_cost = 2000  # 其他日常饮食、外卖、水果等

total_cost = monthly_rent + milk_tea_cost + hotpot_cost + other_food_cost

# ── 主界面：标题 ─────────────────────────────────────────────
st.markdown('<p class="main-title">🇨🇳 回国生活成本计算器</p>', unsafe_allow_html=True)

# ── 汇总卡片 ─────────────────────────────────────────────────
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(
        f"""
        <div class="summary-card">
            <div class="summary-label">预估总月开销（{city}）</div>
            <div class="summary-value">¥ {total_cost:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── 数据分解展示 ─────────────────────────────────────────────
st.markdown("### 📊 开销构成分析")

# 构造饼图数据
categories = ["房租", "奶茶", "火锅", "其他饮食"]
values = [monthly_rent, milk_tea_cost, hotpot_cost, other_food_cost]

# 使用 Plotly 创建饼图
fig = go.Figure(
    data=[
        go.Pie(
            labels=categories,
            values=values,
            hole=0.4,
            marker=dict(colors=["#1f77b4", "#ff7f0e", "#2ca02c", "#9467bd"]),
            textinfo="label+percent",
            textposition="outside",
            hoverinfo="label+value+percent",
            sort=False,
        )
    ]
)

fig.update_layout(
    showlegend=False,
    height=400,
    margin=dict(t=20, b=20, l=20, r=20),
    font=dict(size=14),
)

st.plotly_chart(fig, use_container_width=True)

# ── 详细数据表格 ────────────────────────────────────────────
st.markdown("### 📋 详细开销列表")

col_a, col_b, col_c, col_d = st.columns(4)
col_a.metric("🏠 房租", f"¥{monthly_rent:,.0f}")
col_b.metric("🧋 奶茶", f"¥{milk_tea_cost:,.0f}")
col_c.metric("🍲 火锅", f"¥{hotpot_cost:,.0f}")
col_d.metric("🍎 其他饮食", f"¥{other_food_cost:,.0f}")

# ── 备注说明 ─────────────────────────────────────────────────
with st.expander("📌 计算说明与假设"):
    st.markdown(
        """
        **计算假设：**
        - 火锅：每月 2 顿，按你输入的单价计算
        - 奶茶：按每杯 15 元的均价 × 每月杯数
        - 其他饮食：包括日常三餐、外卖、水果等，暂估 ¥2,000/月
        - 房租：直接按输入值计算

        **注意：** 本计算器仅供参考，实际开销可能因个人消费习惯、城市区域、通勤方式等因素而异。
        """
    )
