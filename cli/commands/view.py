import sys
import os
from rich.console import Console

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.view.view import view as view_func

console = Console()


def register(subparsers):
    # Registra comando view
    parser = subparsers.add_parser('view', help='Visualiza estrutura de pasta')
    parser.add_argument('path', help='Caminho da pasta')
    parser.set_defaults(func=execute)


def execute(args):
    # Executa view
    console.print(f"\n[bold green]view[/bold green] [dim]{args.path}[/dim]\n")
    view_func(args.path)
