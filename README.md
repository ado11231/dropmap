# dropmap

Watches your Downloads folder and automatically sorts files into organized subfolders based on their extension.

## How it works

1. A watcher monitors `~/Downloads` for new files
2. When a file appears, it waits for the download to finish (checks that the file size has stopped changing)
3. The file is moved to `~/Documents/Dropmap/<Category>/<Type>/` based on its extension

**Example:**
```
~/Downloads/photo.png  →  ~/Documents/Dropmap/Images/PNGs/photo.png
~/Downloads/report.pdf →  ~/Documents/Dropmap/Documents/PDFs/report.pdf
~/Downloads/song.mp3   →  ~/Documents/Dropmap/Audio/MP3s/song.mp3
```

If a file with the same name already exists in the destination, dropmap renames it (`file_1.png`, `file_2.png`, etc.) instead of overwriting.

## Setup

**1. Clone the repo and create a virtual environment:**

> Requires Python 3.9–3.13. Python 3.14+ can break `venv` on macOS. If `python3 -m venv` fails, install a stable version with pyenv:
> ```bash
> brew install pyenv && pyenv install 3.12.7 && pyenv local 3.12.7
> ```

```bash
git clone https://github.com/ado11231/dropmap.git
cd dropmap
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

**2. Install and run on startup (macOS only):**
```bash
python3 install.py
```

That's it. Dropmap will start immediately and relaunch automatically every time you log in.

## Run manually (without startup install)

```bash
.venv/bin/python3 watcher.py
```

## Uninstall

```bash
python3 install.py uninstall
```

## Supported extensions

| Category      | Extensions                          |
|---------------|-------------------------------------|
| Images        | jpg, jpeg, png, gif, webp, heic, svg |
| Documents     | pdf, doc, docx, txt, md             |
| Spreadsheets  | xls, xlsx, csv                      |
| Presentations | ppt, pptx                           |
| Audio         | mp3, wav, flac, m4a                 |
| Video         | mp4, mov, mkv                       |
| Archives      | zip, tar, gz, rar                   |
| Code          | py, js, ts, html, css, json         |

To add or change a destination, edit `config.py`.
