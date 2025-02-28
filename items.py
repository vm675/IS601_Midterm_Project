import json

def read_orders(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def process_items(orders):
    items = {}
    for order in orders:
        for item in order.get('items', []):  
            item_name = item["name"]
            price = item["price"]
            if item_name in items:
                items[item_name]["orders"] += 1
            else:
                items[item_name] = {
                    "price": price,
                    "orders": 1,
                }
    return items

def main():
    orders = read_orders('example_orders.json')
    items = process_items(orders)
    
    with open('items.json', 'w') as f:
        json.dump(items, f, indent=2)

    print(" items.json has been successfully created!") 

if __name__ == "__main__":
    main()
