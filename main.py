import sys

__version__ = "v0.0.1"

def print_version():
    print(__version__)
    sys.exit(0)

if __name__ == "__main__":
    print_version()