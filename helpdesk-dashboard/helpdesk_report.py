import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("tickets.csv")

# convert dates
df["CreatedDate"] = pd.to_datetime(df["CreatedDate"])
df["ResolvedDate"] = pd.to_datetime(df["ResolvedDate"])


# -----------------------
# BASIC METRICS
# -----------------------


total_tickets = len(df)
open_tickets = len(df[df["Status"] == "Open"])
closed_tickets = len(df[df["Status"] == "Closed"])

print("\n=== HELP DESK REPORT ===")
print(f"Total Tickets: {total_tickets}")
print(f"Open Tickets: {open_tickets}")
print(f"Closed Tickets: {closed_tickets}")


# -----------------------
# RESOLUTION TIME
# -----------------------


closed_df = df[df["Status"] == "Closed"].copy()

closed_df["ResolutionDays"] = (closed_df["ResolvedDate"] - closed_df["CreatedDate"]).dt.days

avg_resolution = closed_df["ResolutionDays"].mean()

print(f"\nAverage Resolution Time: {avg_resolution:.1f} days")


# -----------------------
# SLA TRACKING
# SLA = resolved within 2 days
# -----------------------


sla_target = 2

sla_met = len(closed_df[closed_df["ResolutionDays"] <= sla_target])

sla_total = len(closed_df)

if sla_total > 0:
    sla_percent = (sla_met / sla_total) * 100
else:
    sla_percent = 0

print(f"SLA Compliance: {sla_percent:.1f}%")


# -----------------------
# OVERDUE OPEN TICKETS
# -----------------------


today = pd.Timestamp.today()

open_df = df[df["Status"] == "Open"].copy()

open_df["DaysOpen"] = (today - open_df["CreatedDate"]).dt.days

overdue = open_df[open_df["DaysOpen"] > sla_target]

print(f"Overdue Open Tickets: {len(overdue)}")


# -----------------------
# CATEGORY ANALYSIS
# -----------------------


issue_counts = df["Category"].value_counts()

print("\nMost Common Issue Categories:")
print(issue_counts)


# -----------------------
# PIE CHART
# -----------------------


status_counts = df["Status"].value_counts()

plt.figure()
plt.pie(status_counts, labels = status_counts.index, autopct = "%1.1f%%")
plt.title("Ticket Status Breakdown")
plt.savefig("ticket_status_pie.png")


# -----------------------
# CATEGORY BAR CHART
# -----------------------


plt.figure()
issue_counts.plot(kind = "bar")
plt.title("Tickets by Category")
plt.xlabel("Category")
plt.ylabel("Number of Tickets")
plt.tight_layout()
plt.savefig("ticket_categories_bar.png")

print("\nCharts saved:")
print("- ticket_status_pie.png")
print("- ticket_categories_bar.png")
