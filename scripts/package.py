"""Build deterministic, standalone plugin archives from public source files."""
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist"
OUTPUT.mkdir(exist_ok=True)
checksums = []
for plugin_id in ("anti_delete", "auto_reply", "notification_throttle", "quoter", "quick_stickers", "bugfix", "quality_of_life"):
    directory = ROOT / "plugins" / plugin_id
    manifest = json.loads((directory / "plugin.json").read_text(encoding="utf-8"))
    if manifest["id"] != plugin_id or manifest["api_version"] not in (1, 2, 3):
        raise ValueError(f"Unexpected manifest: {plugin_id}")
    destination = OUTPUT / f"{plugin_id}.zip"
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for filename in ("plugin.json", "main.rhai"):
            info = zipfile.ZipInfo(f"{plugin_id}/{filename}", (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (directory / filename).read_bytes())
    # Read back exact membership and bytes before publishing.
    with zipfile.ZipFile(destination) as archive:
        expected = [f"{plugin_id}/{name}" for name in ("plugin.json", "main.rhai")]
        if archive.namelist() != expected or archive.testzip() is not None:
            raise ValueError(f"Invalid archive: {plugin_id}")
        for filename in ("plugin.json", "main.rhai"):
            if archive.read(f"{plugin_id}/{filename}") != (directory / filename).read_bytes():
                raise ValueError(f"Archive contents differ: {plugin_id}")
    checksums.append(f"{hashlib.sha256(destination.read_bytes()).hexdigest()}  {destination.name}")
    print(destination.name)
(OUTPUT / "SHA256SUMS").write_text("\n".join(checksums) + "\n", encoding="utf-8")
