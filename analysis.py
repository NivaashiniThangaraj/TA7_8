import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("mrr_quarterly_2024.csv")

# Compute average MRR growth
avg = round(df["MRR_Growth"].mean(), 2)
print("Average MRR Growth (2024):", avg)  # should be 8.68

# Plot trend vs benchmark
plt.figure(figsize=(10, 6))
plt.plot(df["Quarter"], df["MRR_Growth"], marker="o", linewidth=2)
plt.axhline(y=15, linestyle="--", linewidth=1)
plt.title("2024 Quarterly MRR Growth vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth (%)")

for x, y in zip(df["Quarter"], df["MRR_Growth"]):
    plt.text(x, y + 0.3, f"{y:.2f}%", ha="center", va="bottom")
plt.text(3.6, 15.3, "Industry Target: 15%", ha="right", va="bottom")

plt.tight_layout()
plt.savefig("mrr_trend.png", dpi=160)
print("Saved figure to mrr_trend.png")