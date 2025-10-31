import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
PY = sys.executable or "python3"


def run_script(rel_path, heading):
    script = str(BASE / rel_path)
    print(f"=== {heading} ===")
    subprocess.run([PY, script], check=True)


if __name__ == "__main__":
    run_script("utils/gerar_chaves.py", "Etapa 1: Gerando chaves RSA")
    print()
    run_script("utils/origem.py", "Etapa 2: Assinando e criptografando mensagem")
    print()
    run_script("utils/destino.py", "Etapa 3: Decifrando e verificando assinatura")

    print("\nProcesso concluído com sucesso!")
