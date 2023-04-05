import subprocess
from datetime import datetime

inicio = datetime.now()
i = 1
while i <= 10:
    subprocess.run('cd  ./10MilBranches && git fetch && git pull' + r' && copy .\..\arquivo.txt arquivo_de_teste_' + str(6000 + i) + '.txt && git add . && git commit -m "commit ' + str(6000 + i) + '" && git push && cd ..', shell=True)
    i = i + 1
fim = datetime.now()

print(inicio)
print(fim)
print(fim - inicio)
