# cadastro_cliente

## Estrutura do Projeto

```plaintext
.
├── app.py                       # Script principal do Streamlit
├── controllers                        
│   ├── ClienteControllers.py    # Arquivo controle de execução do banco de dados 
├── JPTV                         # Diretório com arquivos das páginas
│   ├── Aplicastivos.py          # Página contendo as infomações de aplicativos para download
│   ├── gestor.py                # Página de execução da consulta, com edição e exclução de usuários
│   ├── inserir.py               # Página inicial para cadastro de usuários
│   ├── paineis.py               # Página com links e acessos aos paineis de servidores
├── models                       
│   ├── Cliente.py               # Arquivo configuração do banco de dados
├── services                    
│   ├── services.py              # Configuração e permissão ao banco de dados
│                
└── README.md                    # Descrição do projeto



## Visão Geral

O Projeto é uma aplicação web para cadastro e gerenciamento de usuarios de serviço, com vencimentos, desenvolvido em Streamlit e banco dados em SQL Server podendo exportar a base de dados em excel.

## Funcionalidades
- ** Cadastro de usuários **: Cadastro simples e intuitivo.
- ** Funções **: Cadastro, alteração e exclusão de clientes; Exportação da base de dados.

## Tecnologias Utilizadas:

- **Python**: Linguagem de programação principal.
- **Streamlit**: Framework para a criação de aplicações web interativas (Streamlit, version 1.29.0).
- ** Sql Server**: Banco de dados utilizado para armazar os dados

## Dependências

Este projeto utiliza as seguintes bibliotecas Python:

- **numpy**
- **pandas**
- **matplotlib**
- **seaborn**
- **streamlit**


Ideia do projeto

```bash
Nome:
Usuario:
Senha:
Serv:
vencimento:

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
