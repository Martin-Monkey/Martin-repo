
import json

class Parser:
    @staticmethod
    def save_order(order, filename):
        data = {
            'order': str(order),
            'total': order.total
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def load_order(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        print(f"Order loaded: {data['order']} - Total: ${data['total']}")
