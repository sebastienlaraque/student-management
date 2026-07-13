"""
Layer 2 — Use Case: Update Student
Single responsibility: apply partial updates to an existing student.
"""

from __future__ import annotations

from typing import Optional

from src.entities.student import Student, Status, StudentClass
from src.use_cases.interfaces.student_repository import StudentRepository


class UpdateStudent:
    def __init__(self, repository: StudentRepository):
        self._repo = repository

    def execute(
        self,
        student_id: str,
        full_name: Optional[str] = None,
        email: Optional[str] = None,
        parent_phone_number: Optional[str] = None,
        student_phone_number: Optional[str] = None,
        status: Optional[Status] = None,
        student_class: Optional[StudentClass] = None,
    ) -> Student:
        """Find the student, apply only provided fields, then persist."""
        existing = self._repo.find_by_id(student_id)
        if existing is None:
            raise ValueError(f"Aucun étudiant trouvé avec l'ID : {student_id}")

        updated = Student(
            student_id=existing.student_id,
            full_name=full_name.strip() if full_name is not None else existing.full_name,
            email=email.strip() if email is not None else existing.email,
            parent_phone_number=parent_phone_number
            if parent_phone_number is not None
            else existing.parent_phone_number,
            student_phone_number=student_phone_number.strip()
            if student_phone_number is not None
            else existing.student_phone_number,
            status=status if status is not None else existing.status,
            student_class=student_class if student_class is not None else existing.student_class,
        )
        return self._repo.update(updated)

