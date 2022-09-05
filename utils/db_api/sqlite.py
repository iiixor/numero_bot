import sqlite3

class Database:
    def __init__(self, path_to_db="data/main.db"):
        self.path_to_db = path_to_db

        # self.cursor = self.connection.cursor()

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False,
                fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()

        return data

    # def create_table_users(self):
    #     sql = """
    #     CREATE TABLE users (
    #     user_id int NOT NULL,
    #     name varchar(255) NOT NULL,
    #     subscribe boolean NOT NULL DEFAULT False,
    #     FSM_horoscope int NOT NULL DEFAULT '0',
    #     FSM_square int NOT NULL DEFAULT '0',
    #     PRIMARY KEY (user_id)
    #     );
    #     """
    #
    #     self.execute(sql, commit=True)


    def add_user(self, user_id: int, name: str, subscribe: bool, FSM_horoscope: int, FSM_square: int):
        sql = "INSERT INTO users(user_id, name, subscribe, FSM_horoscope, FSM_square) VALUES (?, ?, ?, ?, ?)"
        parameters = (user_id, name, subscribe, FSM_horoscope, FSM_square)
        self.execute(sql, parameters=parameters, commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM users"
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())


    def select_user(self, **kwargs):

        sql = "SELECT * FROM users WHERE"
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)

    def update_email(self, email, id):
        sql = "UPDATE users SET email=? WHERE id=?"                #ненужнaя функция
        return self.execute(sql, parameters=(email, id), commit=True)

    # def square_count(self, FSM_square):
    #     sql = "INSERT INTO users (FSM_square) VALUES (%s)"
    #     parameters = (FSM_square)
    #     return self.execute(sql, parameters=(FSM_square), commit=True)

    def square_count(self, user_id, FSM_square):
        sql = "UPDATE users SET FSM_square=? WHERE user_id=?"
        parameters = (user_id, FSM_square)
        return self.execute(sql, parameters=(user_id, FSM_square), commit=True)

    def horoscope_count(self, user_id, FSM_horoscope):
        sql = "UPDATE users SET FSM_horoscope=? WHERE user_id=?"
        return self.execute(sql, parameters=(user_id, FSM_horoscope), commit=True)
        
    # def delete_users(self):
    #     self.execute("DELETE FROM users WHERE True") #delete everything

#
#

def logger(statement):
    print(f"""
    _______________________________________
    Executing:
    {statement}
    _______________________________________
    """)






    #
    # def user_exists(self, user_id):
    #     with self.connection:
    #         result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
    #         return bool(len(result))
    #
    # def user_money(self, user_id, money):
    #     with self.connection:
    #         result = self.cursor.execute("SELECT 'money' FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchmany(1)
    #         return int(result[0][0])
    #
    # def set_money(self, user_id, money):
    #     with self.connection:
    #         return self.cursor.execute("UPDATE 'users' SET 'money' = ? WHERE 'user_id' = ?", (money, user_id,))
    #
    #
    # def add_check(self, user_id, money, bill_id):
    #     with self.connection:
    #         self.cursor.execute("INSERT INTO 'check' ('user_id', 'money', 'bill_id') VALUES (?,?,?)", (user_id, money, bill_id,))
    #
    # def get_check(self, bill_id):
    #     with self.connection:
    #         result = self.cursor.execute("SELECT * FROM 'check' WHERE 'bill_id' = ?", (bill_id,)).fetchmany(1)
    #         if not bool(len(result)):
    #             return False
    #         return result[0]
    #
    # def delete_check(self, bill_id):
    #     with self.connection:
    #         return self.cursor.execute("DELETE FROM 'check' WHERE 'bill_id' = ?", (bill_id,))

 # тут только функции
