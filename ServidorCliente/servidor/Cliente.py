import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Clase del Cliente
class Cliente:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conectar al servidor
        try:
            self.sock.connect((self.host, self.port))
            print("Conectado al servidor")
        except Exception as e:
            print("No se pudo conectar al servidor:", e)
            messagebox.showerror("Error", "No se pudo conectar al servidor.")

        # Iniciar el hilo para recibir mensajes
        self.receive_thread = threading.Thread(target=self.recibir_mensajes)
        self.receive_thread.daemon = True  # Permite que el hilo se cierre al cerrar la aplicación
        self.receive_thread.start()

    def enviar_mensaje(self, mensaje):
        if mensaje:
            self.sock.send(mensaje.encode("UTF-8"))

    def recibir_mensajes(self):
        while True:
            try:
                reply = self.sock.recv(2048).decode("UTF-8")
                if reply:
                    app.agregar_mensaje(f"Servidor: {reply}")
            except Exception as e:
                print("Error al recibir mensaje:", e)
                break

# Clase de la Interfaz Gráfica
class App:
    def __init__(self, master):
        self.master = master
        master.title("Cliente Chat")

        # Campo para IP
        self.ip_label = tk.Label(master, text="IP del servidor:")
        self.ip_label.pack(pady=5)
        self.ip_entry = tk.Entry(master)
        self.ip_entry.pack(padx=10, pady=5)

        # Campo para puerto
        self.port_label = tk.Label(master, text="Puerto:")
        self.port_label.pack(pady=5)
        self.port_entry = tk.Entry(master)
        self.port_entry.pack(padx=10, pady=5)

        # Botón para conectar
        self.connect_button = tk.Button(master, text="Conectar", command=self.conectar)
        self.connect_button.pack(pady=10)

        # Área de chat
        self.chat_area = scrolledtext.ScrolledText(master, state='disabled')
        self.chat_area.pack(padx=10, pady=10)

        # Campo para mensajes
        self.entry = tk.Entry(master)
        self.entry.pack(padx=10, pady=5)
        self.entry.bind("<Return>", self.enviar_mensaje)

        # Botón para enviar mensajes
        self.enviar_button = tk.Button(master, text="Enviar", command=self.enviar_mensaje)
        self.enviar_button.pack(pady=5)

        self.cliente = None  # Inicialmente no hay cliente

    def conectar(self):
        host = self.ip_entry.get()
        port = self.port_entry.get()

        if not host or not port:
            messagebox.showwarning("Advertencia", "Por favor, ingrese la IP y el puerto.")
            return

        try:
            port = int(port)  # Convertir el puerto a un entero
            self.cliente = Cliente(host, port)
            self.ip_entry.config(state='disabled')
            self.port_entry.config(state='disabled')
            self.connect_button.config(state='disabled')  # Deshabilitar el botón de conexión
        except ValueError:
            messagebox.showerror("Error", "El puerto debe ser un número válido.")
        except Exception as e:
            print("Error al conectar:", e)

    def agregar_mensaje(self, mensaje):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, mensaje + '\n')
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)  # Desplaza hacia abajo

    def enviar_mensaje(self, event=None):
        mensaje = self.entry.get()
        if self.cliente:  # Verificar si hay un cliente conectado
            self.cliente.enviar_mensaje(mensaje)
            self.entry.delete(0, tk.END)  # Limpiar entrada

# Configuración de la ventana
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
