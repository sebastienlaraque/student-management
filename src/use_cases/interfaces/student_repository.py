"""
Layer 2 — Interface (PORT)
Abstract contract that every repository adapter must respect.
Use cases depend ONLY on this interface, never on a concrete implementation.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from src.entities.student import Student


class StudentRepository(ABC):

    @abstractmethod
    def save(self, student: Student) -> Student:
        """Persist a new student. Returns the saved student."""
        ...

    @abstractmethod
    def find_by_id(self, student_id: str) -> Optional[Student]:
        """Return a student by ID, or None if not found."""
        ...

    @abstractmethod
    def find_all(self) -> List[Student]:
        """Return all students."""
        ...

    @abstractmethod
    def update(self, student: Student) -> Student:
        """Update an existing student. Raises ValueError if not found."""
        ...

    @abstractmethod
    def delete(self, student_id: str) -> None:
        """Delete a student by ID. Raises ValueError if not found."""
        ...
