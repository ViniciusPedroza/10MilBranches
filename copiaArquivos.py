import subprocess
from datetime import datetime


i = 1
while i <= 10000:
    print('Arquivo numero: ' + str(i))
    subprocess.run('cd  ./10MilBranches' + r' && copy .\..\arquivo.txt arquivo_de_teste_' + str(i) + '.txt', shell=True)
    i = i + 1