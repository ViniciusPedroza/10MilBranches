import subprocess

i = 1
print('Inicio')
while i <= 100:
    try:
        print('Branch numero: ' + str(i))
        
        # Remove local Branch
        subprocess.run('git branch -D branch_' + str(i) + 'k')
        
        #Remove remote Branch
        #subprocess.run('git push origin -d branch_' + str(i))
    except:
        print("Falha na criação ou mudança de branch")
        pass
    i = i + 1