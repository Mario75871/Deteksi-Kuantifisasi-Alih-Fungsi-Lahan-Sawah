@echo off
title PCD Badung - Dashboard Monitoring Alih Fungsi Lahan Sawah
cd /d "%~dp0"

echo ==============================================================================
echo        PCD BADUNG: MONITORING ALIH FUNGSI SAWAH (2018 - 2026)
echo ==============================================================================
echo.

:: 1. Memeriksa ketersediaan Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python tidak terdeteksi di sistem PATH!
    echo Silakan install Python 3.10+ terlebih dahulu dan centang 'Add Python to PATH'.
    echo.
    pause
    exit /b 1
)

echo [1/2] Memeriksa dan menginstal seluruh dependensi dari requirements.txt...
python -m pip install --upgrade pip --quiet
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Terjadi kesalahan saat menginstal dependensi.
    echo Silakan periksa koneksi internet Anda atau log error di atas.
    echo.
    pause
    exit /b 1
)

echo.
echo [2/2] Memulai server Streamlit Web Dashboard...
echo Dashboard akan otomatis terbuka di browser Anda (http://localhost:8501)...
echo Tekan Ctrl+C di jendela ini jika ingin menghentikan aplikasi.
echo ==============================================================================
echo.

python -m streamlit run app.py

if %errorlevel% neq 0 (
    echo.
    echo [INFO] Aplikasi telah ditutup atau terjadi gangguan.
    pause
)
