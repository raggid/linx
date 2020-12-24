from repository.connection import Connection
import json


class ProductRepository:

    def __init__(self, connection: Connection):
        self._conn = connection.connect()

    def get_product(self, product_id):
        product = json.loads(self._conn.one("select json_data from product where id = %(id)s", id=product_id))
        return product

    def get_products(self, product_list):
        data = {}
        products = self._conn.all("select json_data from product where id = ANY (%s)", (product_list,))
        for product in products:
            json_product = json.loads(product)
            data[json_product['id']] = json_product
        return data
