from time import sleep
import os

def temporizador():

    contador = 0
    cont= 0
    os.system('clear')
    print("Wait for a seconds please ...")
    while cont >=0:
        sleep(2)
        contador+=1
        os.system('clear')
        print('Wait....',end=' ')
        print(contador)
        if contador == 10:
            break
        #sleep(1)
    
if __name__ == ('main'):
    temporizador()




temporizador()