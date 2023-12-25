# Deploy.ps1
python -m pip install --upgrade pip
python -m venv .venv
.venv\Scripts\activate
pip install -r requirement.txt
# Define variables
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --workers 4
Start-Process -NoNewWindow -FilePath "cmd.exe" -ArgumentList "/c", "python -m $UvicornCommand"
