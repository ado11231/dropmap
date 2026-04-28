from pathlib import Path

WATCHING_FOLDER = Path.home() / "Downloads"

DROPMAP_FOLDER = Path.home() / "Documents" / "Dropmap"

ROUTING_TABLE = {
    # Images
    ".jpg":  DROPMAP_FOLDER / "Images" / "JPGs",
    ".jpeg": DROPMAP_FOLDER / "Images" / "JPGs",
    ".png":  DROPMAP_FOLDER / "Images" / "PNGs",
    ".gif":  DROPMAP_FOLDER / "Images" / "GIFs",
    ".webp": DROPMAP_FOLDER / "Images" / "WEBPs",
    ".heic": DROPMAP_FOLDER / "Images" / "HEICs",
    ".svg":  DROPMAP_FOLDER / "Images" / "SVGs",
    # Documents
    ".pdf":  DROPMAP_FOLDER / "Documents" / "PDFs",
    ".doc":  DROPMAP_FOLDER / "Documents" / "Word",
    ".docx": DROPMAP_FOLDER / "Documents" / "Word",
    ".txt":  DROPMAP_FOLDER / "Documents" / "Text",
    ".md":   DROPMAP_FOLDER / "Documents" / "Markdown",
    # Spreadsheets
    ".xls":  DROPMAP_FOLDER / "Spreadsheets" / "Excel",
    ".xlsx": DROPMAP_FOLDER / "Spreadsheets" / "Excel",
    ".csv":  DROPMAP_FOLDER / "Spreadsheets" / "CSV",
    # Presentations
    ".ppt":  DROPMAP_FOLDER / "Presentations" / "PowerPoint",
    ".pptx": DROPMAP_FOLDER / "Presentations" / "PowerPoint",
    # Audio
    ".mp3":  DROPMAP_FOLDER / "Audio" / "MP3s",
    ".wav":  DROPMAP_FOLDER / "Audio" / "WAVs",
    ".flac": DROPMAP_FOLDER / "Audio" / "FLAC",
    ".m4a":  DROPMAP_FOLDER / "Audio" / "M4As",
    # Video
    ".mp4":  DROPMAP_FOLDER / "Video" / "MP4s",
    ".mov":  DROPMAP_FOLDER / "Video" / "MOVs",
    ".mkv":  DROPMAP_FOLDER / "Video" / "MKVs",
    # Archives
    ".zip":  DROPMAP_FOLDER / "Archives" / "ZIP",
    ".tar":  DROPMAP_FOLDER / "Archives" / "TAR",
    ".gz":   DROPMAP_FOLDER / "Archives" / "GZ",
    ".rar":  DROPMAP_FOLDER / "Archives" / "RAR",
    # Code
    ".py":   DROPMAP_FOLDER / "Code" / "Python",
    ".js":   DROPMAP_FOLDER / "Code" / "JavaScript",
    ".ts":   DROPMAP_FOLDER / "Code" / "TypeScript",
    ".html": DROPMAP_FOLDER / "Code" / "HTML",
    ".css":  DROPMAP_FOLDER / "Code" / "CSS",
    ".json": DROPMAP_FOLDER / "Code" / "JSON",
}