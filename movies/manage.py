#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movies.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Si deseas usar el servidor de desarrollo para servir HTML
    if 'runserver' in sys.argv:
        from django.core.management.commands.runserver import Command
        # Agrega configuración para servir archivos estáticos
        Command.use_ipv6 = True
        Command.use_threading = True

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
