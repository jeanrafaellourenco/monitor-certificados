# Monitor de Certificados de Domínio

Este diretório contém o script `monitor_certificado.py`, que utiliza a API do [crt.sh](https://crt.sh/) para extrair subdomínios exclusivos associados a um domínio. Ele é útil para tarefas de segurança, como reconhecimento e monitoramento de certificados SSL/TLS.

## Recursos

- Faz consultas à API do crt.sh para obter informações sobre certificados.
- Extrai subdomínios exclusivos registrados nos certificados.
- Salva os subdomínios em um arquivo de saída.
- Possui sistema de re-tentativas em caso de falha.

## Dependências

Certifique-se de que o Python esteja instalado em seu sistema. As dependências estão listadas no arquivo `requirements.txt`. Para instalá-las, execute:

```bash
pip install -r requirements.txt
```

## Uso

### Executando o Script

1. Clone o repositório ou copie o script para o seu sistema.
2. Certifique-se de que todas as dependências estejam instaladas.
3. Execute o script utilizando o comando:

```bash
python monitor_certificado.py
```

4. Digite o nome do domínio e pressione enter.

### Saída

Os subdomínios exclusivos serão salvos em um arquivo chamado `DOMINIO_unique_urls.txt`, onde `DOMINIO` é o nome do domínio especificado.

## Configuração de Parâmetros

Os seguintes parâmetros podem ser configurados no script:

- `output_file`: Nome do arquivo de saída.
- `retries`: Número de tentativas em caso de falha.
- `delay`: Intervalo (em segundos) entre as tentativas.

## Exemplo

Suponha que o domínio configurado seja `example.com`. Após executar o script com sucesso, o arquivo `example.com_unique_urls.txt` conterá:

```
sub.example.com
www.example.com
api.example.com
```

## Tratamento de Erros

- Em caso de falha na requisição à API, o script tenta novamente até o número de tentativas configurado.
- Se a resposta JSON não puder ser decodificada, uma mensagem de erro será exibida.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

### Aviso

Este script destina-se a fins educativos e de segurança. Certifique-se de ter permissão para executar testes no domínio especificado.

