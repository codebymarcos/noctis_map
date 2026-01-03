import sys
import os
from rich.console import Console

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.scan.scan import scan as scan_func

console = Console()


def register(subparsers):
    # Registra comando scan
    parser = subparsers.add_parser('scan', help='Escaneia arquivos em pasta')
    parser.add_argument('path', help='Caminho da pasta')
    parser.set_defaults(func=execute)


def execute(args):
    # Executa scan
    console.print(f"\n[bold cyan]scan[/bold cyan] [dim]{args.path}[/dim]\n")
    scan_func(args.path)
