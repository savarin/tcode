import sys


def exit_with_stderr(comments):
    sys.stderr.write(comments + "\n")
    sys.exit(1)
