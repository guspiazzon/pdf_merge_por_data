import os
import re
from datetime import datetime
from pypdf import PdfReader, PdfWriter
from pypdf.errors import PdfReadError
from dotenv import load_dotenv

def extrair_data(nome_arquivo):
    """
    Extrai a data do nome do arquivo, suportando formatos completos (AAAA-MM-DD) 
    ou parciais (AAAA-MM ou MM-AAAA).
    """
    # Procura por AAAA-MM-DD, DD-MM-AAAA ou apenas AAAA-MM / MM-AAAA
    match = re.search(r'(\d{4}[-_]\d{2}[-_]\d{2})|(\d{2}[-_]\d{2}[-_]\d{4})|(\d{4}[-_]\d{2})|(\d{2}[-_]\d{4})', nome_arquivo)
    
    if match:
        data_str = match.group(0).replace('_', '-')
        for fmt in ('%Y-%m-%d', '%d-%m-%Y', '%Y-%m', '%m-%Y'):
            try:
                return datetime.strptime(data_str, fmt)
            except ValueError:
                continue
                
    return datetime.min

def juntar_pdfs_por_data(diretorio_entrada, arquivo_saida):
    writer = PdfWriter()
    
    if not os.path.exists(diretorio_entrada):
        print(f"Erro: O diretório '{diretorio_entrada}' não foi encontrado.")
        return

    arquivos = [f for f in os.listdir(diretorio_entrada) if f.lower().endswith('.pdf')]
    
    if not arquivos:
        print("Nenhum arquivo PDF encontrado na pasta.")
        return

    arquivos_com_data = []
    for arq in arquivos:
        caminho_completo = os.path.join(diretorio_entrada, arq)
        data = extrair_data(arq)
        arquivos_com_data.append((data, caminho_completo, arq))
    
    # Ordena os arquivos por data (do mais antigo para o mais recente)
    arquivos_com_data.sort(key=lambda x: x[0])
    
    print("Ordem de mesclagem dos arquivos:")
    print("-" * 40)
    
    for data, caminho, nome in arquivos_com_data:
        if data != datetime.min:
            # Se for formato apenas mês/ano
            data_formatada = data.strftime('%m/%Y')
        else:
            data_formatada = "Data não identificada"
            
        print(f"-> {nome} (Data: {data_formatada})")
        
        try:
            reader = PdfReader(caminho)
            for page in reader.pages:
                writer.add_page(page)
        except PdfReadError as e:
            print(f"   [AVISO] O arquivo '{nome}' apresentou erro interno de estrutura e foi ignorado: {e}")
        except Exception as e:
            print(f"   [AVISO] Erro inesperado ao ler '{nome}': {e}")
        
    # Salva o arquivo final consolidado
    with open(arquivo_saida, 'wb') as f_out:
        writer.write(f_out)
        
    print("-" * 40)
    print(f"\nPDFs processados com sucesso no arquivo: **{arquivo_saida}**")

if __name__ == "__main__":
    # CONFIGURAÇÕES:
    load_dotenv()
    PASTA_ARQUIVOS = os.getenv("PASTA_PDF")
    PASTA_DOS_PDFS = PASTA_ARQUIVOS  # Pasta onde estão os seus PDFs originais
    NOME_ARQUIVO_FINAL = "resultado_ordenado.pdf" # Nome do PDF gerado
    
    juntar_pdfs_por_data(PASTA_DOS_PDFS, NOME_ARQUIVO_FINAL)

