# Student Management (Clean Architecture)

## Overview
This project is organized in a clean-architecture style:
- **entities**: business rules and domain models
- **use_cases**: application/business operations
- **interface_adapters**: controllers/repositories/presenters
- **frameworks**: CLI / web delivery mechanisms

---

## Entities


### `Student`
Located at: `src/entities/student.py`

Current model (as implemented in the code):
- `full_name: str`
- `email: str`
- `parent_phone_number: str`
- `student_phone_number: Optional[str] = None`
- `status: Status = Status.ACTIVE`
- `student_id: str = None` *(identifiant de l’étudiant)*
- `student_class: StudentClass = StudentClass.FIRST_GRADE`

#### Validation (`__post_init__`)
- `full_name` must be non-empty
- `email` must contain the domain `@edulink.edu.ht`
- `parent_phone_number` must be a string of exactly 8 digits
- `student_phone_number` (if provided) must be a string of exactly 8 digits
- `status` must be a valid `Status`
- `student_class` must be a valid `StudentClass`
- `student_id` must be a `str` (la validation actuelle exige un `str`)

---

### `Status` (enum)
Located in: `src/entities/student.py`
- `ACTIVE = "active"`
- `INACTIVE = "inactive"`
- `SUSPENDED = "suspended"`
- `DROPPED_OUT = "dropped_out"`

---

### `StudentClass` (enum)
Located in: `src/entities/student.py`

CAF / grades:
- `FIRST_GRADE = "1AF"`
- `SECOND_GRADE = "2AF"`
- `THIRD_GRADE = "3AF"`
- `FOURTH_GRADE = "4AF"`
- `FIFTH_GRADE = "5AF"`
- `SIXTH_GRADE = "6AF"`
- `SEVENTH_GRADE = "7AF"`
- `EIGHTH_GRADE = "8AF"`
- `NINTH_GRADE = "9AF"`

NS tracks:
- `NS1 = "NS1"`
- `NS2 = "NS2"`
- `NS3 = "NS3"`
- `NS4 = "NS4"`

---

---

## Project structure

```text
student_management/
├─ main_cli.py
├─ README.md
├─ TODO.md
├─ src/
│  ├─ __init__.py
│  ├─ entities/
│  │  ├─ __init__.py
│  │  └─ student.py
│  ├─ frameworks/
│  │  ├─ __init__.py
│  │  └─ cli/
│  │     ├─ __init__.py
│  │     └─ cli_app.py
│  ├─ interface_adapters/
│  │  ├─ __init__.py
│  │  ├─ controllers/
│  │  │  ├─ __init__.py
│  │  │  └─ student_controller.py
│  │  ├─ presenters/
│  │  │  ├─ __init__.py
│  │  │  └─ student_presenter.py
│  │  └─ repositories/
│  │     ├─ __init__.py
│  │     ├─ in_memory_student_repository.py
│  │     └─ sqlite_student_repository.py
│  └─ use_cases/
│     ├─ __init__.py
│     ├─ interfaces/
│     │  ├─ __init__.py
│     │  └─ student_repository.py
│     ├─ add_student.py
│     ├─ delete_student.py
│     ├─ get_student.py
│     ├─ list_students.py
│     └─ update_student.py
└─ tests/
   ├─ __init__.py
   ├─ test_entities.py
   ├─ test_use_cases.py
   └─ test_web_api.py
```

---

## Run
### Tests
```bash
pytest -q
```

### CLI
```bash
python main_cli.py
```

---


## Next step (optional)
If you want to migrate `Student` to the richer model you provided (with `status`, `student_class`, phone numbers, etc.), you’ll need to update:
- use cases (add/update)
- controllers/presenters
- repositories mapping
- tests

