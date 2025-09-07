import copy
from utils import low_stock_alert

class ProductManager:
    def __init__(self, products=None):
        self.products = products or []

    def _find(self, code):
        for p in self.products:
            if p['code'] == code:
                return p
        return None

    def add_product(self, code, name, category, qty=0, price=0.0, supplier='', description='', threshold=5):
        if self._find(code):
            raise ValueError(f'Código {code} já existe.')
        prod = {
            'code': code,
            'name': name,
            'category': category,
            'qty': int(qty),
            'price': float(price),
            'supplier': supplier,
            'description': description,
            'threshold': int(threshold)
        }
        self.products.append(prod)

    def list_products(self):
        return copy.deepcopy(self.products)

    def add_stock(self, code, qty):
        p = self._find(code)
        if not p:
            raise ValueError('Produto não encontrado')
        p['qty'] += int(qty)
        if low_stock_alert(p):
            print(f"ALERTA: Produto {p['code']} atingiu nível baixo: {p['qty']} <= {p['threshold']}")
        return p['qty']

    def remove_stock(self, code, qty):
        p = self._find(code)
        if not p:
            raise ValueError('Produto não encontrado')
        if p['qty'] < qty:
            raise ValueError('Quantidade insuficiente em estoque')
        p['qty'] -= int(qty)
        if low_stock_alert(p):
            print(f"ALERTA: Produto {p['code']} atingiu nível baixo: {p['qty']} <= {p['threshold']}")
        return p['qty']

    def set_quantity(self, code, qty):
        p = self._find(code)
        if not p:
            raise ValueError('Produto não encontrado')
        p['qty'] = int(qty)
        if low_stock_alert(p):
            print(f"ALERTA: Produto {p['code']} atingiu nível baixo: {p['qty']} <= {p['threshold']}")
        return p['qty']

    def set_threshold(self, code, threshold):
        p = self._find(code)
        if not p:
            raise ValueError('Produto não encontrado')
        p['threshold'] = int(threshold)
        return p['threshold']

    def to_list(self):
        return copy.deepcopy(self.products)
