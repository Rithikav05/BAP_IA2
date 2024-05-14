import sqlite3, sys

class CIS:
    def __init__(self):
        self.conn=""
        self.crsr=""
        self.err=""

    def ConnectDB(self):
        try:
            self.conn=sqlite3.connect("cinfo.db")
            self.crsr=self.conn.cursor()
            #return("There will be text here soon.")

        except sqlite3.Error as e:
            self.err="Error connecting to Database."+str(e)+"\n"
            sys.exit(1)

    def CreateTable(self):
        try:
            createq='CREATE TABLE IF NOT EXISTS cinfo'
            createq+='(Pno integer primary key, Fname text, Lname text, Email text)'
            self.crsr.execute(createq)

        except sqlite3.Error as e:
            self.err="There is an error creating the table "+str(e)
            #CIS.CloseDB(self)   #IT IS PART OF THE CLASS SO TO CALL THIS FUNTION YOU HAVE TO WRITE CLASS.FUNCTION()
            #sys.exit(1)

    def CloseDB(self):
        try:
            self.conn.close()

        except sqlite3.Error as e:
            self.err="There was an error closing the connection- "+str(e)

    def AddB(self,fname,lname,phoneno,emailid):
        try:

            addq="INSERT INTO cinfo (Pno, Fname, Lname, Email) VALUES (?, ?, ?, ?)"
            self.crsr.execute(addq, (phoneno,fname, lname, emailid))
            self.conn.commit()
            #return("Book added successfully.")

        except sqlite3.Error as er:
            self.err="There was an error inserting record "+str(er)
            #return(self.err )

    def AddInfo(self,fname,lname,phoneno,emailid):

        try:
            searchq="SELECT * FROM cinfo WHERE Pno=?"

            self.crsr.execute(searchq,(phoneno,))

            rdbks=self.crsr.fetchall()
            if rdbks:
                self.UpdateB(fname,lname,phoneno,emailid)
                #return rdbks

            else:
                self.AddB(fname,lname,phoneno,emailid)
                #return("No matching books found.")
        
        except sqlite3.Error as er:
                self.err="There was an error searching for record "+str(er)
                #return(self.err)

    def UpdateB(self,fname,lname,phoneno,emailid):

        try:
            q1="UPDATE cinfo SET "
            if(fname and lname and emailid):
                q1+="Fname = '{0}', Lname='{1}',Email='{2}' where Pno = {3}".format(fname,lname,emailid,phoneno)
                self.crsr.execute(q1)
                self.conn.commit()

            elif (fname and emailid ):
                q1+="Fname = '{0}', Email='{1}'where Pno = {2}".format(fname,emailid,phoneno)
                self.crsr.execute(q1)
                self.conn.commit()

            elif (lname and emailid):
                q1+="Lname = '{0}',Email='{1}' where Pno = {2}".format(lname,emailid,phoneno)
                self.crsr.execute(q1)
                self.conn.commit()

            elif(fname and lname):
                q1+="Fname='{0}',Lname='{1}' where Pno = {2}".format(fname,lname,phoneno)
                self.crsr.execute(q1)
                self.conn.commit()
            
            elif(fname):
                q1+="Fname = '{0}' where Pno = {1}".format(fname,phoneno)
                self.crsr.execute(q1)
                self.conn.commit()

            elif(lname):
                q1+="Lname='{0}' where Pno = {1}".format(lname,phoneno)
                self.crsr.execute(q1)
                self.conn.commit()

            elif(emailid):
                q1+="Email='{0}' where Pno = {1}".format(emailid,phoneno)
                self.crsr.execute(q1)
                self.conn.commit()
            
            '''if(self.conn.total_changes>0):
                return("Book details updated successfully.")
            else:
                return("No matching books found.")'''

        except sqlite3.Error as er:
            self.err="There was an error updating record "+str(er)
            #return(self.err)
            #CIS.CloseDB(self)
            #sys.exit(1)
