@echo off
REM Windows batch: build and upload to PyPI
REM Requires uv (pip install uv) and packages: build, twine

uv pip install build twine
uv run python -m build
uv run twine upload dist/*

REM If not using uv, use:
REM python -m pip install build twine
REM python -m build
REM twine upload dist/*

REM Upload will auto-read %USERPROFILE%\.pypirc or env var PYPI_TOKEN
pause
