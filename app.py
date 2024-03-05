# inventory_management.py

class InventoryProduct:
    def __init__(self, name, category, quantity, price):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

class SalesTransaction:
    def __init__(self, product, customer_name, quantity, payment_method):
        self.product = product
        self.customer_name = customer_name
        self.quantity = quantity
        self.payment_method = payment_method

class Inventory:
    def __init__(self):
        self.inventory_products = []
        self.sales_transactions = []

    def add_inventory_product(self, product):
        self.inventory_products.append(product)

    def add_sales_transaction(self, transaction):
        self.sales_transactions.append(transaction)
        # Reduce the quantity of the sold product in inventory
        for product in self.inventory_products:
            if product.name == transaction.product.name:
                product.quantity -= transaction.quantity

    def generate_inventory_report(self):
        report = ""
        for product in self.inventory_products:
            report += f"Product: {product.name}, Category: {product.category}, Quantity: {product.quantity}, Price: {product.price}\n"
        return report

    def generate_sales_report(self):
        report = ""
        for transaction in self.sales_transactions:
            report += f"Product: {transaction.product.name}, Customer: {transaction.customer_name}, Quantity: {transaction.quantity}, Payment Method: {transaction.payment_method}\n"
        return report
