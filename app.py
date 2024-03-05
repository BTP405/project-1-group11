class Inventory:
    def __init__(self):
        self.inventory_products = []
        self.sales_transactions = []

    def add_inventory_product(self, product):
        self.inventory_products.append(product)

    def delete_inventory_product(self, product_name):
        for product in self.inventory_products:
            if product.name == product_name:
                self.inventory_products.remove(product)
                return True
        return False

    def add_sales_transaction(self, transaction):
        self.sales_transactions.append(transaction)
        # Reduce the quantity of the sold product in inventory
        for product in self.inventory_products:
            if product.name == transaction.product.name:
                product.quantity -= transaction.quantity

    def delete_sales_transaction(self, product_name):
        for transaction in self.sales_transactions:
            if transaction.product.name == product_name:
                self.sales_transactions.remove(transaction)
                return True
        return False

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
