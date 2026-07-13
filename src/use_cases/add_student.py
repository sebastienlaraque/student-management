"""
Layer 2 — Use Case: Add Student
Single responsibility: create and persist a new student.
"""



import uuid
from typing import Optional

from src.entities.student import Student, Status, StudentClass
from src.use_cases.interfaces.student_repository import StudentRepository


class AddStudent:
    def __init__(self, repository: StudentRepository):
        self._repo = repository

    def execute(
        self,
        full_name: str,
        email: str,
        parent_phone_number: str,
        student_phone_number: Optional[str] = None,
        status: Status = Status.ACTIVE,
        student_class: StudentClass = StudentClass.FIRST_GRADE,
    ) -> Student:
        """Create a new Student and save it."""

        # Le modèle `Student` accepte un `student_id` optionnel.
        # Or les repositories (InMemory + SQLite) utilisent ce champ comme clé.
        # Sans génération d'ID, l'insertion écrase l'entrée `None`.
        student_id = str(uuid.uuid4())

        student = Student(
            student_id=student_id,
            full_name=full_name.strip(),
            email=email.strip(),
            parent_phone_number=parent_phone_number,
            student_phone_number=student_phone_number.strip()
            if student_phone_number is not None
            else None,
            status=status,
            student_class=student_class,
        )
        return self._repo.save(student)

