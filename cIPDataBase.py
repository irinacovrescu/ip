import mysql.connector
import datetime

class myDataBase:
    def __init__(self):
        self.mydb = mysql.connector.connect(user='root', password='root',
                                      host='127.0.0.1',
                                      database='irinadb')
        self.myCursor = self.mydb.cursor(buffered=True)

    def askLogIn(self,username,parola):
        query="SELECT * FROM Users WHERE Name=\'"+username+"\' AND Password=\'"+parola+"\'"
        self.myCursor.execute(query)
        answer=self.myCursor.fetchone()
        if answer is not None:
            return True
        else:
            return False

    def exportCurrent(self,username,parola):
        query="SELECT Sold FROM Users WHERE Name=\'"+username+"\' AND Password=\'"+parola+"\'"
        self.myCursor.execute(query)
        answer=self.myCursor.fetchone()
        return answer
