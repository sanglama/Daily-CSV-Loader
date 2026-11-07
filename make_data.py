import csv, random
from datetime import date, timedelta

random.seed(1)
names = ["Anna", "Ben", "Clara", "David", "Eva", "Felix"]

def make_rows(day, n=10):
    rows = [{"id": i, "name": random.choice(names),
             "amount": round(random.uniform(10, 500), 2),
             "updated_at": day.isoformat()} for i in range(1, n + 1)]
    rows += random.sample(rows, 2)   # 2 duplicate rows
    return rows

start = date(2026, 11, 1)
for d in range(5):
    day = start + timedelta(days=d)
    rows = [] if d == 3 else make_rows(day)   # day 4 = empty file
    with open(f"orders_{day}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "name", "amount", "updated_at"])
        w.writeheader()
        w.writerows(rows)

        