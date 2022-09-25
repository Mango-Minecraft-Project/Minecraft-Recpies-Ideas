from os import listdir
from os.path import isfile

for filename in listdir('../img'):
    if not isfile(f'../img/{filename}.json'):
        with open(f'../src/recipes/{filename[:-4]}.json', 'w') as file:
            file.write('{\n    \n}')