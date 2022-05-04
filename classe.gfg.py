import os

def main():
    x = input('1. Desligar\n2. Cancelar Desligamento\n3. Fechar\n')
    if x == '1':
        desligar()
    elif x == '2':
        cancelar()
    elif x == '3':
        exit()
    else:
        print('Opção inválida!')
        
def cancelar():
    comando('shutdown -a')
    
def desligar():
    t = int(input('Quantos minutos para desligar:\n'))
    t = str(t*60)
    cmd = 'shutdown -s -f -t ' + (t)
    comando(cmd)
    
def comando(cmd):
    os.system(cmd)

    
if __name__ == '__main__':
    main()