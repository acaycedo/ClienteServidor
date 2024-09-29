# Proyecto de Cliente-Servidor en Python

Este proyecto implementa un sistema de comunicación cliente-servidor utilizando sockets en Python. El servidor puede manejar múltiples clientes de manera concurrente, permitiendo el intercambio de mensajes en tiempo real.

## Contenido

- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Cómo Ejecutar](#cómo-ejecutar)
- [Algoritmo del Servidor](#algoritmo-del-servidor)
- [Algoritmo del Cliente](#algoritmo-del-cliente)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Descripción

Este sistema permite que múltiples clientes se conecten a un servidor, envíen mensajes y reciban respuestas. El servidor gestiona las conexiones y puede enviar mensajes a clientes específicos.

## Requisitos

- Python 3.x
- Librerías estándar de Python (`socket`, `_thread`, `time`, `sys`)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/acaycedo/ClienteServidor.git
   cd https://github.com/acaycedo/ClienteServidor.git
Primero, inicia el servidor:
  python servidor.py
Luego, inicia el cliente en otra terminal:
  python cliente.py


Algoritmo del Servidor
   1 Configuración:
      El servidor solicita la IP y el puerto para escuchar conexiones.
      Creación del Socket:
   
         Se crea un socket utilizando AF_INET y SOCK_STREAM.
   
   Vinculación:
   
      Se vincula el socket a la IP y puerto especificados.
   
   Escucha de Conexiones:
   
      El servidor espera conexiones de los clientes.
   
   Aceptación de Clientes:
   
      Al aceptar un cliente, se crea un nuevo hilo para manejar la comunicación.
   
   Recepción de Mensajes:
   
      El servidor recibe mensajes de los clientes y los maneja según su lógica (enviar respuestas, gestionar desconexiones).
   
   Cierre de Conexiones:
   
      El servidor cierra las conexiones adecuadamente al finalizar.
   
Algoritmo del Cliente

   Configuración:

      El cliente solicita la IP y el puerto del servidor.
   Creación del Socket:
   
      Se crea un socket utilizando AF_INET y SOCK_STREAM.
   Conexión al Servidor:
   
      El cliente se conecta al servidor utilizando la IP y el puerto proporcionados.
   Recepción de Mensajes:
   
      Se inicia un hilo que escucha mensajes del servidor.
   Envío de Mensajes:
   
      El cliente permite al usuario enviar mensajes al servidor y gestionar la entrada de texto.
   Desconexión:
   
      El cliente cierra la conexión al escribir "salir".
