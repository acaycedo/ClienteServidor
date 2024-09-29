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
