from abc import ABC, abstractmethod
from postgres import Postgres


class Connection(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        pass


class PostgresConnection(Connection):
    def __init__(self):
        super().__init__()
        self.db = self.connect()

    def connect(self):
        db = Postgres('postgresql://postgres:admin@postgres:5432/postgres')
        return db