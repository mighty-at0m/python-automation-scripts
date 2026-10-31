from pathlib import Path
import hashlib

FOLDER = Path("Photos_copy")
groups = {}   # fingerprint -> list of files

for file in sorted(FOLDER.rglob("*")):
    if file.is_file():
        fingerprint = hashlib.sha256(file.read_bytes()).hexdigest()
        if fingerprint not in groups:
            groups[fingerprint] = []
        groups[fingerprint].append(file)

found = 0
for fingerprint, files in groups.items():
    if len(files) > 1:
        found += 1
        print(f"Duplicates #{found} ({fingerprint[:12]}):")
        for file in files:
            print("   ", file.relative_to(FOLDER))

print(found, "duplicate group(s). Nothing was deleted.")
