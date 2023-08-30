import os
import pyodbc

from ACHFileParser import ACHFileParser

def insert_to_db(ach_object, cursor):
    for record in ach_object.records:
        record_dict = record.to_dict()
        
        # Insert statement, adapt fields and table name to your needs
        query = """
        INSERT INTO ACHRecords (Field1, Field2, Field3, ...)
        VALUES (?, ?, ?, ...);
        """
        
        # Execute and commit
        cursor.execute(query, record_dict['Field1'], record_dict['Field2'], record_dict['Field3'], ...)
        cursor.commit()

if __name__ == "__main__":
    ach_folder = "path/to/your/ach/files"
    
    # Establish DB connection
    conn = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=your_server;'
                          'DATABASE=your_db;'
                          'UID=your_user;'
                          'PWD=your_password;')

    cursor = conn.cursor()

    for ach_file in os.listdir(ach_folder):
        if ach_file.endswith(".ach") or ach_file.endswith(".txt"):  # Adapt the condition to your needs
            ach_path = os.path.join(ach_folder, ach_file)
            ach_object = ACHFileParser(ach_path)
            insert_to_db(ach_object, cursor)
