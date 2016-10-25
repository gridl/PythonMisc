# CMs are constructs that allow setup and teandowns
# gurantee that cleanup happens no matter what


# import sqlite3
class DataConn:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        # open the database connection

        self.conn = sqlite3.connect(self.db_name)
        return self.conn


    def __exit__(self, exc_type, exc_val, exc_tb):
        # close the connection
        self.conn.close()
        if exc_val:
            raise


if __name__ == '__main__':
    db ='/Users/vsubr2/Projects/PythonMisc/test.db'
    with DataConn(db) as conn:
        cursor = conn.cursor()

