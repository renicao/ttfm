#!/usr/bin/env python

# This is a test comment for the first SFTP Sublime Text edit.
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ttfm.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
