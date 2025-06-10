"""
setup_path.py

Adiciona o diretório raiz do projeto ao caminho de busca de módulos do Python (sys.path).
Isso garante que os módulos internos (ex: `from aws.session import ...`) possam ser importados
corretamente mesmo quando os scripts são executados a partir de subpastas.

Uso:
    Basta incluir `from setup_path import *` no início de qualquer script
    que precise acessar módulos internos do projeto.
"""

import sys
from pathlib import Path

# Obtém o caminho absoluto até a raiz do projeto
ROOT = Path(__file__).resolve().parent

# Adiciona o caminho raiz ao sys.path se ainda não estiver presente
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
    
# PYTHONPATH=$(pwd) python <nome_do_arquivo_para_rodar>