# 1. Crear el ambiente virtual
if (-Not (Test-Path -Path ".\.venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
} else {
    Write-Host "Virtual environment already exists."
}

# 2. Activar el ambiente virtual
Write-Host "Setting Execution Policy..."
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force

Write-Host "Activating virtual environment..."
. .\.venv\Scripts\Activate.ps1

# 3. Instalar los requerimientos
Write-Host "Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Correr el script de shortcut_maker.py
Write-Host "Running shortcut maker script..."
python .\scripts\shortcut_maker.py

# 5. Desactivar el ambiente virtual
Write-Host "Deactivating virtual environment..."
deactivate

Write-Host "Setup complete. Exiting..."