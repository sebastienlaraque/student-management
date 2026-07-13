"""
Layer 4 — Framework: Interactive CLI
Delivery mechanism. Talks to StudentController, never to use cases directly.
"""

import sys
import os

# Allow running directly: python src/frameworks/cli/cli_app.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))

from src.interface_adapters.controllers.student_controller import StudentController
from src.interface_adapters.presenters.student_presenter import StudentPresenter
from src.use_cases.interfaces.student_repository import StudentRepository


def _print_header():
    print("\n" + "═" * 55)
    print("       Student Management — CLI")
    print("═" * 55)


def _print_menu():
    print(
        """
  1.   Ajouter un étudiant
  2.   Lister tous les étudiants
  3.   Afficher un étudiant (par ID)
  4.   Modifier un étudiant
  5.   Supprimer un étudiant
  0.   Quitter
"""
    )


def _ask(prompt: str, required: bool = True) -> str:
    while True:
        value = input(f"  {prompt}: ").strip()
        if value or not required:
            return value
        print("  Ce champ est obligatoire.")


def _ask_optional(prompt: str) -> str | None:
    value = input(f"  {prompt} (Entrée pour ignorer): ").strip()
    return value if value else None


def _ask_phone_8(prompt: str) -> str:
    # Validation minimale côté UI: l'entity valide aussi.
    return _ask(prompt)


def _parse_class(class_value: str):
    from src.entities.student import StudentClass

    try:
        return StudentClass(class_value)
    except ValueError:
        valid = ", ".join([c.value for c in StudentClass])
        raise ValueError(f"Classe invalide. Valeurs possibles: {valid}")


# ── ACTIONS ──────────────────────────────────────────────────────────────────

def action_add(controller: StudentController):
    print("\n── Ajouter un étudiant ──")

    name = _ask("Nom")

    # UI demande DOB, mais ton entity actuelle n'a pas de champ dob.
    # On le collecte pour l'interface demandée, mais on ne le persiste pas.
    _ = _ask("Date de naissance — jour (ex: 22)")
    _ = _ask("Date de naissance — mois (ex: 12)")
    _ = _ask("Date de naissance — année (ex: 2000)")

    email = _ask("Email")
    parent_phone_number = _ask_phone_8("Téléphone parent (8 chiffres)")
    student_phone_number = _ask_optional("Téléphone élève")

    class_value = _ask("Classe (ex: 1AF, 2AF, ... ou NS1-NS4)")

    try:
        resolved_class = _parse_class(class_value)

        from src.entities.student import Status

        result = controller.add_student(
            full_name=name,
            email=email,
            parent_phone_number=parent_phone_number,
            student_phone_number=student_phone_number,
            status=Status.ACTIVE,
            student_class=resolved_class,
        )


        print(f"\n  Étudiant créé — ID: {result['student_id']}")
    except (ValueError, TypeError) as e:
        print(f"\n  Erreur : {e}")


def action_list(controller: StudentController):
    print("\n── Liste des étudiants ──")
    students = controller.list_students()
    if not students:
        print("  (aucun étudiant enregistré)")
        return
    print(f"\n  {len(students)} étudiant(s) trouvé(s):\n")
    for s in students:
        from src.entities.student import Student

        entity = Student(**s)
        print(" ", StudentPresenter.to_cli_line(entity))


def action_get(controller: StudentController):
    print("\n── Afficher un étudiant ──")
    student_id = _ask("ID de l'étudiant")
    try:
        result = controller.get_student(student_id)
        from src.entities.student import Student

        entity = Student(**result)
        print(StudentPresenter.to_cli_detail(entity))
    except ValueError as e:
        print(f"\n  {e}")


def action_update(controller: StudentController):
    print("\n── Modifier un étudiant ──")
    student_id = _ask("ID de l'étudiant à modifier")
    print("  (laissez vide pour conserver la valeur actuelle)")

    name = _ask_optional("Nouveau nom")
    email = _ask_optional("Nouvel email")
    parent_phone_number = _ask_optional("Nouveau téléphone parent (8 chiffres)")
    student_phone_number = _ask_optional("Nouveau téléphone élève")
    class_value = _ask_optional("Nouvelle classe (ex: 1AF, 2AF, ... ou NS1-NS4)")

    try:
        resolved_class = _parse_class(class_value) if class_value is not None else None

        result = controller.update_student(
            student_id=student_id,
            full_name=name,
            email=email,
            parent_phone_number=parent_phone_number,
            student_phone_number=student_phone_number,
            status=None,
            student_class=resolved_class,
        )
        print(f"\n  Étudiant mis à jour : {result['full_name']}")
    except (ValueError, TypeError) as e:
        print(f"\n  Erreur : {e}")


def action_delete(controller: StudentController):
    print("\n── Supprimer un étudiant ──")
    student_id = _ask("ID de l'étudiant à supprimer")
    confirm = input("   Confirmer la suppression ? (oui/non): ").strip().lower()
    if confirm != "oui":
        print("  Suppression annulée.")
        return
    try:
        result = controller.delete_student(student_id)
        print(f"\n  {result['message']}")
    except ValueError as e:
        print(f"\n  {e}")


# ── MAIN LOOP ────────────────────────────────────────────────────────────────

def run_cli(repository: StudentRepository):
    controller = StudentController(repository)
    _print_header()

    actions = {
        "1": action_add,
        "2": action_list,
        "3": action_get,
        "4": action_update,
        "5": action_delete,
    }

    while True:
        _print_menu()
        choice = input("  Votre choix : ").strip()

        if choice == "0":
            print("\n  Au revoir ! \n")
            break
        elif choice in actions:
            actions[choice](controller)
        else:
            print("  Choix invalide, veuillez réessayer.")

