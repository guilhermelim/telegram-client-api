<div>
    <h1 style="margin: 0; text-align: center;">Telegram Client API</h1>
    <p style="margin: 0; text-align: center;">
        <b>Uma api-restful simples e segura para criação de clientes do telegram.</b>
    </p>
    <p style="text-align: center; padding: 20px 0;">
        <img width="150" src="telegram_logo.svg" alt="telegram client api">
    </p>
</div>

##Descrição do Projeto

Esse projeto foi construído em [Python](https://www.python.org) com o objetivo de fornecer um conjunto de funções para construção de Clientes/Robôs personalizados do Telegram.

**Telegram APIs**
O TELEGRAM Oferece [dois tipos de APIs](https://core.telegram.org/api) para desenvolvedores. Você é bem-vindo para usar ambas as APIs gratuitamente.
1. [API do Bot](https://core.telegram.org/api#bot-api) permite criar facilmente programas que usam mensagens do Telegram para uma interface.
    **Vantagens:**
    1. ✅ Pode criar bots ilimitados com uma única conta do Telegram.
    2. ✅ API bem documentadas e robustas para diversas linguagens de programação.

    **Desvantagens**
    1. ❌ Não pode iniciar conversas com novos usuários sem atender determinadas requisitos. Ex: Usuário precisa falar primeiro com o seu robô para ser capaz de estabelecer diálogos.
    2. ❌ Não pode entrar, enviar, receber, responder e ler histórico de mensagens em grupos ou canais sem o consentimento do administrador. 

2. [API do Cliente](https://core.telegram.org/api#tdlib-build-your-own-telegram) permite que você construa seus próprios clientes personalizados do Telegram. 
    **Vantagens:**
    1. ✅ Possui todos os privilégios e capacidades de uma conta normal do telegram.
    2. ✅ Pode iniciar conversas com qualquer usuário sem restrições.
    3. ✅ Pode entrar, enviar, receber, responder e ler histórico de mensagens em grupos ou canais sem a necessidade de ser administrador.

    **Desvantagens**
    1. ❌ Só é possível criar um único bot por conta de usuário do Telegram.
    2. ❌ Não possui uma vasta quantidade de APIs de terceiros fazendo abstração da API Oficial para WEB, assim como também APIs de terceiros bem documentadas ou disponíveis para uma vasta quantidade de linguagens de programção.

Esse projeto utiliza a [API do Cliente do Telegram](https://core.telegram.org/api#tdlib-build-your-own-telegram) como base, tendo por objetivo resolver (2º desvantagem) o problema de acessibilidade a qualquer linguagem de programação (uma vez que disponível na WEB) e conceder uma API bem documentada e simples de utilizar.

Cumprimos nossa tarefa disponibilizando uma web API RESTFUL segura e simples de usar, abstraindo todas as funções da API OFICIAL para a WEB com endpoints preparados para receber e responder as interações em [JSON](https://www.json.org/json-en.html). Consulte o [wiki]() do repositório para mais informações sobre como iniciar um projeto e uma lista detalhada de endpoints da api e suas funções.

##Recomendações de Boas Praticas
- Utilize uma conta do telegram exclusiva para cada bot construído com essa API. **Isso evitará bugs indesejados.**

Essa API utiliza a sua conta pessoal do telegram para enviar, receber, ler e responder mensagens. É uma boa pratica utilizar uma conta do telegram separada de sua pessoal, criando uma conta exclusiva para cada bot construído com essa ferramenta. Você ainda terá que lhe dar com o inconveniente de ter que criar uma nova conta, possuir e cadastrar um novo números de telefone para cada robô que for criado com essa ferramenta, porém ganhara o privilegio de poder interagir com qualquer usuário, grupo ou canal do telegram sem nenhuma restrição.

##Requisitos

Para usar este bot, você precisará do seguinte:

- Python Versão >= 3.10
- [Poetry](https://github.com/python-poetry/poetry)
- git

#Início rápido
Antes de começar, certifique-se de criar suas credenciais de acesso a API do Telegram. [Crie um APP Telegram](my.telegram.org) e obtenha suas credenciais de acesso _API_ID_ e _API_HASH_.

**Execute os seguintes comandos**
```bash
git clone https://github.com/guilhermelim/telegram-client-api.git
cd telegram-client-api
cp .env.local .env              # Edite seu .env e insira suas credenciais API_ID e API_HASH.
poetry install --no-dev         # Instala todos os pacotes necessários do projeto
poetry run app                  # Executa o Projeto

# Na primeira execução é necessário fazer login em sua conta do Telegram.
# O bot irá criar um arquivo (anon.session) registrando a sua sessão de login. 
# Mantenha esse arquivo de seguro não permitindo o seu acesso a terceiros.

# 1 - Digite o seu número de telefone vinculado a sua conta Telegram. Exemplo: 5585912341234
# 2 - Você receberá um código acesso em seu aplicativo do telegram. Digite o código. Exemplo: 12345
```

# Poetry Comandos

**Criar novo Projeto**
```bash
poetry new nome_do_projeto
```

**Configura Poetry**
```bash
# gera o virtualenvs na pasta do projeto
poetry config virtualenvs.in-project true
```

**Cria a Virtual Env do Projeto**
```bash
# Cria uma virtual Env
poetry shell
# Cria uma virtual Env fiando a versão do Python
poetry env use 3.10.5
```

**Ativa a Virtual Env**
```bash
# Ativa e Acessa a virtual env do projeto
poetry shell                        # Note que é possível criar/acessar a virtualenv com o mesmo comando
```

**Adiciona Módulos/Pacotes**
```bash
poetry add nome_do_mudulo@latest    # Adiciona a ultima versão do pacote
poetry add nome_do_mudulo           # Adiciona o pacote
```

**Instala/Atualiza dependências do Projeto**
```bash
poetry install                      # instala/atualiza dependências do seu projeto (execute quando adicionar um novo pacote)
```

**Gera Build do Projeto tar.gz**
```bash
poetry build                        # A build será gerada dentro da pasta dist
```

**Exporta o Projeto para formato requirements.txt**
```bash
poetry export -o requirements.txt
```

**Publica a build**
```bash
poetry publish                        # A build será gerada dentro da pasta dist
```


##PRODUÇÃO
**Instalar Projeto em Produção**
```bash
# Instalação dentro de uma virtualenv (RECOMENDADO)
poetry install --no-dev
# Executa Projeto
poetry run app

# Instalação padrão do python
pip install --require-hashes -r requirements.txt
```