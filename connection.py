import pyodbc

def get_connection():
  #Change according to your settings
  connection = pyodbc.connect('Driver={SQL Server};'
                    'Server=DESKTOP-DO-MALO\SQLEXPRESS;'
                    'Database=System_Information;'
                    'Trusted_Connection=yes;')
  return connection