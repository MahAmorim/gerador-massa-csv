import csv
import random
import unicodedata
from datetime import datetime, timedelta
from faker import Faker
import argparse
import os

__version__ = "1.0.0"
__author__ = "Marcela Amorim"

# Instância do Faker com localização brasileira
fake = Faker('pt_BR')

# Função para remover acentos e colocar em MAIÚSCULO
def limpar_nome(nome):
    return unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('utf-8').upper()

# Geração de CPF único e válido
def gerar_cpf_unico(cpfs_existentes):
    def calcular_digito(digs):
        soma = sum([v * (len(digs)+1-i) for i, v in enumerate(digs)])
        d = 11 - soma % 11
        return d if d < 10 else 0

    while True:
        n = [random.randint(0, 9) for _ in range(9)]
        n.append(calcular_digito(n))
        n.append(calcular_digito(n))
        cpf = ''.join(map(str, n))
        if cpf not in cpfs_existentes:
            cpfs_existentes.add(cpf)
            return cpf

# Geração de data no formato DDMMAAAA entre 18 e 70 anos
def gerar_data_nascimento():
    hoje = datetime.today()
    idade = random.randint(18, 70)
    nascimento = hoje - timedelta(days=idade * 365 + random.randint(0, 364))
    return nascimento.strftime('%d%m%Y')

# Geração da lista de registros
def gerar_dados(qtd):
    dados = []
    cpfs_gerados = set()
    for _ in range(qtd):
        nome = limpar_nome(fake.first_name())
        cpf = gerar_cpf_unico(cpfs_gerados)
        nascimento = gerar_data_nascimento()
        status = "ACTIVE"
        dados.append([nome, cpf, nascimento, status])
    return dados

# Salva no CSV
def salvar_csv(nome_arquivo, dados):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["UserName", "UserCPF", "UserBirthDate", "UserStatus"])
        writer.writerows(dados)

# Execução principal com argparse
def main():
    parser = argparse.ArgumentParser(description="Gerador de CSV para testes com dados de registro.")
    parser.add_argument('--qtd', type=int, default=100, help="Quantidade de registros a gerar")
    parser.add_argument('--out', type=str, default='users.csv', help="Nome do arquivo CSV de saída")
    args = parser.parse_args()

    # Garante que a pasta /data existe
    pasta_saida = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    os.makedirs(pasta_saida, exist_ok=True)
    caminho_completo = os.path.join(pasta_saida, args.out)

    dados = gerar_dados(args.qtd)

    # Mostrar preview dos primeiros 5 registros
    print("\n🔎 Preview dos primeiros registros gerados:")
    for linha in dados[:5]:
        print(f"  - {linha}")

    salvar_csv(caminho_completo, dados)
    print(f"\n✅ Arquivo '{caminho_completo}' gerado com {args.qtd} registros.")

if __name__ == "__main__":
    main()