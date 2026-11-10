
import pandas as pd

# Load activity data
df = pd.read_csv("developer_activity.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

results = []

for developer, group in df.groupby("developer"):
    group = group.sort_values("timestamp")
    current_flow = 0
    flow_blocks = 0
    total_flow_minutes = 0

    for _, row in group.iterrows():
        if row["event_type"] == "Coding":
            current_flow += row["duration_minutes"]

        elif row["event_type"] == "Interruption":
            if current_flow >= 90:
                flow_blocks += 1
                total_flow_minutes += current_flow
            current_flow = 0

    # Check the final coding block
    if current_flow >= 90:
        flow_blocks += 1
        total_flow_minutes += current_flow

    results.append({
        "developer": developer,
        "flow_blocks_90_plus": flow_blocks,
        "flow_minutes": total_flow_minutes
    })

flow_df = pd.DataFrame(results)
flow_df.to_csv("flow_metrics.csv", index=False)

print("Flow metrics calculated successfully!")
print(flow_df)
