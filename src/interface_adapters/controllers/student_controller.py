"""Layer 3 — Controller: StudentController
Orchestrates use cases and formats results via the presenter.
Delivery layers (CLI, Flask) call the controller — never use cases directly.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from src.entities.student import Status, StudentClass
from src.interface_adapters.presenters.student_presenter import StudentPresenter
from src.use_cases.add_student import AddStudent
from src.use_cases.delete_student import DeleteStudent
from src.use_cases.get_student import GetStudent
from src.use_cases.list_students import ListStudents
from src.use_cases.update_student import UpdateStudent
from src.use_cases.interfaces.student_repository import StudentRepository


class StudentController:

    def __init__(self, repository: StudentRepository):
        self._add = AddStudent(repository)
        self._get = GetStudent(repository)
        self._list = ListStudents(repository)
        self._update = UpdateStudent(repository)
        self._delete = DeleteStudent(repository)

    def add_student(
        self,
        full_name: Optional[str] = None,
        email: Optional[str] = None,
        parent_phone_number: Optional[str] = None,
        student_phone_number: Optional[str] = None,
        status: Status = Status.ACTIVE,
        student_class: StudentClass = StudentClass.FIRST_GRADE,
        # Backward-compatible param (used by the current CLI)
        name: Optional[str] = None,

    ) -> Dict[str, Any]:
        resolved_full_name = full_name or name
        resolved_email = email
        resolved_parent_phone_number = parent_phone_number or ""

        if resolved_full_name is None:
            raise TypeError("Missing required argument: full_name (or legacy name)")

        if resolved_email is None:
            raise TypeError("Missing required argument: email")

        if not resolved_parent_phone_number:
            raise TypeError("Missing required argument: parent_phone_number")

        # Defensive normalization

        resolved_parent_phone_number = str(resolved_parent_phone_number).strip()

        student = self._add.execute(
            full_name=resolved_full_name,
            email=resolved_email,
            parent_phone_number=resolved_parent_phone_number,
            student_phone_number=student_phone_number,
            status=status,
            student_class=student_class,
        )

        return StudentPresenter.to_dict(student)


    def get_student(self, student_id: str) -> Dict[str, Any]:
        student = self._get.execute(student_id)
        return StudentPresenter.to_dict(student)

    def list_students(self) -> List[Dict[str, Any]]:
        students = self._list.execute()
        return StudentPresenter.to_dict_list(students)

    def update_student(
        self,
        student_id: str,
        full_name: Optional[str] = None,
        email: Optional[str] = None,
        parent_phone_number: Optional[str] = None,
        student_phone_number: Optional[str] = None,
        status: Optional[Status] = None,
        student_class: Optional[StudentClass] = None,
    ) -> Dict[str, Any]:
        student = self._update.execute(
            student_id=student_id,
            full_name=full_name,
            email=email,
            parent_phone_number=parent_phone_number,
            student_phone_number=student_phone_number,
            status=status,
            student_class=student_class,
        )
        return StudentPresenter.to_dict(student)

    def delete_student(self, student_id: str) -> Dict[str, str]:
        self._delete.execute(student_id)
        return {"message": f"Étudiant {student_id!r} supprimé avec succès."}

