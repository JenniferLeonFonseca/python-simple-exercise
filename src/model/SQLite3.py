import sqlite3
import pandas as pd
from sqlite3 import Error


class HandleSQL:

    def __init__(self):
        self.conn = self.sql_connection()
        self.cursorObj = self.conn.cursor()

    def sql_connection(self):
        try:
            con = sqlite3.connect('data_exercise.db')
            return con
        except Error:
            print(Error)

    def sql_insert(self, df_data):
        try:
            df_data.to_sql(name='regions', con=self.conn)
        except Error:
            print(Error)

    def sql_fetch(self):

        self.cursorObj.execute('SELECT * FROM employees')
        rows = cursorObj.fetchall()

        return rows
