from tkinter import *
from tkinter import ttk, messagebox

class HelpWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("📚 Manual de Usuario - RSA")
        self.geometry("800x600")
        self.configure(bg='#2C3E50')

        # Crear un canvas con scrollbar
        canvas = Canvas(self, bg='#2C3E50')
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg='#2C3E50')

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Título principal
        Label(scrollable_frame,
              text="🔐 Sistema de Cifrado RSA",
              font=('Roboto', 20, 'bold'),
              fg='#ECF0F1',
              bg='#2C3E50').pack(pady=20)

        # Contenido de ayuda
        help_text = """
        FUNDAMENTOS DEL RSA
        ━━━━━━━━━━━━━━━━━━━━━
        RSA es un algoritmo de cifrado asimétrico que utiliza un par de claves:
        • Clave Pública: Para cifrar mensajes
        • Clave Privada: Para descifrar mensajes

        PASOS DEL ALGORITMO
        ━━━━━━━━━━━━━━━━━━━
        🔑 Generación de Claves:
        • Seleccionar dos números primos (p y q)
        • Calcular n = p × q
        • Calcular φ(n) = (p-1) × (q-1)
        • Elegir e (exponente público)
        • Calcular d (exponente privado)

        USO DEL SISTEMA
        ━━━━━━━━━━━━━━━
        1. Generación de Claves:
           📝 Ingrese dos números primos en los campos p y q
           🔄 Haga clic en 'Generar Claves'
           ✅ El sistema mostrará las claves generadas

        2. Proceso de Cifrado:
           📝 Escriba su mensaje en el campo correspondiente
           🔒 Presione 'Cifrar'
           ✅ El mensaje cifrado aparecerá en el área de resultado

        3. Proceso de Descifrado:
           📝 Ingrese el mensaje cifrado
           🔓 Presione 'Descifrar'
           ✅ El mensaje original aparecerá en el área de resultado

        RECOMENDACIONES DE SEGURIDAD
        ━━━━━━━━━━━━━━━━━━━━━━━━━━
        • ⚠️ Use números primos grandes para mayor seguridad
        • 🔒 Mantenga su clave privada en secreto
        • 🔄 Cambie sus claves periódicamente
        • ⚡ No comparta información sensible sin cifrar

        EJEMPLO PRÁCTICO
        ━━━━━━━━━━━━━━━━
        Números primos sugeridos para pruebas:
        • p = 61
        • q = 53
        """

        # Crear el texto con formato
        text_widget = Text(scrollable_frame,
                          wrap=WORD,
                          width=70,
                          height=30,
                          font=('Consolas', 11),
                          bg='#34495E',
                          fg='#ECF0F1',
                          padx=15,
                          pady=15)
        text_widget.insert(INSERT, help_text)
        text_widget.configure(state='disabled')
        text_widget.pack(padx=20, pady=10)

        # Botón de cerrar
        Button(scrollable_frame,
               text="❌ Cerrar",
               command=self.destroy,
               font=('Roboto', 12, 'bold'),
               bg='#E74C3C',
               fg='white',
               activebackground='#C0392B',
               padx=20,
               pady=10).pack(pady=20)

        # Empaquetar canvas y scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")