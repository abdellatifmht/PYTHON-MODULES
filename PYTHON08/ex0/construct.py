import os
import sys
import site


def is_venv() -> bool:
    return (
        hasattr(sys, 'real_prefix') or
        (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    )


def get_venv_name() -> str:
    if "VIRTUAL_ENV" in os.environ:
        venv_path = os.environ["VIRTUAL_ENV"]
        return os.path.basename(venv_path)
    return "None detected"


def get_site_packages() -> str:
    path = site.getsitepackages()
    if path:
        return path[1] if len(path) > 1 else path[0]
    return "Site-packages path not found"


def display_outside_matrix() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_venv_name()}")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print("\nThen run this program again.")


def display_inside_matrix() -> None:
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_venv_name()}")
    print(f"Environment Path: {sys.prefix}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print(f"\nPackage installation path:\n{get_site_packages()}")


def main() -> None:
    if is_venv():
        display_inside_matrix()
    else:
        display_outside_matrix()


if __name__ == "__main__":
    main()
