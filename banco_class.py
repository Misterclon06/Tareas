import time
import json
import os
import random

# clase usuario
class Usuario():
    def __init__(U, name, tipo, balance, tar):
        U.__nombre = name
        U.__cuenta = tipo
        U.__saldo = balance
        U.__tar = tar

    def __str__(U):
        return f'''  
        Nombre: {U.__nombre}
        Tipo de cuenta: {U.__cuenta}
        su numero trasero de la tarjeta: {U.__tar}
        Su Sado disponible: {U.__saldo}
        '''
    
    def __repr__(U):
        return f"Usuario({U.__nombre}, {U.__cuenta}, {U.__saldo}, {U.__tar})"
    
    
    def Edo(U):

        print(f'''
            Su estado de cuenta es:
            {U.__saldo}
        ''')
    
    def get_data(U):
        return {
            "nombre": U.__nombre,
            "cuenta": U.__cuenta,
            "saldo": U.__saldo,
            "tar": U.__tar
        }
    
    def deposito(U):
        try:
            U.__saldo = U.__saldo + float(input("ingrese cuanto quiere depositar: "))
            U.Edo()
        except:
            print("debe ingresar un numero")
    
    def retiro(U):
        try:
            n = float(input("ingrese cuanto quiere Retirar: "))

            if n <= U.__saldo:
                U.__saldo = U.__saldo - n
                U.Edo()
            else:
                print("Saldo insuficiente!!!")
                U.Edo()
        except:
            print("debe ingresar un numero")

    def get_tar(U):
        return U.__tar


class UsuarioEncoder(json.JSONEncoder):
    def default(self, usr):
        if isinstance(usr, Usuario):
            return usr.get_data()
        return super().default(usr)
    

def usuario_decoder(usr):
    if "nombre" in usr and "cuenta" in usr and "saldo" in usr and "tar" in usr:
        return Usuario(usr["nombre"], usr["cuenta"], usr["saldo"], usr["tar"])
    return usr
    


# Base de datos predeterminada
BD = {

    "regVzl" : {
        "123" : Usuario("Fulanov", "Corriente", 2000.00, "63"),
        },

    "regpan" : {
        "456" : Usuario("Fulanop", "Ahorro", 1000.00, "45"),
    } 

}


# Funcion main (me gusta la estructura de C jaj)
def main():

    global BD
    n = 0
    band = Verificacion()

    while n != 4 and band:
        us = BD[pais][id_us]

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
            if (id_us in BD[pais].keys() and (BD[pais][id_us].get_tar() == tar_us)): # se verifica que los datos sean ciertos (converti el diccionario en lista para no usar el metodo keys xd)
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
        
            pais = naciones()
            
            bs = BD[pais]

            nombre = input("ingrese su nombre: ")

            if input(''' si quiere una cuenta de ahorro introduzca la letra 'H',
                    en caso contrario se le atribuira automaticamente una cuenta corriente...

                    responda para conrinuar ('H' para ahorro / cualquier otra tecla para corriente):
                ''').lower() == 'h':
                cuenta = "Ahorro"
            else:
                cuenta = "Corriente"
            saldo = 0.0
            tar = str(random.randint(10, 99))
            ID = str(random.randint(100, 999))

            while ID in bs.keys():
                ID = str(random.randint(100, 999))
            
            if input(f'''
                sus datos serian:
                    Nombre: {nombre}
                    Tipo de cuenta: {cuenta}
                    su numero trasero de la tarjeta: {tar}
                    Su ID para ingresar: {ID}
                    (acuerdese de los ultimos 2 datos que son importantes para ingresar)

                    ¿Esta de acuerdo con los datos? 'n' para No (repetir el proceso) / cualquier otra tecla para Si Y continuar
            ''').lower() == 'n':
                continue   
            else:
                bs[ID] = Usuario(nombre, cuenta, saldo, tar) # se guarda el Usuario en la base de datos
                with open('reg.json', 'wt') as f:
                    json.dump(BD, f, indent='\t', cls=UsuarioEncoder)
                print("Se ha registrado exitosamente")
                break
        
    

def naciones():
    pais = list(BD)[int(input('''¿Cual es su nacionalidad?
            1. Venezolana
            2. panameña
            ''')) - 1]
    return pais



def salir(base):
    global BD
    print("Hasta la proxima!!!")
    with open('reg.json', 'wt') as f:
        json.dump(BD, f, indent='\t', cls=UsuarioEncoder)


funcion = [registro, Usuario.Edo, Usuario.deposito, Usuario.retiro, salir]



if os.path.exists("reg.json"):
    with open('reg.json', 'rt') as f:
        BD = json.load(f, object_hook = usuario_decoder)




if __name__ == "__main__":
    main()


    



    