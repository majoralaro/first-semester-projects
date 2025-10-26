import json
from collections import defaultdict

# In-memory data simulating the database
customers = [
    {'customer_id': 1, 'name': 'Alice Johnson', 'email': 'alice@example.com', 'join_date': '2023-01-15'},
    {'customer_id': 2, 'name': 'Bob Smith', 'email': 'bob@example.com', 'join_date': '2023-02-20'},
    {'customer_id': 3, 'name': 'Charlie Brown', 'email': 'charlie@example.com', 'join_date': '2023-03-10'},
    {'customer_id': 4, 'name': 'Dana Lee', 'email': 'dana@example.com', 'join_date': '2023-04-05'},
    {'customer_id': 5, 'name': 'Eve Kim', 'email': 'eve@example.com', 'join_date': '2023-05-12'}
]

products = [
    {'product_id': 1, 'product_name': 'Soda', 'category': 'Drinks', 'price': 1.50},
    {'product_id': 2, 'product_name': 'Chips', 'category': 'Snacks', 'price': 2.00},
    {'product_id': 3, 'product_name': 'Milk', 'category': 'Dairy', 'price': 3.00},
    {'product_id': 4, 'product_name': 'Bread', 'category': 'Bakery', 'price': 2.50},
    {'product_id': 5, 'product_name': 'Apple', 'category': 'Fruits', 'price': 1.00}
]

orders = [
    {'order_id': 1, 'customer_id': 1, 'product_id': 1, 'quantity': 2, 'order_date': '2023-06-01'},
    {'order_id': 2, 'customer_id': 2, 'product_id': 2, 'quantity': 3, 'order_date': '2023-06-05'},
    {'order_id': 3, 'customer_id': 1, 'product_id': 3, 'quantity': 1, 'order_date': '2023-06-10'},
    {'order_id': 4, 'customer_id': 3, 'product_id': 4, 'quantity': 4, 'order_date': '2023-06-15'},
    {'order_id': 5, 'customer_id': 4, 'product_id': 5, 'quantity': 5, 'order_date': '2023-06-20'},
    {'order_id': 6, 'customer_id': 5, 'product_id': 1, 'quantity': 1, 'order_date': '2023-06-25'}
]

def simulate_new_orders():
    """Simulate new orders by appending to the orders list."""
    global orders  # Declare global at the start
    new_orders = [
        {'order_id': len(orders) + 1, 'customer_id': 1, 'product_id': 2, 'quantity': 1, 'order_date': '2023-07-01'},
        {'order_id': len(orders) + 2, 'customer_id': 3, 'product_id': 1, 'quantity': 10, 'order_date': '2023-07-02'}
    ]
    orders.extend(new_orders)
    print("New orders added successfully.")

def flag_large_orders():
    """Flag orders with total value > $100."""
    print("\nLarge Orders (Total > $100):")
    large_order_found = False
    for order in orders:
        product = next(p for p in products if p['product_id'] == order['product_id'])
        total = order['quantity'] * product['price']
        if total > 100:
            print(f"Order ID {order['order_id']}: Total ${total:.2f}")
            large_order_found = True
    if not large_order_found:
        print("No orders exceed $100.")

def convert_prices():
    """Convert product prices to EUR and apply discounts if price > $5."""
    EUR_RATE = 0.85
    DISCOUNT_THRESHOLD = 5
    DISCOUNT_RATE = 0.10
    print("\nPrice Conversion (USD to EUR with discounts):")
    for product in products:
        eur_price = product['price'] * EUR_RATE
        if product['price'] > DISCOUNT_THRESHOLD:
            eur_price *= (1 - DISCOUNT_RATE)
            print(f"{product['product_name']}: ${product['price']:.2f} -> EUR {eur_price:.2f} (10% discount applied)")
        else:
            print(f"{product['product_name']}: ${product['price']:.2f} -> EUR {eur_price:.2f}")

def generate_report():
    """Generate report: total products sold, most popular product, revenue per customer."""
    report = {
        'total_products_sold': 0,
        'most_popular_product': None,
        'revenue_per_customer': {}
    }
    
    # Total sold and most popular product
    product_quantities = defaultdict(int)
    for order in orders:
        product = next(p for p in products if p['product_id'] == order['product_id'])
        qty = order['quantity']
        report['total_products_sold'] += qty
        product_quantities[product['product_name']] += qty
    
    if product_quantities:
        report['most_popular_product'] = max(product_quantities, key=product_quantities.get)
    
    # Revenue per customer
    for order in orders:
        product = next(p for p in products if p['product_id'] == order['product_id'])
        customer = next(c for c in customers if c['customer_id'] == order['customer_id'])
        revenue = order['quantity'] * product['price']
        report['revenue_per_customer'][customer['name']] = report['revenue_per_customer'].get(customer['name'], 0) + revenue
    
    return report

def save_and_display_report(report):
    """Save report to JSON and display formatted summary."""
    try:
        with open('report.json', 'w') as f:
            json.dump(report, f, indent=4)
        print("\nReport saved to report.json")
    except IOError as e:
        print(f"Error saving report to JSON: {e}")
    
    print("\n--- MiniMart Report ---")
    print(f"Total Products Sold: {report['total_products_sold']}")
    print(f"Most Popular Product: {report['most_popular_product']}")
    print("Revenue per Customer:")
    for customer, revenue in report['revenue_per_customer'].items():
        print(f"  {customer}: ${revenue:.2f}")

def main():
    """Main function to run all tasks."""
    simulate_new_orders()
    flag_large_orders()
    convert_prices()
    report = generate_report()
    save_and_display_report(report)

if __name__ == "__main__":
    main()