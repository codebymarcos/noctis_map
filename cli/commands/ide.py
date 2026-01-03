import sys
import os
from rich.console import Console

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.ide.ide import IDE

console = Console()


def register(subparsers):
    # Registra comando ide
    parser = subparsers.add_parser('ide', help='Editor com realce de sintaxe')
    parser.add_argument('file', help='Arquivo a editar')
    parser.set_defaults(func=execute)


def execute(args):
    # Executa ide
    console.print(f"\n[bold yellow]ide[/bold yellow] [dim]{args.file}[/dim]\n")
    IDE().edit(args.file)
