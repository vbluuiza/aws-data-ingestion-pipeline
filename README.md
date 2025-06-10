# 📦 Projeto: Pipeline de Ingestão de Dados na AWS (Camada Bronze)

Este é um projeto **acadêmico** com o objetivo de construir uma pipeline de ingestão de dados utilizando **AWS S3**, estruturando a **camada Bronze** de um Data Lake.

---

## 🎯 Objetivos do Projeto

Este projeto foi desenvolvido com o propósito de aplicar conceitos de Engenharia de Dados utilizando os principais serviços da AWS. Através de um fluxo simples e modular, busca-se representar a primeira etapa de um Data Lake.

- Construir uma pipeline de ingestão de dados baseada em arquivos CSV públicos
- Utilizar o Amazon S3 como destino da camada bronze
- Estruturar o Data Lake com o uso do AWS Lake Formation
- Modularizar o processo de extração, transformação e upload com boas práticas de código
- Consolidar o aprendizado sobre segurança e controle de acesso a dados na nuvem

---

## ✅ Funcionalidades implementadas

- `extract_data.py`: faz o download de arquivos CSV públicos e salva localmente.
- `load_dfs_by_year.py`: carrega e organiza arquivos `.csv` por ano em DataFrames.
- `upload_parquet.py`: converte DataFrames em Parquet (em memória) e envia para o S3.
- `setup_path.py`: adiciona o diretório raiz ao `sys.path` para facilitar os imports.
- Notebooks demonstrativos com a lógica de extração, transformação e upload.

---

## 📁 Estrutura de Diretórios

```bash
pipeline-aws-data-lake/
├── aws/                    # Sessão AWS e credenciais
├── config/                 # Setup de path e arquivos de configuração
├── data/
│   └── raw/                # Arquivos .csv baixados
├── notebooks/              # Notebooks de demonstração da lógica
├── s3_upload/              # Upload para S3 (Parquet)
├── scripts/                # Scripts de extração e pipeline
├── transform/              # Transformação dos dados
├── .env                    # Variáveis de ambiente (chaves AWS, bucket, etc.)
├── requirements.txt        # Dependências do projeto
└── README.md

```

---

## ☁️ Serviços AWS utilizados

☁️ **Serviços AWS utilizados**

- ✅ Amazon S3 (armazenamento dos dados na camada bronze)
- ✅ AWS Lake Formation (estruturação do Data Lake e controle de acesso)

---

## 🛠️ Stack utilizada

- `Python`
- `boto3`
- `pandas`
- `pyarrow`
- `python-dotenv`
- `requests`
- `os`, `pathlib.Path`, `io.BytesIO`

---

## 📔 Notebooks

Os notebooks presentes no diretório `notebooks/` têm propósito **demonstrativo**, explicando a lógica dos scripts principais e realizando alguns testes isolados. A execução oficial será realizada via scripts Python.

---

🚧 Este projeto ainda está em andamento e será atualizado conforme evolui com novas etapas e integrações à arquitetura de dados em nuvem.

---

👩‍💻 Desenvolvedora: [Luiza Vieira](https://www.linkedin.com/in/vbluuiza/)
