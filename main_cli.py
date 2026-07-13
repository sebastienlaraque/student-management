"""
Entry point — CLI
Run: python main_cli.py
Swap InMemoryStudentRepository for SQLiteStudentRepository for persistence.
"""

from src.interface_adapters.repositories.in_memory_student_repository import (
    InMemoryStudentRepository,
)
# from src.interface_adapters.repositories.sqlite_student_repository import (
#     SQLiteStudentRepository,
# )
from src.frameworks.cli.cli_app import run_cli

if __name__ == "__main__":
    repository = InMemoryStudentRepository()
    # repository = SQLiteStudentRepository("students.db")   # ← persistent mode
    run_cli(repository)
