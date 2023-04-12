set -eu

if [ -d ".venv" ]
then
    echo "Using an existing virtual environment."
else
    echo "Virtual environment not found, creating."
    python3 -m venv .venv
fi

source .venv/bin/activate

pip install --quiet -r requirements.txt

pytest -s -v
