# Run Django development server on port 11000
# Usage: Open PowerShell, cd to 'city' folder and run: .\runserver.ps1
# Optional: Activate your virtualenv before running. Example (adjust path):
# & "C:\Users\onkar\OneDrive\Desktop\Smart-City\Smart_City\Scripts\Activate.ps1"

$port = 11000
Write-Host "Starting Django dev server on port $port..."
python manage.py runserver 0.0.0.0:$port
