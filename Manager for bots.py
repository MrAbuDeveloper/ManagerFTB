import psycopg2
from data.config import DB_NAME, DB_USER, DB_HOST, DB_PASSWORD


class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database=DB_NAME,
            host=DB_HOST,
            password=DB_PASSWORD,
            user=DB_USER
        )

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                commit: bool = False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
            return result