# Live development server with auto-reload
# Run this script to start the development server

Write-Host "Starting Sphinx auto-build server..." -ForegroundColor Green
Write-Host "The documentation will open at: http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop the server`n" -ForegroundColor Yellow

& .venv\Scripts\sphinx-autobuild.exe docs docs/_build/html --open-browser --port 8000
