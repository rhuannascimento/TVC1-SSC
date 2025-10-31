
#!/usr/bin/env bash
set -euo pipefail

# Cria um ambiente virtual e instala dependências do requirements.txt
# Uso: ./setup.sh [venv_dir]

VENV_DIR="${1:-venv}"
REQ_FILE="requirements.txt"

echo "==> Setup: venv='${VENV_DIR}' requirements='${REQ_FILE}'"

if ! command -v python3 >/dev/null 2>&1; then
	echo "Erro: python3 não encontrado no PATH. Instale o Python 3." >&2
	exit 1
fi

PYTHON=python3

if [ -d "${VENV_DIR}" ]; then
	echo "Aviso: diretório '${VENV_DIR}' já existe. Usando venv existente."
else
	echo "Criando venv em '${VENV_DIR}'..."
	${PYTHON} -m venv "${VENV_DIR}"
fi

echo "Ativando venv..."
. "${VENV_DIR}/bin/activate"

echo "Atualizando pip, setuptools e wheel..."
python -m pip install --upgrade pip setuptools wheel

if [ -f "${REQ_FILE}" ]; then
	echo "Instalando dependências de '${REQ_FILE}'..."
	python -m pip install -r "${REQ_FILE}"
else
	echo "Arquivo '${REQ_FILE}' não encontrado — pulando instalação de dependências."
fi

echo "Concluído. Para ativar o ambiente manualmente:"
echo "  source ${VENV_DIR}/bin/activate"

exit 0
