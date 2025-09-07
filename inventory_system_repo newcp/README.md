# Sistema de Gestão de Estoque (Inventário) - Entrega


## Integrantes
- Luna Rousseau - RM: 564215


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

