@echo off

:: Start CTC Frontend
START "CTCFrontend" "%~dp0nginx-1.22.1/nginx.exe"
:: Start CTC Backend
START "CTCBackend" "%~dp0ctcbackend/main.exe"

:: Start python