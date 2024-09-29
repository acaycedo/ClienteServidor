#Importa la libreria de sockets que son el punto final de la comunicacion entre dos maquinas.
#Se considera como el canal donde se permite enviar y recibir datos entre cliente servidor.
import socket
#Libreria de hilos que basicamente permiten la ejecucion de codigo simultaneo o multiples tareas mejorando eficiencia.
import threading

# Función para recibir mensajes del servidor
def recibir_mensajes(conn):
    while True:
        try:
            #Intentara ricibir hasta 2048 bytes de datos del cliente y luego transforma los bytes en una cadena de texto UTF_8
            mensaje = conn.recv(2048).decode("UTF_8")

            #Si mensaje tiene contenido
            if mensaje:
                #tratara de formatear la cadena para mostrar que es mensaje del servidor
                print(f"\nServidor: {mensaje}")
            else:   
                break
        except:
            #En caso de no recibir mensaje imprime
            print("\nError al recibir el mensaje.")
            break

# Función principal del cliente
def main():
    # Configuración del cliente
    # En este apartado se encargara de que el cliente ingrese los datos del host
    host = input("Ingrese la IP del servidor: ")
    port = int(input("Ingrese el puerto: "))

    # Crear un socket
    # AF_INET establece que el socket usara address family version 4 o direcciones IPv4 que son las mas comunes.
    # SOCK_STREAM Establece que el socket sera de tipo stream es decir que utilizara el protocolo TCP garantizando la entrega en el orden correcto de los paquetes que continen los datos y sin perdidas.
    
    # Se utiliza socket.socket para crear una interfaz u objeto para la comunicación en la red
    # Luego indicamos que socket usara esos dos parametros ya que los establecimos en el servidor
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Se usa el try para capturar alguna excepcion en caso de fallo
    try:
        # Conectar al servidor
        # Intentara conectarse al servidor usando los parametros ingresados
        conn.connect((host, port))
        # Mensaje de Exito
        print("Conectado al servidor.")

        # Iniciar hilo para recibir mensajes
        # Cuando inicie el hilo establecido con el servidor llamara la funcion recibir_mensajes
        # Pasando conn como argumento
        # y daemon usado para que en caso de se cierre el hilo finalice automaticamente

        threading.Thread(target=recibir_mensajes, args=(conn,), daemon=True).start()

        # Bucle para que el usuario le permite enviar mensajes 
        # y en caso de finalizar la conversacion solo debe escribir la palabra salir
        # se pasa como parametro lower, para evitar errores de usuario
        while True:
            # Enviar mensaje al servidor
            mensaje = input("Cliente: ")
            if mensaje.lower() == "salir":
                break
            conn.send(mensaje.encode("UTF_8"))
            # Excepcion que captura elgun error que pase durante la conexion
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        # Este bloque se encarga de cerrar el socket dependiendo si hubo un error o no con el fin de notificar al usuario si exite un error o no.
    finally:
        conn.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    main()
