import json

from postgres import Postgres

db = Postgres('postgres://postgres:admin@postgres:5432/postgres')


def create_table():
    db.run('''            
        create table if not exists product(
                id varchar primary key,
                json_data varchar
            )
    ''')


def load_data():
    with open('catalog.json', 'r') as file:
        for line in file:
            product_id = json.loads(line).pop('id')
            try:
                db.run("insert into product values (%s, %s)", (product_id, line))
            except:
                print("Produto Já Cadastrado")


if __name__ == '__main__':
    create_table()
    load_data()
