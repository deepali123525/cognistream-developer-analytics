
import pandas as pd
import polars as pl
# Load developer activity data
df = pd.read_csv("developer_activity.csv")

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Separate coding and interruption events
coding = df[df["event_type"] == "Coding"]
interruptions = df[df["event_type"] == "Interruption"]

# Calculate developer-wise metrics
summary = df.groupby("developer").agg(
    total_events=("event_type", "count")
).reset_index()

coding_summary = coding.groupby("developer")["duration_minutes"].sum()
interruption_summary = interruptions.groupby("developer")["duration_minutes"].count()

summary["coding_minutes"] = summary["developer"].map(coding_summary).fillna(0)
summary["interruptions"] = summary["developer"].map(interruption_summary).fillna(0)

summary["focus_hours"] = (summary["coding_minutes"] / 60).round(2)

# Save results 

# Polars data processing
polars_data = pl.read_csv("developer_activity.csv")

polars_summary = polars_data.group_by("developer").agg([
    (pl.col("event_type") == "Coding").sum().alias("coding_sessions"),
    pl.when(pl.col("event_type") == "Coding")
      .then(pl.col("duration_minutes"))
      .otherwise(0).sum().alias("coding_minutes"),
    (pl.col("event_type") == "Interruption").sum().alias("interruptions")
])

print("\nPolars Analysis:")
print(polars_summary)

summary.to_csv("developer_summary.csv", index=False)

print("Developer flow analysis completed!")
print(summary)
print("File created: developer_summary.csv")
