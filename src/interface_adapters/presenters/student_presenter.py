"""Layer 3 — Presenter: StudentPresenter
Formats Student entities into different output shapes.
Use cases return raw entities; presenters transform them for delivery layers.
"""

from __future__ import annotations

from typing import Any, Dict, List

from src.entities.student import Student, Status, StudentClass


class StudentPresenter:

    @staticmethod
    def to_dict(student: Student) -> Dict[str, Any]:
        """Serialize a Student to a plain dict (usable by JSON, CLI, etc.)."""
        return {
            "student_id": student.student_id,
            "full_name": student.full_name,
            "email": student.email,
            "parent_phone_number": student.parent_phone_number,
            "student_phone_number": student.student_phone_number,
            "status": student.status.value,
            "student_class": student.student_class.value,
        }

    @staticmethod
    def to_dict_list(students: List[Student]) -> List[Dict[str, Any]]:
        """Serialize a list of Students."""
        return [StudentPresenter.to_dict(s) for s in students]

    @staticmethod
    def to_cli_line(student: Student) -> str:
        return (
            f"[{student.student_id}...]  {student.full_name:<24} "
            f"Status: {student.status.value} | Class: {student.student_class.value}"
        )

    @staticmethod
    def to_cli_detail(student: Student) -> str:
        lines = [
            "─" * 60,
            f"  Student ID          : {student.student_id}",
            f"  Full name           : {student.full_name}",
            f"  Email               : {student.email}",
            f"  Parent phone number: {student.parent_phone_number}",
            f"  Student phone number: {student.student_phone_number or '—'}",
            f"  Status              : {student.status.value}",
            f"  Student class       : {student.student_class.value}",
            "─" * 60,
        ]
        return "\n".join(lines)

