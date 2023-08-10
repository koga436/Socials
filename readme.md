# Script de pesquisa de usuários

Este script em Python pesquisa usuários no LinkedIn, Facebook e Instagram com base em uma lista de e-mails e números de telefone fornecida em um arquivo CSV e gera uma lista com os resultados em um arquivo chamado `final.csv`.

## Requisitos

Para executar este script, você precisará ter o Python 3 instalado em seu computador. Além disso, você precisará instalar as seguintes bibliotecas Python:

- `instagram-private-api`
- `python-linkedin-v2`
- `facebook-sdk`

Você pode instalar essas bibliotecas executando o seguinte comando:

pip install instagram-private-api python-linkedin-v2 facebook-sdk


Além disso, você precisará fornecer suas credenciais do Instagram, LinkedIn e Facebook para autenticar suas solicitações às respectivas APIs. Você pode fazer isso editando as variáveis `INSTAGRAM_USERNAME`, `INSTAGRAM_PASSWORD`, `LINKEDIN_CONSUMER_KEY`, `LINKEDIN_CONSUMER_SECRET`, `LINKEDIN_USER_TOKEN`, `LINKEDIN_USER_SECRET`, `LINKEDIN_RETURN_URL` e `FACEBOOK_ACCESS_TOKEN` no início do script.

## Uso

Para usar este script, basta executá-lo a partir da linha de comando:

python socials.py

O script lerá a lista de e-mails e números de telefone do arquivo `emails_telefones.csv` e gerará uma lista com os resultados no arquivo `final.csv`. Certifique-se de que o arquivo `emails_telefones.csv` esteja no mesmo diretório que o script e que ele contenha duas colunas: a primeira coluna deve conter os endereços de e-mail e a segunda coluna deve conter os números de telefone.

## Licença

Este script é fornecido "como está" sem garantias ou condições de qualquer tipo. Você pode usá-lo e modificá-lo livremente para seus próprios propósitos.
