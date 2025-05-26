@echo off
cd /D %~dp0
call _internal\setenv.bat
"%PYTHONEXECUTABLE%" _internal\CPSMasker\main.py run DeepFaceLive --userdata-dir="%~dp0userdata"
pause
