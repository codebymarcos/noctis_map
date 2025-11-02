# import facilitado

import sys
import os

def load_noctis():
    # adicionar o caminho de noctis_map ao sys.path para facilitar imports
    noctis_path = os.path.dirname(os.path.dirname(__file__))
    if noctis_path not in sys.path:
        sys.path.insert(0, noctis_path)

i