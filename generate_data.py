
import csv
import random
from datetime import datetime, timedelta

random.seed(42)

developers = ["Developer A", "Developer B", "Developer C"]
events = []

start_date = datetime(2026, 11, 1, 9, 0)

for day in range(5):
    for developer in developers:
        current_time = start_date + timedelta(days=day)

        for session in range(4):
            # IDE coding activity
            coding_time = random.randint(30, 120)

            events.append({
                "timestamp": current_time,
                "developer": developer,
                "source": "VSCode",
                "event_type": "Coding",
                "duration_minutes": coding_time,
                "description": "Coding session"
            })

            current_time += timedelta(minutes=coding_time)

            # Slack interruption
            if random.random() < 0.6:
                events.append({
                    "timestamp": current_time,
                    "developer": developer,
                    "source": "Slack",
                    "event_type": "Interruption",
                    "duration_minutes": 5,
                    "description": "Slack notification"
                })

                current_time += timedelta(minutes=5)

            # GitHub activity
            if random.random() < 0.5:
                events.append({
                    "timestamp": current_time,
                    "developer": developer,
                    "source": "GitHub",
                    "event_type": "Commit",
                    "duration_minutes": 2,
                    "description": "Code commit"
                })

                current_time += timedelta(minutes=2)

# Sort events by timestamp
events.sort(key=lambda x: x["timestamp"])

# Save data to CSV
with open("developer_activity.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=events[0].keys())
    writer.writeheader()

    for event in events:
        event["timestamp"] = event["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow(event)

print("Developer activity data generated successfully!")
print("Total events:", len(events))
print("File created: developer_activity.csv")
