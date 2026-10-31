from pathlib import Path
import shutil

FOLDER = Path("Downloads_copy")   # a COPY of your Downloads
DRY_RUN = True                    # True = only print the plan

TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".csv"],
    "Archives": [".zip", ".gz"],
    "Media": [".mp3", ".wav", ".mp4", ".mov"],
}

for file in sorted(FOLDER.iterdir()):
    if not file.is_file():
        continue
    group = "Other"
    for name, extensions in TYPES.items():
        if file.suffix.lower() in extensions:
            group = name
    target = FOLDER / group / file.name
    if target.exists():
        print("skip, already there:", file.name)
    elif DRY_RUN:
        print("would move", file.name, "->", group)
    else:
        target.parent.mkdir(exist_ok=True)
        shutil.move(file, target)
        print("moved", file.name, "->", group)
