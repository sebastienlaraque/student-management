"""
Layer 2 — Use Case: List Students
Single responsibility: return all persisted students.
"""

from __future__ import annotations

from typing import List

from src.entities.student import Student
from src.use_cases.interfaces.student_repository import StudentRepository


class ListStudents:
    def __init__(self, repository: StudentRepository):
        self._repo = repository

    def execute(self) -> List[Student]:
        """Return all students, sorted by full_name."""
        students = self._repo.find_all()
        return sorted(students, key=lambda s: s.full_name.lower())

