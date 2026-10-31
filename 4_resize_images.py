from pathlib import Path
from PIL import Image

SOURCE = Path("photos")
OUTPUT = Path("resized")     # originals are never changed
MAX_SIZE = (1280, 1280)      # longest side becomes 1280 px

OUTPUT.mkdir(exist_ok=True)
for file in sorted(SOURCE.iterdir()):
    if file.suffix.lower() not in (".jpg", ".jpeg", ".png"):
        continue
    with Image.open(file) as img:
        old_size = img.size
        img.thumbnail(MAX_SIZE)      # shrinks, keeps the shape
        img.save(OUTPUT / file.name)
    print(f"{file.name}: {old_size} -> {img.size}")

print("Done! Resized images are in", OUTPUT)
