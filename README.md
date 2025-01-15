# PDV PETS EM FOCO

Este é um projeto de **PDV (Ponto de Venda)** para o setor de **e-commerce de pets**, desenvolvido com Django. O sistema tem como objetivo gerenciar produtos, estoque e pedidos de uma loja de pets, permitindo uma experiência de compra eficiente e intuitiva.

## Funcionalidades

- **Cadastro de Produtos**: Gerencie os produtos da loja, incluindo nome, descrição, preço e código de barras.
- **Gestão de Estoque**: Controle de estoque em tempo real, com registros de entrada e saída de produtos.
- **Gestão de Pedidos**: Criação e controle de pedidos, com a possibilidade de atualizar o status de cada um.
- **Cadastro de Fornecedores**: Registre fornecedores de produtos para gerenciar o abastecimento da loja.
- **Integração com APIs de Pagamento**: Suporte para pagamento via **Stripe** e **Paypal**.
- **Interface de Administração em Django**: Painel administrativo baseado em **Bootstrap** para facilitar a gestão de produtos, estoque e pedidos.

## Tecnologias

- **Django**: Framework Python para desenvolvimento web.
- **PostgreSQL**: Banco de dados relacional para armazenar informações do sistema.
- **Docker**: Contêineres para facilitar a configuração e implantação do ambiente de desenvolvimento.
- **Stripe e Paypal APIs**: Integrações para processar pagamentos de forma segura.
- **Bootstrap**: Framework CSS para a construção de uma interface de administração responsiva.

## Como Começar

### 1. Clone o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/Jadson-Jose/pdv-pets-foco.git
```

### 2. Instale Dependências

Antes de executar o projeto, crie um ambiente virtual e instale as dependências:


cd pdv-pets-foco
python3 -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
pip install -r requirements.txt


### 3. Configure o Banco de Dados

O projeto utiliza o **PostgreSQL**. Certifique-se de ter o PostgreSQL instalado e configurado. Em seguida, crie o banco de dados e execute as migrações do Django:


python manage.py migrate


### 4. Crie um Superusuário

Para acessar o painel administrativo do Django, crie um superusuário:


python manage.py createsuperuser


### 5. Execute o Servidor de Desenvolvimento

Agora você pode executar o servidor de desenvolvimento:


python manage.py runserver


Acesse o aplicativo no navegador em: `http://127.0.0.1:8000/`

### 6. Acesse o Painel Administrativo

Você pode acessar o painel administrativo do Django em:


http://127.0.0.1:8000/admin


Faça login com o superusuário criado anteriormente.

## Estrutura do Projeto


pdv-pets-foco/
│</br>
├── core/  </br>              # Aplicativo principal do projeto
├── product/ </br>            # Gerenciamento de produtos
├── order/  </br>             # Gerenciamento de pedidos
├── supplier/            # Cadastro de fornecedores
├── templates/           # Templates HTML
├── static/              # Arquivos estáticos (CSS, JS, imagens)
├── manage.py            # Script principal do Django
└── requirements.txt     # Dependências do projeto



## Contribuições

Contribuições são bem-vindas! Para contribuir, siga as etapas abaixo:

1. Faça um fork do repositório.
2. Crie uma branch com a sua nova feature (`git checkout -b feature/nova-feature`).
3. Faça as modificações necessárias.
4. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
5. Faça o push para o seu fork (`git push origin feature/nova-feature`).
6. Abra um Pull Request explicando as mudanças.

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
