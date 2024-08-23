from os import system


system('ruff format ./test')

system('pytest -n 15')
