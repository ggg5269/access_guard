@echo off
REM Windows 批次檔：build 並上傳到 PyPI
REM 需先安裝 uv (pip install uv) 及 build、twine

uv pip install build twine
uv run python -m build
uv run twine upload dist/*

REM 若未用 uv，請改用：
REM python -m pip install build twine
REM python -m build
REM twine upload dist/*

REM 上傳時會自動讀取 %USERPROFILE%\.pypirc 或環境變數 PYPI_TOKEN
pause
