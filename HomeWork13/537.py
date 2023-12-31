students = [
    {"name": "Ronaldo", "points": [75, 65, 45, 85]},
    {"name": "Messi", "points": [45, 60, 30, 49]},
    {"name": "Bob", "points": [60, 55, 50, 60]}
]

min_points = min(student["points"] for student in students)

result = ' '.join(map(str, min_points))
print(result)