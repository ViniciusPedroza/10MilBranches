import subprocess
from datetime import datetime

inicio = datetime.now()

#fghph_l7GoEtmmbZt4gNH1nDKt79CTyJSZ6m0hiPge3
i = 1
while i <= 10000:
    try:
        print('Branch numero: ' + str(i))
        subprocess.run('cd  ./10MilBranches  && git checkout -b branch_' + str(i) + r' && copy .\..\arquivo.txt arquivo_de_teste_' + str(i) + '.txt && git add . && git commit -m "Adicao do documento ' + str(i) + '" && git push --set-upstream origin branch_' + str(i) + ' && git checkout Desenvolvimento', shell=True)  
    except:
        print("Falha na criação ou mudança de branch")
        pass
    i = i + 1
    
fim = datetime.now()

print(inicio)
print(fim)
print(fim - inicio)
