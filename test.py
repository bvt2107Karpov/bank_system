import sqlite3


card_number = login.Login().return_crd_num()
transaction_type = 'test'
amount = 1


with sqlite3.connect('bank.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS registration (
                        card_number INTEGER PRIMARY KEY,
                        transaction_type TEXT,
                        amount INTEGER
                    )
                    """)
        cursor.execute("INSERT INTO registration VALUES (?, ?, ?)", (card_number, transaction_type, amount))