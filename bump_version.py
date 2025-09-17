"""
Windows/cmd friendly: Auto-sync bump versions in pyproject.toml and src/access_guard/__init__.py.
Usage: python bump_version.py 0.1.4
"""
import sys
import re
from pathlib import Path

def bump_pyproject(path, new_version):
    text = Path(path).read_text(encoding="utf-8")
    text2 = re.sub(r'(?m)^(version\s*=\s*")[^"]+(\")', lambda m: f'{m.group(1)}{new_version}{m.group(2)}', text)
    Path(path).write_text(text2, encoding="utf-8")
    print(f"pyproject.toml -> {new_version}")

def bump_init(path, new_version):
    text = Path(path).read_text(encoding="utf-8")
    text2 = re.sub(r'(?m)^(__version__\s*=\s*")[^"]+(\")', lambda m: f'{m.group(1)}{new_version}{m.group(2)}', text)
    Path(path).write_text(text2, encoding="utf-8")
    print(f"__init__.py -> {new_version}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python bump_version.py <NEW_VERSION>")
        sys.exit(1)
    new_version = sys.argv[1]
    bump_pyproject("pyproject.toml", new_version)
    bump_init("src/access_guard/__init__.py", new_version)

if __name__ == "__main__":
    main()
