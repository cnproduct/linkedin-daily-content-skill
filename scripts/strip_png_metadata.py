"""Rebuild PNG from decoded pixels; verify chunks, CRC, and unchanged pixels.
Usage: python strip_png_metadata.py image1.png [image2.png ...]
       python strip_png_metadata.py --verify image1.png [image2.png ...]
Backups are stored outside the final image directory with unique names.
"""
import argparse
import hashlib
import os
from pathlib import Path
import struct
import tempfile
import uuid
import zlib
from PIL import Image

ALLOWED = {b"IHDR", b"IDAT", b"IEND"}
SIGNATURE = b"\x89PNG\r\n\x1a\n"

def chunks(path):
    data = Path(path).read_bytes()
    if not data.startswith(SIGNATURE):
        raise ValueError("Not a PNG: " + str(path))
    pos, found = 8, []
    while pos + 12 <= len(data):
        size = struct.unpack_from(">I", data, pos)[0]
        kind = data[pos+4:pos+8]
        end = pos + size + 12
        if end > len(data):
            raise ValueError("Truncated PNG chunk")
        payload = data[pos+8:pos+8+size]
        crc = struct.unpack_from(">I", data, pos+8+size)[0]
        if zlib.crc32(kind + payload) & 0xffffffff != crc:
            raise ValueError("Invalid PNG CRC")
        found.append(kind)
        pos = end
        if kind == b"IEND":
            break
    if not found or found[0] != b"IHDR" or found[-1] != b"IEND" or pos != len(data):
        raise ValueError("Invalid PNG framing")
    return found

def pixels(path):
    with Image.open(path) as source:
        source.load()
        mode = "RGBA" if "A" in source.getbands() or "transparency" in source.info else "RGB"
        converted = source.convert(mode)
        return mode, converted.size, converted.tobytes()

def verify(path, expected=None):
    found = chunks(path)
    if set(found) - ALLOWED:
        raise ValueError("Unexpected metadata chunks: " + repr(found))
    actual = pixels(path)
    if expected is not None and actual != expected:
        raise ValueError("Pixels, dimensions, or mode changed")
    return {"path": str(Path(path).resolve()), "size": actual[1],
            "chunks": sorted({x.decode("ascii") for x in found}),
            "pixel_sha256": hashlib.sha256(actual[2]).hexdigest()}

def clean(path):
    path = Path(path)
    if path.suffix.lower() != ".png":
        raise ValueError("Expected PNG")
    chunks(path)
    original = pixels(path)
    rebuilt = Image.frombytes(original[0], original[1], original[2])
    with tempfile.NamedTemporaryFile(dir=path.parent, suffix=".png", delete=False) as handle:
        temporary = Path(handle.name)
    try:
        rebuilt.save(temporary, format="PNG")
        verify(temporary, original)
        backup_dir = path.parent.parent / (path.parent.name + "_original_backups")
        backup_dir.mkdir(parents=True, exist_ok=True)
        backup = backup_dir / (path.stem + "_" + uuid.uuid4().hex[:8] + ".png")
        backup.write_bytes(path.read_bytes())
        os.replace(temporary, path)
        return verify(path, original)
    finally:
        if temporary.exists():
            temporary.unlink()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("images", nargs="+", type=Path)
    args = parser.parse_args()
    for image in args.images:
        print(verify(image) if args.verify else clean(image))

