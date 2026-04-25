from pathlib import Path

MAIN = Path.home() / "Downloads"

DROPMAP_FOLDER = Path.home() / "Documents" / "Dropmap"

ROUTING_TABLE = {
    ".jpg": DROPMAP_FOLDER / "JPGS",
    ".png": DROPMAP_FOLDER / "PNGS",
    ".svg": DROPMAP_FOLDER / "SVGS",
    ".pdf": DROPMAP_FOLDER / "PDFS"
   
}