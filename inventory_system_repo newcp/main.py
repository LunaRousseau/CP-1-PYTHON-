import argparse
from products import ProductManager
from storage import Storage
from utils import format_currency

DATA_FILE = "data/products.json"

def main():
    parser = argparse.ArgumentParser(description="Sistema de Gestão de Estoque")
    sub = parser.add_subparsers(dest="cmd")

    # add product
    p_add = sub.add_parser("add", help="Adicionar novo produto")
    p_add.add_argument("--code", required=True)
    p_add.add_argument("--name", required=True)
    p_add.add_argument("--category", required=True)
    p_add.add_argument("--qty", type=int, default=0)
    p_add.add_argument("--price", type=float, default=0.0)
    p_add.add_argument("--supplier", default="")
    p_add.add_argument("--desc", default="")
    p_add.add_argument("--threshold", type=int, default=5)

    p_list = sub.add_parser("list", help="Listar produtos")

    p_addstock = sub.add_parser("add_stock", help="Adicionar quantidade ao estoque")
    p_addstock.add_argument("--code", required=True)
    p_addstock.add_argument("--qty", type=int, required=True)

    p_removestock = sub.add_parser("remove_stock", help="Remover quantidade do estoque")
    p_removestock.add_argument("--code", required=True)
    p_removestock.add_argument("--qty", type=int, required=True)

    p_setqty = sub.add_parser("set_qty", help="Ajustar quantidade manualmente")
    p_setqty.add_argument("--code", required=True)
    p_setqty.add_argument("--qty", type=int, required=True)

    p_setthr = sub.add_parser("set_threshold", help="Configurar alerta de estoque baixo")
    p_setthr.add_argument("--code", required=True)
    p_setthr.add_argument("--threshold", type=int, required=True)

    args = parser.parse_args()
    storage = Storage(DATA_FILE)
    pm = ProductManager(storage.load())

    if args.cmd == "add":
        pm.add_product(code=args.code, name=args.name, category=args.category,
                       qty=args.qty, price=args.price, supplier=args.supplier,
                       description=args.desc, threshold=args.threshold)
        storage.save(pm.to_list())
        print(f"Produto {args.code} adicionado.")
    elif args.cmd == "list":
        for p in pm.list_products():
            print(f"{p['code']} - {p['name']} | {p['category']} | Qtd: {p['qty']} | Preço: {format_currency(p['price'])} | Fornecedor: {p.get('supplier','')}")
    elif args.cmd == "add_stock":
        pm.add_stock(args.code, args.qty)
        storage.save(pm.to_list())
        print("Estoque atualizado.")
    elif args.cmd == "remove_stock":
        pm.remove_stock(args.code, args.qty)
        storage.save(pm.to_list())
        print("Estoque atualizado.")
    elif args.cmd == "set_qty":
        pm.set_quantity(args.code, args.qty)
        storage.save(pm.to_list())
        print("Quantidade ajustada.")
    elif args.cmd == "set_threshold":
        pm.set_threshold(args.code, args.threshold)
        storage.save(pm.to_list())
        print("Threshold atualizado.")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
