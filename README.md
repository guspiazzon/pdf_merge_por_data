# pdf_merge_por_data
Automação em Python desenvolvida para ordenar e consolidar múltiplos arquivos PDF localizados em um diretório com base nas datas identificadas em seus nomes.


## 📌 Funcionalidades

- **Identificação Automática de Datas:** Extrai datas nos formatos `AAAA-MM-DD`, `DD-MM-AAAA`, `AAAA-MM` ou `MM-AAAA` (aceita hífens `-` ou underscores `_`).
- **Ordenação Cronológica:** Reordena os documentos do mais antigo para o mais recente antes de realizar a fusão.
- **Tratamento de Exceções:** Ignora arquivos corrompidos ou ilegíveis sem interromper o processamento da fila.
- **Segurança de Caminhos:** Configuração de diretórios via variáveis de ambiente (`.env`).

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **[pypdf]** — Manipulação e mesclagem de arquivos PDF.
- **[python-dotenv]** — Gerenciamento de variáveis de ambiente.

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python instalado na sua máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/pdf_merge_por_data.git](https://github.com/seu-usuario/pdf_merge_por_data.git)
   cd pdf_merge_por_data

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
  python -m venv venv
# No Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# No Linux/macOS:
source venv/bin/activate

3. **Instale as dependências:**
pip install -r requirements.txt


4. **Configure as variáveis de ambiente:**
Crie um arquivo .env na raiz do projeto com base no .env.example:
Snippet de código
PASTA_PDF=C:/caminho/para/sua/pasta_de_pdfs

5. **Execute o script:**
Bash
python main.py

O arquivo consolidado resultado_ordenado.pdf será gerado no diretório raiz da aplicação.
