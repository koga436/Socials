import csv
import facebook
from instagram_private_api import (
    Client, ClientCompatPatch, ClientError, ClientLoginError
)
from linkedin_v2 import linkedin

# Inicialize suas credenciais do Instagram
INSTAGRAM_USERNAME = 'SEU_USUARIO'
INSTAGRAM_PASSWORD = 'SUA_SENHA'

# Inicialize suas credenciais do LinkedIn
LINKEDIN_CONSUMER_KEY = 'SEU_CONSUMER_KEY'
LINKEDIN_CONSUMER_SECRET = 'SEU_CONSUMER_SECRET'
LINKEDIN_USER_TOKEN = 'SEU_USER_TOKEN'
LINKEDIN_USER_SECRET = 'SEU_USER_SECRET'
LINKEDIN_RETURN_URL = 'SEU_RETURN_URL'

# Inicialize suas credenciais do Facebook
FACEBOOK_ACCESS_TOKEN = 'SEU_ACCESS_TOKEN'

# Crie uma instância da API do Instagram
instagram_api = Client(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

# Crie uma instância da API do LinkedIn
linkedin_authentication = linkedin.LinkedInDeveloperAuthentication(LINKEDIN_CONSUMER_KEY, LINKEDIN_CONSUMER_SECRET, LINKEDIN_USER_TOKEN, LINKEDIN_USER_SECRET, LINKEDIN_RETURN_URL, linkedin.PERMISSIONS.enums.values())
linkedin_application = linkedin.LinkedInApplication(linkedin_authentication)

# Crie uma instância da API do Facebook
facebook_graph = facebook.GraphAPI(FACEBOOK_ACCESS_TOKEN)

# Abra o arquivo CSV com a lista de e-mails e números de telefone
with open('emails_telefones.csv', 'r') as f:
    reader = csv.reader(f)
    emails_telefones = list(reader)

# Crie um arquivo CSV para armazenar os resultados
with open('final.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Email', 'Telefone', 'Username do Instagram', 'Nome do LinkedIn', 'Nome do Facebook'])

    # Pesquise usuários do Instagram, LinkedIn e Facebook com base nos e-mails e números de telefone
    for email_telefone in emails_telefones:
        email = email_telefone[0]
        telefone = email_telefone[1]
        instagram_username = None
        linkedin_name = None
        facebook_name = None

        # Pesquise usuários do Instagram com base no e-mail e número de telefone
        try:
            instagram_results = instagram_api.search_users(email)
            if not instagram_results.get('users'):
                instagram_results = instagram_api.search_users(telefone)
            for user in instagram_results.get('users', []):
                instagram_username = user['username']
                break
        except ClientError as e:
            print(e)

        # Pesquise usuários do LinkedIn com base no e-mail
        try:
            linkedin_results = linkedin_application.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': email})
            for profile in linkedin_results.get('people', {}).get('values', []):
                linkedin_name = profile['firstName'] + ' ' + profile['lastName']
                break
        except Exception as e:
            print(e)

        # Pesquise usuários do Facebook com base no e-mail
        try:
            facebook_results = facebook_graph.search(type='user', q=email)
            for user in facebook_results.get('data', []):
                facebook_name = user['name']
                break
        except facebook.GraphAPIError as e:
            print(e)

        writer.writerow([email, telefone, instagram_username, linkedin_name, facebook_name])
