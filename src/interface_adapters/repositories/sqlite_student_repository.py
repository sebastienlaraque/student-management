"""
Layer 3 — Adapter: SQLiteStudentRepository
Persists students in a local SQLite database.
Swappable with InMemoryStudentRepository without touching any use case.
"""

from __future__ import annotations

import sqlite3
from typing import List, Optional

from src.entities.student import Student, Status, StudentClass
from src.use_cases.interfaces.student_repository import StudentRepository


class SQLiteStudentRepository(StudentRepository):
    def __init__(self, db_path: str = "students.db"):
        self._db_path = db_path
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS students (
                    student_id TEXT PRIMARY KEY,
                    full_name  TEXT NOT NULL,
                    email      TEXT NOT NULL,
                    parent_phone_number TEXT NOT NULL,
                    student_phone_number TEXT,
                    status     TEXT NOT NULL,
                    student_class TEXT NOT NULL
                )
                """
            )
            conn.commit()

    @staticmethod
    def _row_to_student(row: sqlite3.Row) -> Student:
        return Student(
            student_id=row["student_id"],
            full_name=row["full_name"],
            email=row["email"],
            parent_phone_number=row["parent_phone_number"],
            student_phone_number=row["student_phone_number"],
            status=Status(row["status"]),
            student_class=StudentClass(row["student_class"]),
        )

    def save(self, student: Student) -> Student:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO students (
                    student_id, full_name, email, parent_phone_number,
                    student_phone_number, status, student_class
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    student.student_id,
                    student.full_name,
                    student.email,
                    student.parent_phone_number,
                    student.student_phone_number,
                    student.status.value,
                    student.student_class.value,
                ),
            )
            conn.commit()
        return student

    def find_by_id(self, student_id: str) -> Optional[Student]:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT * FROM students WHERE student_id = ?", (student_id,)
            ).fetchone()
        return self._row_to_student(row) if row else None

    def find_all(self) -> List[Student]:
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM students").fetchall()
        return [self._row_to_student(r) for r in rows]

    def update(self, student: Student) -> Student:
        with self._connect() as conn:
            cursor = conn.execute(
                """
                UPDATE students
                SET full_name = ?, email = ?, parent_phone_number = ?,
                    student_phone_number = ?, status = ?, student_class = ?
                WHERE student_id = ?
                """,
                (
                    student.full_name,
                    student.email,
                    student.parent_phone_number,
                    student.student_phone_number,
                    student.status.value,
                    student.student_class.value,
                    student.student_id,
                ),
            )
            conn.commit()

        if cursor.rowcount == 0:
            raise ValueError(f"Aucun étudiant trouvé avec l'ID : {student.student_id}")
        return student

    def delete(self, student_id: str) -> None:
        with self._connect() as conn:
            cursor = conn.execute(
                "DELETE FROM students WHERE student_id = ?", (student_id,)
            )
            conn.commit()
        if cursor.rowcount == 0:
            raise ValueError(f"Aucun étudiant trouvé avec l'ID : {student_id}")

