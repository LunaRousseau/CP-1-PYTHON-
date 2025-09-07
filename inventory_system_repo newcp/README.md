# Sistema de Gestão de Estoque (Inventário) - Entrega

**Instruções:** Este repositório contém um sistema em Python para cadastro de produtos e gestão de estoque conforme solicitado.

**ATENÇÃO:** Substitua os placeholders abaixo pelos nomes e RMs reais dos integrantes do grupo antes de enviar.

## Integrantes
- Luna Rousseau - RM: 564215
- NOME COMPLETO 2 - RM: 000000
- NOME COMPLETO 3 - RM: 000000

## Requisitos
- Python 3.8+
- (Opcional) criar um ambiente virtual: `python -m venv .venv` e ativar
- Instalar dependências (não há dependências externas obrigatórias): `pip install -r requirements.txt`

## Estrutura do projeto
```
inventory_system/
├─ main.py           # CLI principal
├─ products.py       # Classe Product e gerenciamento em memória
├─ storage.py        # Persistência em JSON
├─ utils.py          # Funções utilitárias (validação, alertas)
├─ README.md
├─ requirements.txt
└─ .gitignore
```

## Funcionalidades implementadas
1. Cadastro de Produtos
- Nome, código (único), categoria, quantidade, preço, descrição, fornecedor.

2. Gestão de Estoque
- Adicionar ao estoque (aumentar quantidade).
- Remover do estoque (reduzir quantidade).
- Atualização manual de quantidade.
- Alerta de estoque baixo quando quantidade atinge o limite mínimo (configurável por produto).

## Uso rápido (CLI)
Executar:
```bash
python main.py --help
```

Exemplos:
- `python main.py add --code P001 --name "Mouse" --category "eletronicos" --qty 10 --price 59.90 --supplier "ACME Ltda" --desc "Mouse USB"`
- `python main.py list`
- `python main.py add_stock --code P001 --qty 5`
- `python main.py remove_stock --code P001 --qty 3`
- `python main.py set_qty --code P001 --qty 20`
- `python main.py set_threshold --code P001 --threshold 5`

## Persistência
Os dados são salvos em `data/products.json` automaticamente.

## Como gerar o link do GitHub (passo a passo)
1. Crie um repositório no GitHub (por exemplo: `inventory-system`).
2. No terminal dentro da pasta do projeto:
```bash
git init
git add .
git commit -m "Entrega: sistema de gestão de estoque"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/NOME_REPO.git
git push -u origin main
```
3. Copie o link do repositório e entregue conforme solicitado.

---

Se desejar, eu já posso preencher os nomes e RMs se você me enviar — ou posso fazer o push para um repositório público **se você me der credenciais**, mas por segurança não recomendamos enviar credenciais. Melhor: eu entrego o zip e orientações e você faz o push.

Boa sorte na entrega!
