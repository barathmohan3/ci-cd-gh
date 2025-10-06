import pandas as pd

# Simulated source data
data = {
    "Item": ["Apple", "Banana", "Orange"],
    "Qty": [10, 5, 7],
    "Price": [2, 1, 3]
}

# Save raw data
df = pd.DataFrame(data)
df.to_csv("source.csv", index=False)
print("✅ Extract step completed. Source data written to source.csv")
