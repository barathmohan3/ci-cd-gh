import pandas as pd

# Read extracted data
df = pd.read_csv("source.csv")

# Add a new calculated column
df["Total"] = df["Qty"] * df["Price"]

# Save transformed data
df.to_csv("transformed.csv", index=False)
print("✅ Transform step completed. Added 'Total' column.")
