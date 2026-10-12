import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(page_title="DuckDB ELT Pipeline", page_icon="📊", layout="wide")

st.title("DuckDB GitHub Repository Analytics")
st.markdown("""
**Data Engineering Pipeline Overview:**
This dashboard visualizes commit history extracted directly from the official **duckdb/duckdb** GitHub repository.
* **Extraction (Bronze):** Raw JSON pulled from the GitHub REST API and loaded via `dlt`.
* **Transformation (Silver & Gold):** Flattened, cleaned, and aggregated using `dbt`.
* **Storage:** Queried live from a local DuckDB analytical data warehouse.
""")

st.divider()

@st.cache_data
def load_data():
    con = duckdb.connect(r'C:\Users\acer\github_elt\github_pipeline.duckdb')
    df = con.sql("SELECT * FROM gold_daily_metrics ORDER BY total_commits DESC").df()

    if not df.empty:
        df['commit_date'] = pd.to_datetime(df['commit_date']).dt.strftime('%Y-%m-%d')
    return df

df = load_data()

if not df.empty:
    total_commits = df['total_commits'].sum()
    unique_authors = df['author_name'].nunique()
    latest_date = df['commit_date'].max()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Commits Analyzed", int(total_commits))
    col2.metric("Unique Contributors", int(unique_authors))
    col3.metric("Latest Activity Date", str(latest_date))

    st.divider()

    col_chart, col_table = st.columns([2, 1])

    with col_chart:
        st.subheader("Top Contributors")
        st.bar_chart(
            data=df,
            x='author_name',
            y='total_commits',
            use_container_width=True
        )

    with col_table:
        st.subheader("Gold Layer Data")
        st.dataframe(
            df,
            column_config={
                "commit_date": "Date",
                "author_name": "Author",
                "total_commits": "Commits"
            },
            hide_index=True,
            use_container_width=True
        )
else:
    st.warning("No data found in the Gold table.")