import json, os

class Storage:
    def __init__(self, path):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)

    def load(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save(self, products_list):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(products_list, f, indent=4, ensure_ascii=False)
