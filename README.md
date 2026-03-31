# ⚖️ BalanceMate

**BalanceMate** is a deeply optimized, cross-platform desktop application designed to process bank statement CSV files and flawlessly export the transactions into a formatted Excel report. It takes the pain out of managing and balancing monthly accounting sheets.

![BalanceMate Overview](resources/icons/icon.png)

## ✨ Key Features
- **Cross-Platform Support**: Runs natively and beautifully on both **macOS** and **Windows**.
- **Modern Premium UI**: Featuring a sleek Dark Mode aesthetic rendered with Qt Style Sheets, utilizing zero-lag system typography and dynamic drag-and-drop dropzones.
- **Lightning-Fast Generation**: The underlying data engine processes banking statements instantly into an `.xlsx` templated model with zero structural bottleneck.
- **Smart Data Validation**: Built-in `Sniffer` dynamically detects delimiter boundaries (`,`, `;`), checks for missing required columns, verifies content structures, and returns detailed human-readable errors via the GUI if a bad CSV is uploaded.
- **Automated Windows Builds**: Seamlessly generates bundled `.exe` executables through GitHub Actions.

## 🚀 Installation & Usage

### Prerequisites
- Python 3.9+ 
- (Optional) Git

### Quickstart (macOS & Windows Source)
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/balance-mate.git
    cd balance-mate
    ```

2. **Set up the Virtual Environment & Dependencies:**
    ```bash
    python -m venv .venv
    
    # On macOS:
    source .venv/bin/activate
    # On Windows:
    .\.venv\Scripts\Activate.ps1
    
    pip install -r requirements.txt
    ```

3. **Launch the Application:**
    ```bash
    python main.pyw
    ```

---

## 💻 Packaging an Executable (`.exe`) for Windows

If you wish to distribute a standalone `.exe` file that doesn't require Python to be installed on the host machine, you have two options:

### Option A: GitHub Actions (Automated & Recommended)
1. Push your code to the GitHub repository.
2. The bundled GitHub Action (`.github/workflows/build-windows.yml`) will automatically trigger.
3. Wait ~2 minutes for the build to pass.
4. Download your compiled standalone application from the **Artifacts** summary under the "Actions" tab.

### Option B: Local Windows Build
If you are currently on a Windows machine:
1. Double click the **`build.bat`** file from the root directory.
2. PyInstaller will compile everything statically and output the `.exe` inside the automatically generated `dist/` directory.

---

## 📁 CSV Structure Requirements
For the application to correctly balance the sheet, the input CSV banking statement must maintain the following headers (as exported natively by standard Spanish bank platforms):
- `oficina`
- `fechaMovimiento`
- `numeroDocumento`
- `debito`
- `credito`
- `descripcion`

## 🤝 Contributing
If you would like to contribute to BalanceMate, please fork the repository and submit a pull request. We welcome all contributions!

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📞 Contact
For any questions or issues, please open an issue on the [GitHub repository](https://github.com/yourusername/balance-mate/issues).