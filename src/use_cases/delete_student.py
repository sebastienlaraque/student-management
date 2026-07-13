"""
Layer 2 — Use Case: Delete Student
Single responsibility: remove a student from the repository.
"""

from __future__ import annotations

from src.use_cases.interfaces.student_repository import StudentRepository


class DeleteStudent:
    def __init__(self, repository: StudentRepository):
        self._repo = repository

    def execute(self, student_id: str) -> None:
        """Delete the student with the given ID. Raises ValueError if not found."""
        existing = self._repo.find_by_id(student_id)
        if existing is None:
            raise ValueError(f"Aucun étudiant trouvé avec l'ID : {student_id}")
        self._repo.delete(student_id)

