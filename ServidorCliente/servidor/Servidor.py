#librerias para necesarios

#Importa la libreria de sockets que son el punto final de la comunicacion entre dos maquinas.
#Se considera como el canal donde se permite enviar y recibir datos entre cliente servidor.
from socket import *

#Libreria de hilos que basicamente permiten la ejecucion de codigo simultaneo o multiples tareas mejorando eficiencia.
from _thread import *

#Libreia Time para colocar tiempos muertos entre el codigo. 
import time

#sys usado para manejar aspectos del sistema y el entorno de python.
import sys

#Funciones necesarias para comunicar cliente servidor y demas.

#ini función que pide la ip del servidor o el host, y el puerto del socket.
def ini():
    host = input("servidor: ")
    port = int(input("puerto: "))
    return host, port

# crearSocket() funcion que retorna un nuevo socket.
def crearSocket():
    #AF_INET establece que el socket usara address family version 4 o direcciones IPv4 que son las mas comunes.
    #SOCK_STREAM Establece que el socket sera de tipo stream es decir que utilizara el protocolo TCP garantizando la entrega en el orden correcto de los paquetes que continen los datos y sin perdidas.
    
    #s Sera la variable que instanceara un socket permitiendo las operaciones de red como enviar recibir y cerrar conexiones.
    return socket(AF_INET, SOCK_STREAM)

#ligarSocket(host,port) Funcion encargada de unir los datos que se tomaron para el puerto y la ip al socket creado.
def ligarSocket(s,host,port):
    while True:
        try:
            s.bind((host,port))
            break
        except error as e:
            print("Error no se encontraron datos para asociar",e)

#conexion(s) Funcion encargada de esperar la conexion de un cliente devolviendo una ip y un puerto del cliente.
def conexion(s):
    conn, addr = s.accept()
    print("\n Conexion Estrablecida. \n El cliente es: ",addr[0]+ ":" + str(addr[1]) + "\n")
    return conn, addr

#enviar(conn) Funcion que se encarga en enviar mensaje al cliente 1
def enviar(conn):
    while True:
        msg = input("Servidor: ")
        if msg.lower() == "salir":
            break
        try:
            conn.send(msg.encode("UTF_8"))
        except Exception as e:
            print("\nError al enviar el mensaje:", e)
            break
    
#recibir(conn) Funcion encargada de manejar los mensajes recibidos por cada cliente
#Esta funcion mientras el bucle no se rompa va seguir recibiendo los mensajes de los clientes

def recibir(conn):
    while True:
        try:
            #Recibe la conexion y se establece que no supere los 2048 bytes
            reply = conn.recv(2048)
            if not reply:  # Verifica si la conexión está cerrada
                print("El cliente se ha desconectado.")
                break
            reply = reply.decode("UTF_8")
            print("Cliente:", reply)
        except Exception as e:
            #Captura el error y determina si en caso de estar sin clientes bota el error
            print("\nNo puede recibirse respuesta:", e)
            break
        #En caso de error de perdida de conexion por ejemplo se establece un mensaje de espera.

#Funcion principal

def main():
    #llama la funcion ini para solicitar la ip y el puerto
    host, port = ini()
    #llama la funcion crearSoctek almacenandolo en la variable s
    s = crearSocket()
    #llama la funcion ligarSocket pasando como parametro s los datos obtenidos y ligandolos con el host y el port para que el servidor pueda recibir conexiones en esta direccion
    ligarSocket(s, host, port)
    #llama el metodo listen para habilitar las conexiones entrantes, el 2 estipula que solo se pueden mantener 2 conexiones en cola
    s.listen(2)
    
    #Una vez establecida la conexion el servidor estara en modo escucha
    print("\nEsperando por clientes.")

    #Condicion que permite ejecutar en bucle infinito hasta que se haga un cierre manual o mecanismo
    while True:
        #Llama la funcion conexion, pasando el socket por la variable s, Esta funcion espera hasta que un cliente se conecte
        #Almacena la conexion del socket del cliente en conn, y luego almacena la direccion ip del cliente en addr.
        conn, addr = conexion(s)
        #start_new_thread Inicia un nuevo hilo para manejar la recepcion de los mensajes entrantes
        #la funcion recibir se ejecutara en el nuevo hilo creado
        start_new_thread(recibir, (conn,))
        #Inicia un nuevo hilo pero para le manejo de los mensajes del cliente
        start_new_thread(enviar, (conn,))
        #El objetivo de las dos funciones es mantener las conversaciones en un hilo, y en caso de que entre una nueva conexion pueda manejarlo sin dificultad.
        #Siempre y cuando se respete la excepcion donde solo se puede mantener 2 conexiones.

#Ejecuta el main
if __name__ == "__main__":
    main()