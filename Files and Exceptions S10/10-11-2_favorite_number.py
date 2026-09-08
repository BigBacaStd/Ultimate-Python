from pathlib import Path
import json

path = Path('favorite_number.json')
contents = path.read_text()
favorite = json.loads(contents)

print(f"Your favorite number is: {favorite}")