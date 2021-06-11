
set -eu

PROJECT_ROOT=$(dirname $(dirname $(realpath $0)))
cd $PROJECT_ROOT

python3 -m venv venv
venv/bin/pip3 install --upgrade pip
venv/bin/pip3 install -r setup/requirements.txt
