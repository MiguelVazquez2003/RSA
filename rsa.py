import random
from tkinter import *
from tkinter import ttk, messagebox
import time

from ayuda import HelpWindow


class RSAGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cifrado RSA")
        self.root.geometry("800x900")
        self.root.configure(bg='#2C3E50')

        # Variables de clase
        self.claves = None

        # Título principal con icono
        title_frame = Frame(root, bg='#2C3E50')
        title_frame.pack(fill=X, pady=20)

        title_label = Label(title_frame,
                          text="🔐 Sistema de Cifrado RSA",
                          font=('Roboto', 24, 'bold'),
                          fg='#ECF0F1',
                          bg='#2C3E50')
        title_label.pack()
        # Botón de ayuda
        help_button = Button(root, text="Ayuda", command=self.show_help, font=('Roboto', 12, 'bold'), bg='#3498DB', fg='white', activebackground='#2980B9')
        help_button.pack(pady=10)


        # Marco principal con scroll
        self.main_canvas = Canvas(root, bg='#2C3E50')
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.main_canvas.yview)
        self.scrollable_frame = Frame(self.main_canvas, bg='#2C3E50')

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.main_canvas.configure(
                scrollregion=self.main_canvas.bbox("all")
            )
        )

        self.main_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.main_canvas.configure(yscrollcommand=scrollbar.set)

        self.main_canvas.pack(side="left", fill="both", expand=True, padx=20)
        scrollbar.pack(side="right", fill="y")

        # Crear secciones
        self.create_key_generation_section(self.scrollable_frame)
        self.create_encryption_section(self.scrollable_frame)
        self.create_decryption_section(self.scrollable_frame)
    def show_help(self):
        self.help_window = HelpWindow(self.root)

    def create_key_generation_section(self, parent):
        key_frame = LabelFrame(parent,
                             text=" 🔑 Generación de Claves ",
                             font=('Roboto', 14, 'bold'),
                             bg='#34495E',
                             fg='#ECF0F1',
                             pady=10)
        key_frame.pack(fill=X, pady=10)

        input_frame = Frame(key_frame, bg='#34495E')
        input_frame.pack(fill=X, padx=10, pady=10)

        Label(input_frame, text="Número primo p:",
              bg='#34495E', fg='#ECF0F1',
              font=('Roboto', 12)).grid(row=0, column=0, padx=5, pady=5)
        self.entry_p = Entry(input_frame, font=('Roboto', 12), bg='#ECF0F1')
        self.entry_p.grid(row=0, column=1, padx=5, pady=5)

        Label(input_frame, text="Número primo q:",
              bg='#34495E', fg='#ECF0F1',
              font=('Roboto', 12)).grid(row=0, column=2, padx=5, pady=5)
        self.entry_q = Entry(input_frame, font=('Roboto', 12), bg='#ECF0F1')
        self.entry_q.grid(row=0, column=3, padx=5, pady=5)

        Button(key_frame,
               text="🔄 Generar Claves",
               command=self.generar_claves_evento,
               font=('Roboto', 12, 'bold'),
               bg='#3498DB',
               fg='white',
               activebackground='#2980B9').pack(pady=10)

        self.text_claves = Text(key_frame,
                               height=4,
                               font=('Consolas', 12),
                               bg='#ECF0F1',
                               fg='#2C3E50')
        self.text_claves.pack(fill=X, padx=10, pady=5)

    def create_encryption_section(self, parent):
        enc_frame = LabelFrame(parent,
                             text=" 🔒 Cifrado ",
                             font=('Roboto', 14, 'bold'),
                             bg='#34495E',
                             fg='#ECF0F1',
                             pady=10)
        enc_frame.pack(fill=X, pady=10)

        Label(enc_frame,
              text="Mensaje a cifrar:",
              bg='#34495E',
              fg='#ECF0F1',
              font=('Roboto', 12)).pack(anchor=W, padx=10, pady=5)

        self.entry_mensaje = Entry(enc_frame,
                                 font=('Roboto', 12),
                                 bg='#ECF0F1')
        self.entry_mensaje.pack(fill=X, padx=10, pady=5)

        Button(enc_frame,
               text="🔒 Cifrar",
               command=self.cifrar_evento,
               font=('Roboto', 12, 'bold'),
               bg='#2ECC71',
               fg='white',
               activebackground='#27AE60').pack(pady=10)

        self.text_cifrado = Text(enc_frame,
                                height=4,
                                font=('Consolas', 12),
                                bg='#ECF0F1',
                                fg='#2C3E50')
        self.text_cifrado.pack(fill=X, padx=10, pady=5)

    def create_decryption_section(self, parent):
        dec_frame = LabelFrame(parent,
                             text=" 🔓 Descifrado ",
                             font=('Roboto', 14, 'bold'),
                             bg='#34495E',
                             fg='#ECF0F1',
                             pady=10)
        dec_frame.pack(fill=X, pady=10)

        Label(dec_frame,
              text="Mensaje cifrado:",
              bg='#34495E',
              fg='#ECF0F1',
              font=('Roboto', 12)).pack(anchor=W, padx=10, pady=5)

        self.entry_mensaje_cifrado = Entry(dec_frame,
                                         font=('Roboto', 12),
                                         bg='#ECF0F1')
        self.entry_mensaje_cifrado.pack(fill=X, padx=10, pady=5)

        Button(dec_frame,
               text="🔓 Descifrar",
               command=self.descifrar_evento,
               font=('Roboto', 12, 'bold'),
               bg='#E74C3C',
               fg='white',
               activebackground='#C0392B').pack(pady=10)

        # Etiqueta para el resultado del descifrado
        Label(dec_frame,
              text="Mensaje descifrado:",
              bg='#34495E',
              fg='#ECF0F1',
              font=('Roboto', 12)).pack(anchor=W, padx=10, pady=5)

        self.text_descifrado = Text(dec_frame,
                                  height=4,
                                  font=('Consolas', 12),
                                  bg='#ECF0F1',
                                  fg='#2C3E50')
        self.text_descifrado.pack(fill=X, padx=10, pady=5)

    def generar_claves_evento(self):
        try:
            p = int(self.entry_p.get())
            q = int(self.entry_q.get())
            self.text_claves.delete(1.0, END)
            self.text_claves.insert(END, "⏳ Generando claves, por favor espere...\n")
            self.root.update()
            time.sleep(1)

            self.claves = generar_claves(p, q)
            self.text_claves.delete(1.0, END)
            self.text_claves.insert(END, f"🔑 Clave pública: {self.claves[0]}\n")
            self.text_claves.insert(END, f"🔑 Clave privada: {self.claves[1]}")
            messagebox.showinfo("Éxito", "¡Claves generadas correctamente!")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números primos válidos")

    def cifrar_evento(self):
        if not self.claves:
            messagebox.showerror("Error", "Primero debe generar las claves")
            return
        try:
            mensaje = self.entry_mensaje.get()
            self.text_cifrado.delete(1.0, END)
            self.text_cifrado.insert(END, "⏳ Cifrando el mensaje, por favor espere...\n")
            self.root.update()
            time.sleep(1)

            mensaje_cifrado = cifrar(self.claves[0], mensaje)
            self.text_cifrado.delete(1.0, END)
            self.text_cifrado.insert(END, f"🔒 Mensaje cifrado:\n{mensaje_cifrado}")
            messagebox.showinfo("Éxito", "¡Mensaje cifrado correctamente!")
        except:
            messagebox.showerror("Error", "Error al cifrar el mensaje")

    def descifrar_evento(self):
        if not self.claves:
            messagebox.showerror("Error", "Primero debe generar las claves")
            return
        try:
            mensaje_cifrado = eval(self.entry_mensaje_cifrado.get())
            self.text_descifrado.delete(1.0, END)
            self.text_descifrado.insert(END, "⏳ Descifrando el mensaje, por favor espere...\n")
            self.root.update()
            time.sleep(1)

            mensaje_descifrado = descifrar(self.claves[1], mensaje_cifrado)
            self.text_descifrado.delete(1.0, END)
            self.text_descifrado.insert(END, f"🔓 Mensaje descifrado:\n{mensaje_descifrado}")
            messagebox.showinfo("Éxito", "¡Mensaje descifrado correctamente!")
        except:
            messagebox.showerror("Error", "Error al descifrar el mensaje")

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def inverso_modular(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generar_claves(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = mcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = mcd(e, phi)
    d = inverso_modular(e, phi)
    return ((e, n), (d, n))

def cifrar(clave_publica, mensaje):
    clave, n = clave_publica
    cifrado = [(ord(char) ** clave) % n for char in mensaje]
    return cifrado

def descifrar(clave_privada, mensaje_cifrado):
    clave, n = clave_privada
    descifrado = [chr((char ** clave) % n) for char in mensaje_cifrado]
    return ''.join(descifrado)



if __name__ == "__main__":
    root = Tk()
    root.configure(bg='#2C3E50')
    app = RSAGUI(root)
    root.mainloop()
