# 5 Python Automation Scripts That Save Hours

Beginner-friendly scripts from the Mighty Atom video **"5 Python Automation Scripts That Save Hours (Beginner Friendly)"**.

| Script | What it does |
|---|---|
| `1_rename_files.py` | Adds a prefix to every file in `test_files` (skips already-prefixed names and collisions) |
| `2_sort_downloads.py` | Sorts a Downloads folder into Images / Documents / Archives / Media / Other (`DRY_RUN = True` first) |
| `3_find_duplicates.py` | Finds duplicate files by SHA-256 hash. Reports only, never deletes |
| `4_resize_images.py` | Shrinks JPG/PNG photos to max 1280 px into `resized/`. Originals untouched |
| `5_merge_pdfs.py` | Merges every PDF in `invoices/` into `merged.pdf` |

## Setup
```bash
python3 --version        # Python 3.8+ (use "python" on Windows)
pip install -r requirements.txt
```

## Run
Put the script next to the folder it works on, edit the folder name at the top, then:
```bash
python3 1_rename_files.py
```

**Always test on a COPY of your files first.**

Subscribe for daily Python Shorts: [Mighty Atom on YouTube](https://www.youtube.com/@dmightyatom)

MIT License
