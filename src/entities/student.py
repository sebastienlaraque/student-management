"""src.entities.student

Layer 1 — Entities
Pure Python business object. No imports from outer layers.
"""


from dataclasses import dataclass
from typing import Optional
import enum


class Status(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    DROPPED_OUT = "dropped_out"


class StudentClass(enum.Enum):
    FIRST_GRADE = "1AF"
    SECOND_GRADE = "2AF"
    THIRD_GRADE = "3AF"
    FOURTH_GRADE = "4AF"
    FIFTH_GRADE = "5AF"
    SIXTH_GRADE = "6AF"
    SEVENTH_GRADE = "7AF"
    EIGHTH_GRADE = "8AF"
    NINTH_GRADE = "9AF"

    NS1 = "NS1"
    NS2 = "NS2"
    NS3 = "NS3"
    NS4 = "NS4"


@dataclass
class Student:
    student_id: str
    full_name: str
    email: str
    parent_phone_number: str
    student_phone_number: Optional[str] = None
    status: Status = Status.ACTIVE
    student_class: StudentClass = StudentClass.FIRST_GRADE

    # Business rules
    def __post_init__(self):
        if not self.full_name or not self.full_name.strip():
            raise ValueError("Full name is required.")


        if "@edulink.edu.ht" not in self.email:
            raise ValueError("email isn't valid.")

        if not isinstance(self.parent_phone_number, str) or len(self.parent_phone_number) != 8:
            raise ValueError("The parents' phone number must have exactly 8 digits.")

        if self.student_phone_number is not None and (
            not isinstance(self.student_phone_number, str) or len(self.student_phone_number) != 8
        ):
            raise ValueError("The student's phone number must have exactly 8 digits if provided.")

        if not isinstance(self.student_class, StudentClass):
            raise ValueError("Invalid student class.")

        

    def drop_out(self) -> None:
        """Marque l'étudiant comme ayant abandonné (dropped out)."""
        if self.status == Status.DROPPED_OUT:
            raise ValueError("Student is already dropped out.")
        self.status = Status.DROPPED_OUT

    def update_student_class(self, new_class: str) -> None:
        """Met à jour la classe de l'étudiant."""
        if not isinstance(new_class, StudentClass):
            raise ValueError("Invalid student class.")
        self.student_class = new_class

    def is_active(self) -> bool:
        """Vérifie si l'étudiant est actif."""
        return self.status == Status.ACTIVE

    def is_inactive(self) -> bool:
        """Vérifie si l'étudiant est inactif."""
        return self.status == Status.INACTIVE

    def is_suspended(self) -> bool:
        """Vérifie si l'étudiant est suspendu."""
        return self.status == Status.SUSPENDED

    def is_dropped_out(self) -> bool:
        """Vérifie si l'étudiant a abandonné."""
        return self.status == Status.DROPPED_OUT

