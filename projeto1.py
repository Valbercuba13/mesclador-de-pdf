import PyPDF2
import os

pasta_arquivos = "arquivos"
pasta_mesclados = "mesclados"

merger = PyPDF2.PdfMerger()

lista_arquivos = [arquivo for arquivo in os.listdir(pasta_arquivos) if arquivo.lower().endswith('.pdf')]
lista_arquivos.sort()

pdfs_adicionados = set()

for idx, arquivo in enumerate(lista_arquivos):
    nome_base = os.path.splitext(arquivo)[0]  
    novo_nome = f"NewPdf{idx+1:02d}.pdf"  # para poder gerar os nomes em sequencia ex 01,02,03...

    pdfs_adicionados.add(novo_nome)
    merger.append(os.path.join(pasta_arquivos, arquivo))

caminho_saida = os.path.join(pasta_mesclados, novo_nome)
with open(caminho_saida, "wb") as output_file:
    merger.write(output_file)

merger.close()
