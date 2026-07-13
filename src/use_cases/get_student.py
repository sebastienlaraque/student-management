"""
Layer 2 — Use Case: Get Student
Single responsibility: retrieve one student by ID.
"""

from __future__ import annotations

from src.entities.student import Student
from src.use_cases.interfaces.student_repository import StudentRepository


class GetStudent:
    def __init__(self, repository: StudentRepository):
        self._repo = repository

    def execute(self, student_id: str) -> Student:
        """Return the student with the given ID. Raises ValueError if not found."""
        student = self._repo.find_by_id(student_id)
        if student is None:
            raise ValueError(f"Aucun étudiant trouvé avec l'ID : {student_id}")
        return student

