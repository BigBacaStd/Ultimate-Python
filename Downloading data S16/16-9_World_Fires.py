from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('EQ_Data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

print(header_row)