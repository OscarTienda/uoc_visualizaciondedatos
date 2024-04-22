import plotly.graph_objects as go
import pandas as pd
import numpy as np

df = pd.read_csv("student-scores.csv")


sample_students = df.sample(n=3)

categories = [
    "math_score",
    "history_score",
    "physics_score",
    "chemistry_score",
    "biology_score",
    "english_score",
    "geography_score",
]

fig = go.Figure()

for index, student in sample_students.iterrows():
    student_scores = [student[category] for category in categories]
    fig.add_trace(
        go.Scatterpolar(
            r=student_scores,
            theta=categories,
            fill="toself",
            name=f"{student['first_name']} {student['last_name']}",
        )
    )

fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
    title="Radar Chart of Student Performance",
    showlegend=True,
)

fig.show()
