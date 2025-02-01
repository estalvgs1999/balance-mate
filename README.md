# BalanceMate

BalanceMate is a software application designed to process CSV files containing financial transactions and export the data to an Excel format. It is particularly useful for managing and reporting monthly balances.

## Features

- Reads and processes CSV files with financial data.
- Cleans and formats the data.
- Exports the processed data to an Excel file.
- User-friendly interface for selecting files and specifying report parameters.

## Installation

### Prerequisites

- Python 3.9 must be installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/release/python-390/).

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/balance-mate.git
    cd balance-mate
    ```

2. **Run the installation script:**

    Open PowerShell and navigate to the project directory. Then, execute the following command:

    ```ps1
    .\install.ps1
    ```

    This script will:
    - Create a virtual environment.
    - Activate the virtual environment.
    - Install the required dependencies.
    - Create a desktop shortcut for easy access.

## Running the Application

1. **Activate the virtual environment:**

    ```ps1
    .\.venv\Scripts\Activate.ps1
    ```

2. **Run the application:**

    ```sh
    python main.pyw
    ```

    Alternatively, you can use the desktop shortcut created during the installation process.

## Important Notes

- Ensure that your CSV files follow the expected structure with the required columns: `oficina`, `fechaMovimiento`, `numeroDocumento`, `debito`, `credito`, and `descripcion`.
- The application uses PyQt6 for the graphical user interface, so make sure your system supports it.

## Contributing

If you would like to contribute to BalanceMate, please fork the repository and submit a pull request. We welcome all contributions!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on the [GitHub repository](https://github.com/yourusername/balance-mate/issues).
## 📞 Contact

For any questions or issues, please open an issue on the [GitHub repository](https://github.com/yourusername/balance-mate/issues).

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

If you would like to contribute to BalanceMate, please fork the repository and submit a pull request. We welcome all contributions!