# Importa o módulo ou biblioteca OS (integra os progrmas e recursos do S.O)
import os
# Imprimindo o # 60 vezes
print('#' * 60)
# Criamos uma variável que vai receber do usuário um ip
ip_ou_host = input('Digite o ip ou host a ser verificado: ')
# Imprimindo o - 60 vezes
print('-' * 60)
# Chamando o método System da biblioteca OS
# -n número de pacotes (no caso 6)
os.system(f'ping -n 6 {ip_ou_host}')