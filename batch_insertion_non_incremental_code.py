import csv
import mysql.connector
from dotenv import load_dotenv
import os
from pathlib import Path
load_dotenv()

#fetching database details from .env
DB_HOST = os.environ.get("DATABASE_HOST", "localhost")  # Defaults to 'localhost' if missing
DB_USER = os.environ.get("DATABASE_USER")
DB_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DB_NAME = os.environ.get("DATABASE_NAME")

#creating connection
conn = mysql.connector.connect(
    host = DB_HOST,
    user= DB_USER,
    password= DB_PASSWORD,
    database= DB_NAME
)

if conn:
    print("Connected to database")
    # Loading execution
    # Loop through the files in folder of specific type using Path and glob
    folder_path = Path("./datasets")
    cursor = conn.cursor()
    batch_size = 200
    available_files = {file.name : file for file in folder_path.glob("*.csv")}
    load_order = [
        ("warehouse.csv", "warehouse"),
        ("customer.csv", "customer"),
        ("product.csv", "product"),
        ("inventory.csv", "inventory"),
        ("orders.csv", "orders"),
        ("order_items.csv", "order_items"),
        ("payments.csv", "payments")
    ]

    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    # truncate the table to reset auto increment pk in mysql
    for table in load_order:
        table_name = table[1]
        cursor.execute(f"TRUNCATE TABLE {table_name}")
    conn.commit()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    batch = [] # batch processing rows stored in list as temp storage
    #looping
    for file_name, table_name in load_order:
        if file_name in available_files:
            print("Fetching file...", file_name)
            with open(available_files[file_name], "r", encoding="utf-8") as f:
                table_name = table_name
                print("Opening file: ", table_name)
                dict_reader = csv.DictReader(f)
                # dynamic sql query
                headers = dict_reader.fieldnames
                columns = ",".join(headers)
                placeholders = ",".join([f"%({h})s" for h in headers])
                query = f"INSERT INTO {table_name}({columns}) VALUES({placeholders})"
                print("Starting insertion to database...")
                # batch processing code
                for row in dict_reader:
                    batch.append(row)
                    # if len(batch) == batch_size:
                    #     cursor.executemany(query, batch)
                    #     conn.commit()
                    #     batch = []

                    if batch and len(batch) == batch_size:
                        try:
                            cursor.executemany(query, batch)
                            print(f"Finished insertion of {file_name} data to mysql database...")
                            conn.commit()
                            batch = []
                        except mysql.connector.Error as err:
                            conn.rollback()
                            for row in batch:
                                try:
                                    #cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
                                    cursor.execute(f"TRUNCATE TABLE {table_name}")
                                    #cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
                                    cursor.execute(query,row)
                                except mysql.connector.Error as err:
                                    print(f"{err} found while inserting row data - {row}")
                if 0 < len(batch) < batch_size:
                    try:
                        cursor.executemany(query, batch)
                        print(f"Finished insertion of {file_name} data to mysql database...")
                        conn.commit()
                        batch = []
                    except mysql.connector.Error as err:
                        conn.rollback()
                        for row in batch:
                            try:
                                #cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
                                cursor.execute(f"TRUNCATE TABLE {table_name}")
                                #cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
                                cursor.execute(query, row)
                            except mysql.connector.Error as err:
                                print(f"{err} found while inserting row data - {row}")
        else:
            print("File not found - ", file_name)
    #cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

conn.close()
print("Connection closed")