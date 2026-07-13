"""
Layer 3 — Adapter: InMemoryStudentRepository
Stores students in a plain Python dict (RAM only).
Perfect for tests and development — no external dependency.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from src.entities.student import Student
from src.use_cases.interfaces.student_repository import StudentRepository
import copy


class InMemoryStudentRepository(StudentRepository):
    def __init__(self):
        self._store: Dict[str, Student] = {}

    def save(self, student: Student) -> Student:
        if student.student_id in self._store:
            raise ValueError(f"Un étudiant avec l'ID {student.student_id!r} existe déjà.")
        self._store[student.student_id] = student
        return student

    def find_by_id(self, student_id: str) -> Optional[Student]:
        return self._store.get(student_id)

    def find_all(self) -> List[Student]:
        #return list(self._store.values())
        return [copy.deepcopy(s)for s in self._store.values()]

    def update(self, student: Student) -> Student:
        if student.student_id not in self._store:
            raise ValueError(f"Aucun étudiant trouvé avec l'ID : {student.student_id}")
        self._store[student.student_id] = student
        return student

    def delete(self, student_id: str) -> None:
        if student_id not in self._store:
            raise ValueError(f"Aucun étudiant trouvé avec l'ID : {student_id}")
        del self._store[student_id]

