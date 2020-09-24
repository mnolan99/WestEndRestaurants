#!/usr/bin/env python
import os
import sys


#a script that allows us to launch the app from our machines, and to carry out various database commands
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WER_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
