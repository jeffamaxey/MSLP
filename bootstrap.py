import os

PIP_BIN = 'pip'
REQUIREMENTS_PIP = './requirements.pip'
VIRTUALENV_BIN = 'virtualenv'
VIRTUALENV_DIR = './venv'

try:
    del os.environ['PIP_RESPECT_VIRTUALENV']
except KeyError:
    pass

try:
    del os.environ['PIP_VIRTUALENV_BASE']
except KeyError:
    pass

try:
    os.mkdir(VIRTUALENV_DIR)
except OSError:
    pass

os.system(f'{VIRTUALENV_BIN} --distribute {VIRTUALENV_DIR}')
os.system(f'{VIRTUALENV_DIR}/bin/pip install -r {REQUIREMENTS_PIP}')
