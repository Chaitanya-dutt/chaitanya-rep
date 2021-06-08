import pyodbc

def DataUpdate(FirstName,LastName,Feedback):
               conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                      "Server= LAPTOP-AK4UVUIE\SQLEXPRESS;"
                                      "Database=Chaitanya;"
                                      "Trusted_Connection=yes;")
               except:
               dispatcher.utter_message("failed connecting sql server")

               mycursor = conn.cursor()
               sql='INSERT INTO Test_Table (FirstName, LastName, Feedback) VALUES ("{0}","{1}", "{2}");'.format(FirstName,LastName,Feedback)
               mycursor.execute(sql)
               conn.commit()


       return[]
