from dataclasses import dataclass
from Name import Name
import pyodbc


@dataclass
class Database:
    __connection = None

    #Opens the connection to the database
    @classmethod
    def connect(cls):
        if cls.__connection is None:
            server = 'tcp:cisdbss.pcc.edu'
            database = 'NAMES'
            username = '275student'
            password = '275student'
            trustedconnection = 'yes'
            trustservercertificate = 'yes'
            try:
                cls.__connection = pyodbc.connect(
                    'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ';DATABASE=' + database
                    + ';UID=' + username + ';PWD=' + password
                    + ';trustedconnection=' + trustedconnection
                    + ';trustservercertificate=' + trustservercertificate)
            except pyodbc.InterfaceError:
                cls.__connection = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database
                    + ';UID=' + username + ';PWD=' + password)

    @classmethod
    def readNames(cls, year, gender):
        cls.connect()
        sql = """
        SELECT TOP 20 Name, Year, Gender, NameCount
        FROM all_data
        WHERE Year = ?
        AND Gender = ?
        ORDER BY NameCount DESC;
        """
        cursor = cls.__connection.cursor()
        cursor.execute(sql, year, gender)
        data = cursor.fetchall()
        names = []
        for row in data:
            names.append(Name(row.Name, row.Year, row.Gender, row.NameCount))
        return names
