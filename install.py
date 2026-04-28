import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
PYTHON = PROJECT_DIR / ".venv" / "bin" / "python3"
LAUNCH_AGENTS = Path.home() / "Library" / "LaunchAgents"
PLIST_NAME = "com.dropmap.plist"
PLIST_DEST = LAUNCH_AGENTS / PLIST_NAME

PLIST = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.dropmap</string>

    <key>ProgramArguments</key>
    <array>
        <string>{PYTHON}</string>
        <string>{PROJECT_DIR / "watcher.py"}</string>
    </array>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>StandardOutPath</key>
    <string>{PROJECT_DIR / "dropmap.log"}</string>

    <key>StandardErrorPath</key>
    <string>{PROJECT_DIR / "dropmap.err"}</string>

    <key>WorkingDirectory</key>
    <string>{PROJECT_DIR}</string>
</dict>
</plist>"""

def install():
    if not PYTHON.exists():
        print("Virtual environment not found. Run: python3 -m venv .venv && .venv/bin/pip install watchdog")
        return

    LAUNCH_AGENTS.mkdir(parents=True, exist_ok=True)
    PLIST_DEST.write_text(PLIST)
    print(f"Wrote plist to {PLIST_DEST}")

    subprocess.run(["launchctl", "unload", str(PLIST_DEST)], capture_output=True)
    subprocess.run(["launchctl", "load", str(PLIST_DEST)], check=True)
    print("Dropmap is running and will start automatically on login.")

def uninstall():
    if PLIST_DEST.exists():
        subprocess.run(["launchctl", "unload", str(PLIST_DEST)], capture_output=True)
        PLIST_DEST.unlink()
        print("Dropmap removed from startup.")
    else:
        print("Dropmap is not installed.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "uninstall":
        uninstall()
    else:
        install()
