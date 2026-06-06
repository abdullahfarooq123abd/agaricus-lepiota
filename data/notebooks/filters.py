import streamlit as st


def apply_filters(df):

    st.sidebar.header("Dashboard Filters")

    class_filter = st.sidebar.multiselect(
        "Class",
        options=df["class"].unique(),
        default=df["class"].unique()
    )

    habitat_filter = st.sidebar.multiselect(
        "Habitat",
        options=df["habitat"].unique(),
        default=df["habitat"].unique()
    )

    odor_filter = st.sidebar.multiselect(
        "Odor",
        options=df["odor"].unique(),
        default=df["odor"].unique()
    )

    search_text = st.sidebar.text_input(
        "Search"
    )

    filtered_df = df[
        (df["class"].isin(class_filter))
        &
        (df["habitat"].isin(habitat_filter))
        &
        (df["odor"].isin(odor_filter))
    ]

    if search_text:
        filtered_df = filtered_df[
            filtered_df.astype(str)
            .apply(
                lambda row:
                row.str.contains(
                    search_text,
                    case=False
                ).any(),
                axis=1
            )
        ]

    return filtered_df