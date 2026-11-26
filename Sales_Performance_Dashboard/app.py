
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Sales Studio",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"], [data-testid="stApp"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #F8F5FC;
    color: #40364D;
}

[data-testid="stHeader"] {
    background: #F8F5FC;
}

[data-testid="stSidebar"] {
    background: #F0EAF7;
    border-right: 1px solid #E5D9EF;
}

[data-testid="stSidebar"] * {
    color: #514260;
}

[data-testid="stSidebar"] h2 {
    font-size: 23px;
    font-weight: 700;
}

.stApp h1, .stApp h2, .stApp h3 {
    color: #514260 !important;
    font-weight: 700;
}

.stApp p, .stApp label {
    color: #655B70;
}

.report-label {
    color: #A17AB8;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.report-title {
    color: #514260;
    font-size: 38px;
    font-weight: 800;
    margin-top: 5px;
}

.report-subtitle {
    color: #82758E;
    font-size: 15px;
    margin-bottom: 20px;
}

.metric-card {
    background-color: #FFFFFF;
    border: 1px solid #EAE2F0;
    border-radius: 16px;
    padding: 20px;
    min-height: 120px;
    box-shadow: 0 3px 12px rgba(91, 67, 112, 0.06);
}

.metric-label {
    color: #897B96;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
}

.metric-value {
    color: #57466B;
    font-size: 27px;
    font-weight: 800;
    margin-top: 12px;
}

.section-note {
    color: #92869C;
    font-size: 13px;
    margin-top: -10px;
    margin-bottom: 15px;
}

.insight-card {
    background-color: #FFFFFF;
    border: 1px solid #EAE2F0;
    border-left: 4px solid #B89ACD;
    border-radius: 12px;
    padding: 18px;
    color: #57466B;
    min-height: 95px;
    box-shadow: 0 3px 12px rgba(91, 67, 112, 0.05);
}

.insight-card b {
    color: #9A76B2;
}

div[data-testid="stPlotlyChart"] {
    background-color: #FFFFFF !important;
    border: 1px solid #EAE2F0;
    border-radius: 16px;
    padding: 12px;
    box-shadow: 0 3px 12px rgba(91, 67, 112, 0.05);
}

div[data-testid="stDataFrame"] {
    background-color: #FFFFFF;
    border: 1px solid #EAE2F0;
    border-radius: 12px;
}

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background-color: #FFFFFF;
    border-color: #DCCFE8;
    border-radius: 9px;
}

.stButton button {
    background: #A98BC1;
    color: white;
    border: none;
    border-radius: 10px;
}

hr {
    border-color: #E8DFEF;
}

[data-testid="stExpander"] {
    background: #FFFFFF;
    border: 1px solid #EAE2F0;
    border-radius: 12px;
}

[data-testid="stMetric"] {
    background: #FFFFFF;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    data = pd.read_csv("sales_data.csv")
    data["Date"] = pd.to_datetime(data["Date"])
    return data

df = load_data()

st.sidebar.markdown("## ✿ Sales Studio")
st.sidebar.caption("Your sales report, your way")
st.sidebar.divider()

regions = st.sidebar.multiselect(
    "Choose Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

products = st.sidebar.multiselect(
    "Choose Product",
    options=sorted(df["Product"].unique()),
    default=sorted(df["Product"].unique())
)

start_date = st.sidebar.date_input(
    "Start Date",
    value=df["Date"].min().date()
)

end_date = st.sidebar.date_input(
    "End Date",
    value=df["Date"].max().date()
)

st.sidebar.divider()
st.sidebar.caption("SALES REPORT · 2026")
st.sidebar.caption("Made with Python & Streamlit")

if start_date > end_date:
    st.error("Please select a valid date range.")
    st.stop()

filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Product"].isin(products)) &
    (df["Date"].dt.date >= start_date) &
    (df["Date"].dt.date <= end_date)
]

if filtered_df.empty:
    st.warning("No records found. Please change your filters.")
    st.stop()

total_revenue = filtered_df["Revenue"].sum()
total_orders = filtered_df["Order_ID"].nunique()
total_quantity = filtered_df["Quantity"].sum()
average_order_value = total_revenue / total_orders

st.markdown(
    '<div class="report-label">YOUR BUSINESS AT A GLANCE ✿</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="report-title">Sales Overview</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="report-subtitle">'
    'A simple overview of sales, products and regional performance.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

st.markdown("### Performance Summary")

c1, c2, c3, c4 = st.columns(4)

metrics = [
    ("TOTAL REVENUE", f"₹{total_revenue:,.0f}"),
    ("TOTAL ORDERS", f"{total_orders:,}"),
    ("UNITS SOLD", f"{total_quantity:,}"),
    ("AVERAGE ORDER VALUE", f"₹{average_order_value:,.2f}")
]

for col, (label, value) in zip([c1, c2, c3, c4], metrics):
    with col:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("")
st.divider()

st.markdown("### Revenue Trend")
st.markdown(
    '<div class="section-note">Monthly revenue across the selected period</div>',
    unsafe_allow_html=True
)

monthly = filtered_df.copy()
monthly["Month"] = monthly["Date"].dt.to_period("M").astype(str)
monthly = monthly.groupby("Month")["Revenue"].sum().reset_index()

fig1 = px.line(
    monthly,
    x="Month",
    y="Revenue",
    markers=True
)

fig1.update_traces(
    line=dict(color="#A98BC1", width=3),
    marker=dict(size=9, color="#D99AA8"),
    fill="tozeroy",
    fillcolor="rgba(197, 166, 217, 0.16)"
)

fig1.update_layout(
    template="plotly_white",
    height=350,
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",
    font=dict(color="#514260", family="DM Sans"),
    margin=dict(l=25, r=25, t=20, b=25),
    xaxis_title="Month",
    yaxis_title="Revenue (₹)",
    showlegend=False
)

fig1.update_xaxes(showgrid=False, linecolor="#EAE2F0")
fig1.update_yaxes(gridcolor="#F0EAF5", zeroline=False)

st.plotly_chart(fig1, use_container_width=True)

st.divider()

left, right = st.columns(2)

with left:
    st.markdown("### Product Performance")
    st.markdown(
        '<div class="section-note">Revenue generated by each product</div>',
        unsafe_allow_html=True
    )

    product_sales = (
        filtered_df.groupby("Product")["Revenue"]
        .sum()
        .reset_index()
        .sort_values("Revenue", ascending=True)
    )

    fig2 = px.bar(
        product_sales,
        x="Revenue",
        y="Product",
        orientation="h",
        text_auto=".2s"
    )

    fig2.update_traces(
        marker_color="#B89ACD",
        textposition="outside",
        textfont=dict(color="#514260")
    )

    fig2.update_layout(
        template="plotly_white",
        height=370,
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(color="#514260", family="DM Sans"),
        margin=dict(l=15, r=35, t=20, b=25),
        xaxis_title="Revenue (₹)",
        yaxis_title=""
    )

    fig2.update_xaxes(gridcolor="#F0EAF5")
    fig2.update_yaxes(showgrid=False)

    st.plotly_chart(fig2, use_container_width=True)

with right:
    st.markdown("### Regional Distribution")
    st.markdown(
        '<div class="section-note">Revenue share across all regions</div>',
        unsafe_allow_html=True
    )

    region_sales = (
        filtered_df.groupby("Region")["Revenue"]
        .sum()
        .reset_index()
    )

    fig3 = px.pie(
        region_sales,
        names="Region",
        values="Revenue",
        hole=0.55
    )

    fig3.update_traces(
        marker=dict(
            colors=["#A98BC1", "#D99AA8", "#E8C5D0", "#C5B5D9"],
            line=dict(color="#FFFFFF", width=3)
        ),
        textinfo="percent",
        textposition="inside",
        textfont=dict(color="#FFFFFF", size=12),
        sort=False
    )

    fig3.update_layout(
        template="plotly_white",
        height=370,
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(color="#514260", family="DM Sans"),
        margin=dict(l=15, r=15, t=20, b=35),
        legend=dict(
            orientation="h",
            y=-0.08,
            x=0.5,
            xanchor="center"
        )
    )

    st.plotly_chart(fig3, use_container_width=True)

st.divider()

st.markdown("### Category Analysis")
st.markdown(
    '<div class="section-note">Revenue contribution by product category</div>',
    unsafe_allow_html=True
)

category_sales = (
    filtered_df.groupby("Category")["Revenue"]
    .sum()
    .reset_index()
)

fig4 = px.bar(
    category_sales,
    x="Category",
    y="Revenue",
    text_auto=".2s"
)

fig4.update_traces(
    marker_color="#D99AA8",
    textposition="outside",
    textfont=dict(color="#514260")
)

fig4.update_layout(
    template="plotly_white",
    height=330,
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",
    font=dict(color="#514260", family="DM Sans"),
    margin=dict(l=25, r=25, t=20, b=25),
    xaxis_title="Category",
    yaxis_title="Revenue (₹)",
    showlegend=False
)

fig4.update_xaxes(showgrid=False)
fig4.update_yaxes(gridcolor="#F0EAF5")

st.plotly_chart(fig4, use_container_width=True)

st.divider()

st.markdown("### Key Observations")
st.markdown(
    '<div class="section-note">A few highlights from your selected sales data</div>',
    unsafe_allow_html=True
)

top_product = filtered_df.groupby("Product")["Revenue"].sum().idxmax()
top_region = filtered_df.groupby("Region")["Revenue"].sum().idxmax()
top_category = filtered_df.groupby("Category")["Revenue"].sum().idxmax()

i1, i2, i3 = st.columns(3)

with i1:
    st.markdown(
        f'<div class="insight-card"><b>✿ Leading Product</b><br>{top_product} generated the highest revenue.</div>',
        unsafe_allow_html=True
    )

with i2:
    st.markdown(
        f'<div class="insight-card"><b>✿ Leading Region</b><br>{top_region} contributed the highest revenue.</div>',
        unsafe_allow_html=True
    )

with i3:
    st.markdown(
        f'<div class="insight-card"><b>✿ Leading Category</b><br>{top_category} recorded the highest revenue.</div>',
        unsafe_allow_html=True
    )

st.divider()

with st.expander("View Detailed Sales Records"):
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

st.caption(
    "Note: This dashboard uses a sample dataset created for academic demonstration."
)

st.caption(
    "Sales Studio | Developed using Python, Pandas, Streamlit and Plotly"
)
