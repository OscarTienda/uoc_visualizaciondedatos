import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("orders.csv")

df["created_at"] = pd.to_datetime(df["created_at"])
df["hour"] = df["created_at"].dt.hour

hour_counts = df["hour"].value_counts().sort_index()
all_hours = pd.Series(index=np.arange(24), data=0)  
hour_counts = hour_counts.reindex(all_hours.index, fill_value=0) 

values = (hour_counts / hour_counts.max()).tolist()
values += values[:1]

n_points = len(hour_counts)
inner_radius = 0.2

angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Draw bars
bars = ax.bar(
    angles,
    values,
    width=2 * np.pi / n_points,
    bottom=inner_radius,
    color="red",
    edgecolor="white",
    linewidth=2,
)

ax.set_xticks([])
ax.set_yticks([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels([f"{h}:00" for h in range(24)], color="black", size=12)

for bar, height in zip(bars, hour_counts):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + inner_radius,
        str(int(height)),
        ha="center",
        va="bottom",
    )

plt.title("Número de pedidos por hora en una cafetería", va="bottom")

plt.show()
