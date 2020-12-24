from fastapi import FastAPI
import uvicorn

from repository import ProductRepository
from repository.connection import PostgresConnection
from service import ProductService

app = FastAPI()

conn = PostgresConnection()
p_repo = ProductRepository(conn)
service = ProductService(p_repo)


@app.get('/products/{product_id}')
async def get_product(product_id: str):
    return service.get_product(product_id)


@app.post('/products')
async def get_products(id_list: list):
    return service.get_products(id_list)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
