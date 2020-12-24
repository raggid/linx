class ProductService:

    def __init__(self, repository):
        self._rp = repository


    def get_product(self, id):
        product = self._rp.get_product(id)
        return product

    def get_products(self, product_list):
        products = self._rp.get_products(product_list)
        return products
