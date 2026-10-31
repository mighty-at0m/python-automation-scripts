from pathlib import Path

folder = Path("test_files")
prefix = "project_"

if not folder.is_dir():
    raise SystemExit("Create a test_files folder beside this script first.")

for file in folder.iterdir():
    if not file.is_file():
        continue

    if file.name.startswith(prefix):
        continue

    new_name = file.with_name(prefix + file.name)

    if new_name.exists():
        print(f"Skipped: {new_name.name} already exists")
        continue

    file.rename(new_name)
    print(f"{file.name} -> {new_name.name}")
