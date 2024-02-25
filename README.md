# Ping Checker Simples

Este script em Python realiza uma verificação básica de conectividade usando o comando `ping`. Ele permite que o usuário insira um endereço IP ou host a ser verificado. A biblioteca `os` é utilizada para executar o comando `ping` no terminal.

## Uso

1. Execute o script em um terminal ou prompt de comando.
2. Insira o endereço IP ou host que você deseja verificar quando solicitado.
3. O script executará o comando `ping` com 6 pacotes para o endereço fornecido.
4. O resultado do comando `ping` será exibido no terminal, mostrando a conectividade com o endereço IP ou host especificado.

## Executando o Script

```bash
python nome_do_script.py
```

## Exemplo de Saída

A saída do script mostrará o tempo de resposta de cada pacote enviado, indicando a conectividade com o endereço IP ou host.

## Observações

- O número de pacotes enviados é definido como 6 no exemplo. Se desejar ajustar esse número, você pode modificar o valor na linha que contém o comando `os.system`.

## Contribuições

Este é um script simples destinado a fins educacionais. Se desejar contribuir ou adicionar recursos mais avançados, sinta-se à vontade para fazer um fork e enviar uma solicitação pull.

**Nota:** Lembre-se de que a eficácia deste script pode variar dependendo do sistema operacional e configurações específicas. Este script é adequado para verificações básicas de conectividade.
