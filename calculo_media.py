import tkinter as tk

#Função para calcular a média de 4 números
def calcular_media():
    #Pegar numeros dos campos entry
    notas = [
    float(nota_1.get()),
    float(nota_2.get()),
    float(nota_3.get()),
    float(nota_4.get()),
    ]
    #Calcular a média
    media = sum(notas)/len(notas)
    #Mostrar o resultado
    if media <=5:
        media_final.config(text=f"Sua média final é: {media:.2f}" + "   " + "REPROVADO")
    else:
        media_final.config(text=f"Sua média final é: {media:.2f}" + "   " + "PARABÉNS. APROVADO")

# Criação da janela principal
root = tk.Tk()
root.geometry("700x500")
root.title("Cálculo de média")

#Para adicionar um widget na janela principal (root) você cria um objeto, e entre () o nome do objeto mestre. No caso a janela que chamamos de root

#Entries para os números
nota_1 = tk.Entry(root)
nota_2 = tk.Entry(root)
nota_3 = tk.Entry(root)
nota_4 = tk.Entry(root)

#Posicionar Entries na tela
nota_1.grid(row=0, column=0, padx=10, pady=5)
nota_2.grid(row=0, column=1, padx=10, pady=5)
nota_3.grid(row=0, column=2, padx=10, pady=5)
nota_4.grid(row=0, column=3, padx=10, pady=5)

#Botão para calcular a média
botao = tk.Button(root, text='Calcular média', command=calcular_media)
botao.grid(row=1, column=0, columnspan=4, pady=10)

#Label para mostrar o resultado
media_final = tk.Label(root, text="Média: ")
media_final.grid(row=2, column=0, columnspan=4, pady=10)

root.mainloop()






