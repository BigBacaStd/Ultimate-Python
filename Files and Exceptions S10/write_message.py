#Python script

from pathlib import Path


contents = "Everyone loves Python.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programing.txt')
path.write_text(contents)