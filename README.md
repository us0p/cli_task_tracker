# CLI Task Tracker
A modular, command-line task tracking tool built using clean architecture principles.

## 🧱 Architecture Overview
The project follows a **Clean Architecture** pattern, divided into the following layers:

- **Domain Layer** (`src/domain`): Core business logic, entities (`Task`), and domain-specific rules.
- **Application Layer** (`src/application`): Application logic orchestrating domain entities, not directly dependent on any framework or interface.
- **Interface Layer** (`src/interfaces`): Adapters for user interfaces (CLI), output formatting (tabulation), and persistence (repository pattern).
- **Controller Layer** (`src/controllers`): Coordinates between interface and application logic (if applicable).

This separation ensures that changes in external tools (CLI parsing, display, etc.) don't affect core logic.

## 🛠 Tools & Technologies

- **Python 3.12**
- **Tabulated Output** with [tabulate](https://pypi.org/project/tabulate/)
- **Unit Testing** with [pytest](https://docs.pytest.org)

## 📂 Project Structure
cli_task_tracker/  
├── main.py # Entry point  
├── src/  
│ ├── domain/ # Core business logic  
│ ├── application/ # Application services  
│ ├── interfaces/ # CLI, display, and repo implementations  
│ └── controllers/ # Optional controllers  
└── README.md # Project documentation

## 🚀 How to Use

### 1. Clone and Set Up

```bash
git clone <your_repo_url>
cd cli_task_tracker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the CLI

```bash
python main.py --help
```

Use available CLI commands to add, view, or manage tasks. The command router handles argument parsing and routes commands appropriately.

### 3. Run Tests
Unit tests are located alongside domain and interface logic. Use pytest to run all tests:

```
pytest
```

## 📌 Example Commands

```bash
# List all tasks
python main.py list

# Add a new task
python main.py add --title "Buy groceries" --due "2024-05-01"
```

🧑‍💻 Author
Developed by [us0p](https://github.com/us0p) — Clean, extensible, testable code for simple task management in the terminal.
