import tkinter as tk
from tkinter import ttk

# Função para converter Celsius para Fahrenheit
def converter():
    try:
        celsius = float(entry_celsius.get())  # Pega o valor inserido no campo de entrada
        fahrenheit = (celsius * 9/5) + 32  # Conversão para Fahrenheit
        label_resultado.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        label_resultado.config(text="Entrada inválida")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Conversor de Temperatura")

# Estilo e tamanho da janela
janela.geometry("400x200")
janela.config(bg="#e6f2ff")

# Rótulo de título
label_titulo = tk.Label(janela, text="Conversor de Celsius para Fahrenheit", font=('Helvetica', 16, 'bold'), bg="#e6f2ff")
label_titulo.pack(pady=10)

# Frame para organizar os widgets
frame = tk.Frame(janela, bg="#e6f2ff")
frame.pack(pady=20)

# Campo de entrada para o valor em Celsius
entry_celsius = ttk.Entry(frame, font=('Helvetica', 14), width=10)
entry_celsius.grid(row=0, column=1, padx=10)

# Rótulo para indicar o campo de entrada
label_celsius = tk.Label(frame, text="°C", font=('Helvetica', 14), bg="#e6f2ff")
label_celsius.grid(row=0, column=2)

# Botão de conversão
botao_converter = ttk.Button(frame, text="Converter", command=converter)
botao_converter.grid(row=0, column=3, padx=10)

# Rótulo para mostrar o resultado
label_resultado = tk.Label(janela, text="", font=('Helvetica', 16), bg="#e6f2ff")
label_resultado.pack(pady=20)

# Loop da interface gráfica
janela.mainloop()