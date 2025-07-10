# 🧪 Gerador de Massa de Dados em CSV

Gere arquivos `.csv` com dados fictícios de forma rápida e personalizável para uso em testes funcionais, de carga ou integração.

Ideal para ferramentas como **SoapUI**, **k6**, **JMeter**, **Taurus** e **Postman**.


## 📦 O que o script gera

Um arquivo `CSV` com as seguintes colunas:

| Campo          | Descrição                                |
|----------------|-------------------------------------------|
| UserName     | Nome em maiúsculo, sem acento             |
| UserCPF      | CPF válido e único, sem pontuação         |
| UserBirthDate      | Data de nascimento no formato `DDMMAAAA`  |
| UserStatus   | Sempre `ACTIVE`                           |

Exemplo:

```
UserName,UserCPF,UserBirthDate,UserStatus
ISAQUE,08348013881,19051962,ACTIVE
YASMIN,81398859834,09052003,ACTIVE
```


## 🗂 Estrutura do Projeto
```
.
├── data/                  # Onde os arquivos CSV gerados são salvos
│   └── massa.csv
│
├── src/                   # Código-fonte do gerador de massa
│   └── gerar_csv.py       # Script principal
│
├── .gitignore             # Arquivos/pastas ignorados pelo Git
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```
⚠️ Obs: Se você optar por outro nome além de src/, como massadata/, é só ajustar o nome aqui também.



## 🚀 Como usar

### 1. Clone ou baixe este repositório

```bash
git clone https://github.com/MahAmorim/gerador-massa-csv
cd gerador-massa-csv
```

### 2. Crie o ambiente virtual

```bash
python3 -m venv .venv
```

Ative o ambiente:

- **Windows PowerShell:**  
  `.\.venv\Scripts\Activate`

- **Git Bash:**  
  `source .venv/Scripts/activate`

- **Linux/macOS:**  
  `source .venv/bin/activate`

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install faker
```

## ⚙️ Executando o gerador

```bash
python src/gerar_csv.py --qtd 500 --out data/massa_500.csv
```

- `--qtd`: Quantidade de registros a gerar (padrão: 100)
- `--out`: Nome do arquivo de saída (padrão: `users.csv`)


## 💡 Requisitos

- Python 3.7+
- Biblioteca `Faker` (para geração de nomes)

## 🛠 Aplicações possíveis

- Testes com **SoapUI** usando DataSource CSV
- Simulações de carga com **k6**, **JMeter** ou **Taurus**
- Preenchimento de massa para ambientes de desenvolvimento e staging
- Mocks em APIs SOAP ou REST

## 🧰 Tecnologias utilizadas

Este projeto foi desenvolvido com foco em simplicidade, portabilidade e integração com ferramentas de teste. As principais tecnologias utilizadas são:

- [**Python 3.7+**](https://www.python.org/) — linguagem principal do script
- [**Faker**](https://faker.readthedocs.io/en/master/) — biblioteca para geração de dados fictícios realistas (nomes, CPFs, datas)
- [**argparse**](https://docs.python.org/3/library/argparse.html) — módulo nativo para criação de interface de linha de comando (CLI)
- [**UTF-8**](https://en.wikipedia.org/wiki/UTF-8) — codificação padrão para garantir compatibilidade internacional de caracteres

> 💡 O script é leve, sem dependências desnecessárias, e pode ser executado em qualquer sistema com Python instalado.

## ⚠️ Importante: sobrescrita de arquivos

Se o arquivo passado com `--out` já existir, ele será **sobrescrito automaticamente** sem aviso.

Exemplo:

```bash
python gerar_csv.py --qtd 5 --out massa_5.csv
```

Rodar esse comando duas vezes seguidas irá **substituir** o conteúdo do arquivo `massa_5.csv`.

> Para evitar perdas, escolha nomes diferentes ou faça backup dos arquivos antes de executar novamente.

## 🤝 Contribuindo

Quer contribuir com melhorias, correções ou novas ideias? Veja o [CONTRIBUTING.md](CONTRIBUTING.md) para orientações.

## 📄 Licença

Este projeto é de uso livre para fins de teste e aprendizado.
