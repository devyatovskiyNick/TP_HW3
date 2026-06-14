import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["КУРС", "ГРУППА", "ПОСЕЩАЕМОСТЬ", "ОЦЕНКА_ЗА_ЭКЗАМЕН"]

def generate_row():

    return {
        "КУРС": random.randint(1, 5),
        "ГРУППА": random.choice(["ББИ", "БУЦП", "БТАДБ", "БУЦ"]) + str(random.randint(1, 10)),
        "ПОСЕЩАЕМОСТЬ": random.randint(0, 10),
        "ОЦЕНКА_ЗА_ЭКЗАМЕН": round(random.uniform(0, 10),1)
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)

