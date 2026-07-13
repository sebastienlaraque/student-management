# Project structure

```text
student_management/
├─ main_cli.py
├─ README.md
├─ README_structure.md
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

