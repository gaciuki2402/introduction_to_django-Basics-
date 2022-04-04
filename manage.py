#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secondProject.settings')
=======
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Library_System.settings')
>>>>>>> c979997c2e55e1eea0d57b172d424e32f685934d
>>>>>>> eadf4933b17b4f1e48aa6f604a342fb4573953d9
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fifthProject.settings')
>>>>>>> c5cfede35fded4403fe8b335a6b75cf8207eecfa
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
