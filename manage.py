#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
        # port = os.getenv("DJANGO_PORT", "3081")  # Lấy port từ biến môi trường, mặc định là 8000
       
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    # execute_from_command_line([sys.argv[0], "runserver", f"0.0.0.0:{port}"])

if __name__ == '__main__':
    main()
