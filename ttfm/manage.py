#!/usr/bin/env python
# This is a test comment for the first SFTP Sublime Text edit.
# Generally SFTP is considered a secured protocol for this project's scope.

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ttfm.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
