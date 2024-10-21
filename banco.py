import time
import json
import os
import random


# Base de datos predeterminada
BD = {

    "regVzl" : {
        "123" : {
            "nombre" : "fulanov",
            "cuenta" : "Corriente",
            "saldo" : 2000.00,
            "tar" : "63"
        }
    },

    "regpan" : {
        "456" : {
            "nombre" : "fulanov",
            "cuenta" : "Ahorro",
            "saldo" : 1000.00,
            "tar" : "45"
        }
    } 

}



# Funcion main (me gusta la estructura de C jaj)
def main():

    global BD
    n = 0
    band = Verificacion()

    while n != 4 and band:
        us = BD[pais][id_us]

        try:
            n = int(input('''
            Seleccione la operacion:
                1. Edo. de cuenta
                2. Deposito
                3. Retiro
                4. Salir          
                '''))

            # basicamente se le pregunta al usuario que quiere hacer y si esta en el rango admitido entonces llama a la funcion que esta en el indice de la lista
            if n in range (1, 5):
                funcion[n](us)
            else:
                print("Debe seleccionar una de las opciones dadas")
            
        except:
            print("Debe ser un entero")


# funcion para verificar usuario, yo lo hice por id y por el numero de tarjeta
def Verificacion():
    global id_us, pais #estas variables deben ser globales porque se manejan en el main

    # Para registrar nuevos usuarios
    if input('''¿Usted ya posee una cuenta o se quiere registrar?
            introduzca 'r' para registro / cualquier otra tecla para iniciar sesion''').lower() == 'r':
        
        funcion[0]()

    else:
        for i in range(5):
            #como ahora hay registro por nacionalidad tuve que preguntar para diferenciar (queria que un numero del id te identificara el pais por ser mas practico pero lo deje asi jaj)
            pais = naciones()
            id_us = input("introduzca su ID: ")
            tar_us = input("introduzca los ultimos numeros de la parte de atras de su tarjeta: ")
            if (id_us in BD[pais].keys() and (BD[pais][id_us]["tar"] == tar_us)): # se verifica que los datos sean ciertos (converti el diccionario en lista para no usar el metodo keys xd)
                return True 
            
            else:
                print("ID o Tarjeta invalida")
            
            if i == 2:
                print('''Ya va por el tercer intento, si se equivoca 2 veces mas se cerrara el programa...
                    Espere 5 seg para continuar''')
                time.sleep(5)
            
            if i == 4:
                print("se ha equivocado un numero de 5 veces, el programa se cerrara...")
                return False



def registro():
    global BD

    while True:
        try:
            pais = naciones()
            
            bs = BD[pais]
            
            dict = {} #se crea un diccionario momentaneo

            dict["nombre"] = input("ingrese su nombre: ")

            if input(''' si quiere una cuenta de ahorro introduzca la letra 'H',
                    en caso contrario se le atribuira automaticamente una cuenta corriente...

                    responda para conrinuar ('H' para ahorro / cualquier otra tecla para corriente):
                ''').lower() == 'h':
                dict["cuenta"] = "Ahorro"
            else:
                dict["cuenta"] = "Corriente"
            dict["saldo"] = 0.0
            dict["tar"] = str(random.randint(10, 99))
            ID = str(random.randint(100, 999))

            while ID in bs.keys():
                ID = str(random.randint(100, 999))
            
            if input(f'''
                sus datos serian:
                    Nombre: {dict["nombre"]}
                    Tipo de cuenta: {dict["cuenta"]}
                    su numero trasero de la tarjeta: {dict["tar"]}
                    Su ID para ingresar: {ID}
                    (acuerdese de los ultimos 2 datos que son importantes para ingresar)

                    ¿Esta de acuerdo con los datos? 'n' para No (repetir el proceso) / cualquier otra tecla para Si Y continuar
            ''').lower() == 'n':
                continue   
            else:
                bs[ID] = dict # se añade el diccionario a la base de datos
                with open('reg.json', 'wt') as f:
                    json.dump(BD, f, indent='\t')
                print("Se ha registrado exitosamente")
                break
        except:
            print("debe ingresar una de las opciones")
    

def naciones():
    pais = list(BD)[int(input('''¿Cual es su nacionalidad?
            1. Venezolana
            2. panameña
            ''')) - 1]
    return pais


def Edo(us):

    print(f'''
        Su estado de cuenta es:
          {us["saldo"]}
    ''')




def deposito(us):
    try:
        us["saldo"] = us["saldo"] + float(input("ingrese cuanto quiere depositar: "))
        Edo(us)
    except:
        print("debe ingresar un numero")




def retiro(us):
    try:
        n = float(input("ingrese cuanto quiere Retirar: "))

        if n <= us["saldo"]:
            us["saldo"] = us["saldo"] - n
            Edo(us)
        else:
            print("Saldo insuficiente!!!")
            Edo(us)
    except:
        print("debe ingresar un numero")



def salir(base):
    global BD
    print("Hasta la proxima!!!")
    with open('reg.json', 'wt') as f:
        json.dump(BD, f, indent='\t')


funcion = [registro, Edo, deposito, retiro, salir]



if os.path.exists("reg.json"):
    with open('reg.json', 'rt') as f:
        BD = json.load(f)




if __name__ == "__main__":
    main()


    



    