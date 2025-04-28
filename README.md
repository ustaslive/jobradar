# Work in progress

# Install in dev
```
git clone https://github.com/ustaslive/jobradar.git
python3.11 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt -r requirements-dev.txt
pre-commit install
```

# Python packages for prod
prod env: 

`pip install -r requirements.txt`


# git hooks
## run them manually
`pre-commit run --all-files`

# Structure
## ./scripts
Working scripts

## ./tests
Tests for python code


# How to run tests
Tests based on `pytest`

```
cd /path/to/project/
export PYTHONPATH=$(pwd)
pytest
```
