"""Execute todos os testes a partir da raiz: python verify.py."""
from pathlib import Path
import subprocess,sys
base=Path(__file__).resolve().parent
for project in ('relatorios-producao-python','analise-logistica-sql','planejamento-entregas'):
 print(f'Validando {project}',flush=True)
 subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-v'],cwd=base/'projects'/project,check=True)
print('18 testes aprovados.')
