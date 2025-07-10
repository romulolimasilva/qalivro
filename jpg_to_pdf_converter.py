import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
import tkinter as tk
from tkinter import filedialog, messagebox

class ImageToPdfConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Conversor de JPG para PDF")
        self.window.geometry("400x200")
        self.setup_gui()

    def setup_gui(self):
        # Criando e configurando widgets
        self.label = tk.Label(self.window, text="Selecione as imagens JPG para converter em PDF")
        self.label.pack(pady=10)

        self.select_button = tk.Button(self.window, text="Selecionar Imagens", command=self.select_images)
        self.select_button.pack(pady=10)

        self.convert_button = tk.Button(self.window, text="Converter para PDF", command=self.convert_to_pdf)
        self.convert_button.pack(pady=10)

        self.selected_files = []

    def select_images(self):
        # Abre diálogo para selecionar arquivos
        files = filedialog.askopenfilenames(
            title="Selecione as imagens",
            filetypes=[("Arquivos JPG", "*.jpg;*.jpeg")]
        )
        self.selected_files = list(files)
        if self.selected_files:
            messagebox.showinfo("Sucesso", f"{len(self.selected_files)} imagens selecionadas")
        else:
            messagebox.showwarning("Aviso", "Nenhuma imagem selecionada")

    def convert_to_pdf(self):
        if not self.selected_files:
            messagebox.showerror("Erro", "Nenhuma imagem selecionada")
            return

        # Solicita local para salvar o PDF
        pdf_file = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("Arquivos PDF", "*.pdf")]
        )

        if not pdf_file:
            return

        try:
            # Cria o PDF
            c = canvas.Canvas(pdf_file, pagesize=A4)
            
            for image_path in self.selected_files:
                # Abre a imagem
                img = Image.open(image_path)
                
                # Obtém as dimensões da imagem
                img_width, img_height = img.size
                
                # Calcula a escala para ajustar a imagem na página A4
                aspect = img_height / float(img_width)
                
                # Define largura máxima como 540 (tamanho do A4 com margens)
                max_width = 540
                width = max_width
                height = width * aspect
                
                # Se a altura for maior que o permitido, ajusta proporcionalmente
                if height > 720:  # altura máxima do A4 com margens
                    height = 720
                    width = height / aspect
                
                # Adiciona a imagem ao PDF
                c.drawImage(image_path, 
                          (A4[0] - width) / 2,  # centraliza horizontalmente
                          (A4[1] - height) / 2,  # centraliza verticalmente
                          width=width, 
                          height=height)
                
                c.showPage()
            
            c.save()
            messagebox.showinfo("Sucesso", "PDF criado com sucesso!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar PDF: {str(e)}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    converter = ImageToPdfConverter()
    converter.run()
