import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# =========================
# GLOBAL STYLE
# =========================

sns.set_style("whitegrid")

sns.set_palette([
    "#22c55e",
    "#84cc16",
    "#06b6d4",
    "#f59e0b",
    "#8b5cf6"
])


def setup_chart(ax, title):
    ax.set_title(
        title,
        fontsize=16,
        fontweight="bold",
        color="#14532d"
    )

    ax.grid(alpha=0.25)

    return ax


# =========================
# HISTOGRAM
# =========================

def plot_histogram(df):
    fig, ax = plt.subplots(figsize=(4, 4))

    col = df.columns[1]

    df[col].value_counts().plot(
        kind="bar",
        color="#22c55e",
        edgecolor="black",
        ax=ax
    )

    setup_chart(ax, "Histogram")

    plt.tight_layout()

    return fig


# =========================
# CLASS DISTRIBUTION
# =========================

def plot_class_distribution(df):
    fig, ax = plt.subplots(figsize=(6, 6))

    target = df.columns[0]

    colors = [
        "#22c55e",
        "#84cc16",
        "#06b6d4",
        "#f59e0b"
    ]

    df[target].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        colors=colors,
        wedgeprops={"edgecolor": "white"},
        ax=ax
    )

    ax.set_ylabel("")

    ax.set_title(
        "Class Distribution",
        fontsize=16,
        fontweight="bold",
        color="#14532d"
    )

    plt.tight_layout()

    return fig


# =========================
# BAR CHART
# =========================

def plot_bar_chart(df):
    fig, ax = plt.subplots(figsize=(8, 4))

    col = df.columns[1]

    df[col].value_counts().head(10).plot(
        kind="bar",
        color="#84cc16",
        edgecolor="black",
        ax=ax
    )

    setup_chart(ax, "Bar Chart")

    plt.tight_layout()

    return fig


# =========================
# LINE CHART
# =========================

def plot_line_chart(df):
    fig, ax = plt.subplots(figsize=(10, 5))

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        ax.text(
            0.5,
            0.5,
            "No numeric columns available",
            ha="center",
            va="center"
        )
        ax.axis("off")
        return fig

    col = numeric_cols[0]

    sample = df[col].head(100)

    ax.plot(
        sample.index,
        sample.values,
        linewidth=3,
        color="#06b6d4"
    )

    ax.fill_between(
        sample.index,
        sample.values,
        color="#06b6d4",
        alpha=0.25
    )

    ax.set_title(
        f"{col} Trend",
        fontsize=16,
        fontweight="bold",
        color="#14532d"
    )

    ax.set_xlabel("Index")
    ax.set_ylabel(col)

    plt.tight_layout()

    return fig


# =========================
# SCATTER PLOT
# =========================

def plot_scatter_plot(df):
    fig, ax = plt.subplots(figsize=(8, 5))

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) < 2:
        ax.text(
            0.5,
            0.5,
            "Need at least 2 numeric columns",
            ha="center",
            va="center"
        )
        ax.axis("off")
        return fig

    ax.scatter(
        df[numeric_cols[0]],
        df[numeric_cols[1]],
        color="#f59e0b",
        alpha=0.7,
        s=60
    )

    setup_chart(ax, "Scatter Plot")

    plt.tight_layout()

    return fig


# =========================
# BOX PLOT
# =========================

def plot_box_plot(df):
    fig, ax = plt.subplots(figsize=(10, 5))

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        ax.text(
            0.5,
            0.5,
            "No numeric columns available",
            ha="center",
            va="center"
        )
        ax.axis("off")
        return fig

    sns.boxplot(
        data=numeric_df,
        palette="crest",
        ax=ax
    )

    setup_chart(ax, "Box Plot")

    plt.xticks(rotation=45)

    plt.tight_layout()

    return fig


# =========================
# HEATMAP
# =========================

def plot_heatmap(df):
    fig, ax = plt.subplots(figsize=(14, 10))

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        ax.text(
            0.5,
            0.5,
            "No numeric data available",
            ha="center",
            va="center"
        )
        ax.axis("off")
        return fig

    corr = numeric_df.corr()

    if corr.empty or corr.shape[0] < 2:
        ax.text(
            0.5,
            0.5,
            "Not enough numeric columns",
            ha="center",
            va="center"
        )
        ax.axis("off")
        return fig

    sns.heatmap(
        corr,
        cmap="RdYlGn",
        annot=False,
        square=True,
        linewidths=0.5,
        linecolor="white",
        cbar_kws={"shrink": 0.8},
        ax=ax
    )

    ax.set_title(
        "Correlation Heatmap",
        fontsize=18,
        fontweight="bold",
        color="#14532d"
    )

    plt.xticks(
        rotation=45,
        ha="right",
        fontsize=9
    )

    plt.yticks(
        fontsize=9
    )

    plt.tight_layout()

    return fig


# =========================
# AREA CHART
# =========================

def plot_area_chart(df):
    fig, ax = plt.subplots(figsize=(10, 5))

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        ax.text(
            0.5,
            0.5,
            "No numeric columns available",
            ha="center",
            va="center"
        )
        ax.axis("off")
        return fig

    numeric_df.head(30).plot.area(
        ax=ax,
        alpha=0.7
    )

    ax.legend(
        loc="upper left",
        bbox_to_anchor=(1.02, 1)
    )

    ax.set_title(
        "Area Chart",
        fontsize=16,
        fontweight="bold",
        color="#14532d"
    )

    plt.tight_layout()

    return fig


# =========================
# COUNT PLOT
# =========================

def plot_count_plot(df):
    fig, ax = plt.subplots(figsize=(8, 4))

    col = df.columns[1]

    sns.countplot(
        x=df[col],
        hue=df[col],
        legend=False,
        palette="crest",
        ax=ax
    )

    plt.xticks(rotation=45)

    setup_chart(ax, "Count Plot")

    plt.tight_layout()

    return fig


# =========================
# VIOLIN PLOT
# =========================

def plot_violin_plot(df):
    fig, ax = plt.subplots(figsize=(8, 4))

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        ax.text(
            0.5,
            0.5,
            "No numeric columns available",
            ha="center",
            va="center"
        )
        ax.axis("off")
        return fig

    sns.violinplot(
        y=df[numeric_cols[0]],
        color="#a3e635",
        ax=ax
    )

    setup_chart(ax, "Violin Plot")

    plt.tight_layout()

    return fig