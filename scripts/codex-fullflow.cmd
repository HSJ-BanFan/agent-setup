@echo off
setlocal
title Codex Queue (codex-probe.py)
rem ASCII-only on purpose: cmd.exe misparses UTF-8 Chinese comments under GBK.
rem All Chinese output comes from the Python script (UTF-8 safe).
rem
rem   Double-click       = full flow (probe until in, then keepalive every 300s)
rem   codex-fullflow.cmd "your message"   = also send this message once you get in
rem   codex-fullflow.cmd stats            = show statistics report
rem   codex-fullflow.cmd clean            = clean test session files (no prompt)
chcp 65001 >nul
cd /d "%~dp0"

set "PY=%~dp0codex-probe.py"
if not exist "%PY%" set "PY=%USERPROFILE%\codex-probe.py"
if not exist "%PY%" (
  echo ERROR: codex-probe.py not found next to this file or in %USERPROFILE%
  pause
  endlocal & exit /b 1
)

set "ARG=%~1"
if "%ARG%"=="" (
  python "%PY%" --fullflow
) else if /i "%ARG%"=="stats" (
  python "%PY%" --stats
) else if /i "%ARG%"=="clean" (
  python "%PY%" --clean --yes
) else (
  python "%PY%" --fullflow --fire "%~1"
)
set ERR=%ERRORLEVEL%
if %ERR% neq 0 (
  echo.
  echo Exit code: %ERR%   ^(0=normal, 2=max-tries, 3=permanent: key dead / model not mapped^)
)
echo.
echo Log:   %USERPROFILE%\.codex-queue\probe.log
echo Reply: %USERPROFILE%\.codex-queue\last-reply.txt  ^(when fire message used^)
pause
endlocal & exit /b %ERR%
