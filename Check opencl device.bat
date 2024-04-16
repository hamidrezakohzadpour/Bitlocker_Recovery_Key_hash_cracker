@echo off
COLOR 02
TIME /T Key new_time
john.exe --list=opencl-devices
TIME /T Key new_time
pause
