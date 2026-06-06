import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

from charts import (
    plot_histogram,
    plot_class_distribution,
    plot_bar_chart,
    plot_line_chart,
    plot_scatter_plot,
    plot_box_plot,
    plot_heatmap,
    plot_area_chart,
    plot_count_plot,
    plot_violin_plot
)

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="🍄 Mushroom EDA Dashboard",
    page_icon="🍄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #14532d
    );
}

/* Dashboard Title */
.main-title{
    text-align:center;
    font-size:48px;
    font-weight:800;
    color:#98FB98;

    text-shadow:
        0 0 5px rgba(152,251,152,0.5),
        0 0 10px rgba(152,251,152,0.3);

    margin-bottom:15px;
}

/* Section Title */
.section-title{
    color:#d9f99d;
    font-size:28px;
    font-weight:bold;
}

/* KPI Cards */
.metric-card{
    background:rgba(255,255,255,0.08);
    border-radius:20px;
    padding:20px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.15);
    box-shadow:0px 0px 15px rgba(34,197,94,0.4);
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:linear-gradient(
        180deg,
        #052e16,
        #14532d,
        #166534
    );
}

/* Sidebar Text */
.sidebar-logo{
    text-align:center;
    font-size:60px;
}

.sidebar-title{
    text-align:center;
    color:white;
    font-size:24px;
    font-weight:bold;
}

.sidebar-sub{
    text-align:center;
    color:#d1fae5;
}

/* Headings */
h1,h2,h3{
    color:white !important;
}

label{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# TITLE
# ==================================================

st.markdown(
    """
    <div class="main-title">
        🍄 Mushroom EDA Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

# ==================================================
# LOAD DATA
# ==================================================

@st.cache_data
def load_data():
    return pd.read_excel(
       df = pd.read_excel("data/agaricus-lepiota.xlsx")
    )

df = load_data()

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-logo">
        🍄
    </div>

    <div class="sidebar-title">
        Mushroom Analytics
    </div>

    <div class="sidebar-sub">
        Exploratory Data Analysis
    </div>

    <hr>
    """, unsafe_allow_html=True)

    st.header("🔍 Filters")

    target_col = df.columns[0]

    selected_classes = st.multiselect(
        "Select Class",
        options=df[target_col].unique(),
        default=df[target_col].unique()
    )

# ==================================================
# FILTER DATA
# ==================================================

filtered_df = df[
    df[target_col].isin(selected_classes)
]

# ==================================================
# ENCODE DATA
# ==================================================

encoded_df = filtered_df.copy()

for col in encoded_df.columns:
    le = LabelEncoder()
    encoded_df[col] = le.fit_transform(
        encoded_df[col].astype(str)
    )

# ==================================================
# KPI CARDS
# ==================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>📄 Rows</h3>
        <h1>{filtered_df.shape[0]}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h3>📊 Columns</h3>
        <h1>{filtered_df.shape[1]}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <h3>🍄 Classes</h3>
        <h1>{filtered_df[target_col].nunique()}</h1>
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# TOP CHARTS
# ==================================================

st.markdown("---")

left, right = st.columns(2)

with left:
    st.subheader("📊 Histogram")
    st.pyplot(plot_histogram(filtered_df))

with right:
    st.subheader("🥧 Class Distribution")
    st.pyplot(plot_class_distribution(filtered_df))

# ==================================================
# GRAPH SELECTOR
# ==================================================

with st.sidebar:

    st.header("📈 Graph Selection")

    graph_options = [
        "All",
        "Bar Chart",
        "Line Chart",
        "Scatter Plot",
        "Box Plot",
        "Heatmap",
        "Area Chart",
        "Count Plot",
        "Violin Plot"
    ]

    selected_graphs = st.multiselect(
        "Choose Graphs",
        graph_options,
        default=["All"]
    )

show_all = "All" in selected_graphs

# ==================================================
# VISUAL ANALYTICS
# ==================================================

st.markdown("---")
st.markdown(
    '<div class="section-title">📈 Visual Analytics</div>',
    unsafe_allow_html=True
)

if show_all or "Bar Chart" in selected_graphs:
    st.subheader("Bar Chart")
    st.pyplot(plot_bar_chart(filtered_df))

if show_all or "Line Chart" in selected_graphs:
    st.subheader("Line Chart")
    st.pyplot(plot_line_chart(encoded_df))

if show_all or "Scatter Plot" in selected_graphs:
    st.subheader("Scatter Plot")
    st.pyplot(plot_scatter_plot(encoded_df))

if show_all or "Box Plot" in selected_graphs:
    st.subheader("Box Plot")
    st.pyplot(plot_box_plot(encoded_df))

if show_all or "Heatmap" in selected_graphs:
    st.subheader("Heatmap")
    st.pyplot(plot_heatmap(encoded_df))

if show_all or "Area Chart" in selected_graphs:
    st.subheader("Area Chart")
    st.pyplot(plot_area_chart(encoded_df))

if show_all or "Count Plot" in selected_graphs:
    st.subheader("Count Plot")
    st.pyplot(plot_count_plot(filtered_df))

if show_all or "Violin Plot" in selected_graphs:
    st.subheader("Violin Plot")
    st.pyplot(plot_violin_plot(encoded_df))

# ==================================================
# DATA PREVIEW
# ==================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">📋 Dataset Preview</div>',
    unsafe_allow_html=True
)

st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)