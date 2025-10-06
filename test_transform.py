import pandas as pd

def test_total_column_exists():
    df = pd.read_csv("transformed.csv")
    assert "Total" in df.columns, "❌ 'Total' column missing in transformed data"

def test_row_count():
    df_source = pd.read_csv("source.csv")
    df_transformed = pd.read_csv("transformed.csv")
    assert len(df_source) == len(df_transformed), "❌ Row count mismatch after transform"
