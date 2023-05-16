from .main import view
from .parser import parse, help, ParseError
import sys


def entrypoint(args=None):
    f"""Command-line interface for `view`
    
    {help}
    
    """
    # Exceptions are dealt with here
    try:
        _entrypoint(args)
    except ParseError as e:
        print(help)
        print(f'[ERROR] {str(e)}', file=sys.stderr)
    except Exception as e:
        print(f'[ERROR] {str(e)}', file=sys.stderr)


def _entrypoint(args):
    """Command-line interface for `denoise_mri` without exception handling"""
    args = args or sys.argv[1:]

    options = parse(args)
    if not options:
        return

    view(options.files)
