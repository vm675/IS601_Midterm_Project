import json

def read_orders(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def extract_customer_data(orders):
    customer_data = {}
    for order in orders:
        phone = order.get("phone")
        name = order.get("name")
        if phone and name:
            customer_data[phone] = name  
    return customer_data

def main():
    orders = read_orders('example_orders.json')
    customer_data = extract_customer_data(orders)
    
    with open('customers.json', 'w') as f:
        json.dump(customer_data, f, indent=2)

    print(" customers.json has been successfully created!")  

if __name__ == "__main__":
    main()
