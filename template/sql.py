import sqlite3, datetime

# This class is a simple handler for all of our SQL database actions
# Practicing a good separation of concerns, we should only ever call 
# These functions from our models

# If you notice anything out of place here, consider it to your advantage and don't spoil the surprise

class SQLDatabase():
    # Get the database running
    def __init__(self, database_arg="Users.db"):
        self.conn = sqlite3.connect(database_arg)
        self.cur = self.conn.cursor()
        id = 1

    # SQLite 3 does not natively support multiple commands in a single statement
    # Using this handler restores this functionality
    # This only returns the output of the last command
    def execute(self, sql_string):
        out = None
        for string in sql_string.split(";"):
            try:
                out = self.cur.execute(string)
            except:
                pass
        return out

    # Commit changes to the database
    def commit(self):
        self.conn.commit()

    #-----------------------------------------------------------------------------
    
    # Sets up the database
    # Default admin password
    def database_setup(self, admin_password='WaSdIjKl3113'):

        # Clear the database if needed
        self.execute("DROP TABLE IF EXISTS Users")
        self.execute("DROP TABLE IF EXISTS Messages")
        self.commit()

        # Create the users table
        self.cur.execute("""CREATE TABLE Users(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            admin INTEGER DEFAULT 0
        )""")

        self.cur.execute("""CREATE TABLE Messages(
             Id INTEGER PRIMARY KEY AUTOINCREMENT,
             Sender TEXT,
             Receiver TEXT,
             Message TEXT,
             MessageNum INTEGER
         )""")
         self.commit()



        # Add our admin user
        self.add_user('admin', admin_password, admin=1)
        print("Database created")


    #-----------------------------------------------------------------------------
    # User handling
    #-----------------------------------------------------------------------------

    # Add a user to the database
    def add_user(self, username, password, admin=0):
        find_user = ("SELECT 1 FROM Users WHERE username = ?")
        self.cur.execute(find_user, [(username)])
        results = self.cur.fetchone()
        if results!= None:
            return False
        else:
            sql_cmd = """
                    INSERT INTO Users(username,password,admin)
                    VALUES( '{username}', '{password}', {admin})
                """.format(username=username, password=password, admin=admin)

            self.cur.execute(sql_cmd)
            self.cur.execute("SELECT * FROM Users")
            print(self.cur.fetchall())

            self.commit()
            return True

    #-----------------------------------------------------------------------------

    # Check login credentials
    def check_credentials(self, u, p):
        find_user = ("SELECT 1 FROM Users WHERE username = ? AND password = ?")
        self.cur.execute(find_user, [(u), (p)])
        results = self.cur.fetchone()
        print(results)
        if results!= None:
            return True
        else:
            return False

    #-----------------------------------------------------------------------------
    #Messages
    def store_msg(self,sender, receiver, msg, msg_num=1):
        self.cur.execute("SELECT MAX(MessageNum) FROM Messages WHERE Sender = '{s}' AND Receiver = '{r}'".format(s=sender,r=receiver))
        max_num = self.cur.fetchone()
        print(max_num[0])
        if(max_num[0] != None):
            msg_num = max_num[0]+1
        insert_msg = """INSERT INTO Messages (Sender, Receiver, Message, MessageNum) 
                     VALUES ('{s}','{r}', '{m}', '{mn}')
                     """.format(s=sender, r=receiver, m=msg, mn=msg_num)
        self.cur.execute(insert_msg)
        self.cur.execute("SELECT * FROM Messages")
        print(self.cur.fetchall())
        self.commit()


    def retrieve_msgs(self, sender_u, receiver_u):
        print("sender: {s}, Receiver: {r}".format(s=sender_u, r=receiver_u))
        self.cur.execute("SELECT Id,Message,Sender FROM Messages WHERE Sender = '{s}' AND Receiver = '{r}'".format(s=sender_u,r=receiver_u))
        msgs = self.cur.fetchall()
        print(msgs)
        return msgs

    def message_count(self,sender,receiver):
        self.cur.execute(
            "SELECT MAX(MessageNum) FROM Messages WHERE Sender = '{s}' AND Receiver = '{r}'".format(s=sender, r=receiver))
        max_num = self.cur.fetchone()
        print(max_num[0])
        return max_num[0]
    #-----------------------------------------------------------------------------
    #Find User
    def find_user(self, u):
        find_user = ("SELECT 1 FROM Users WHERE username = '{}'".format(u))
        self.cur.execute(find_user)
        results = self.cur.fetchone()
        if results!= None:
            return True
        else:
            return False



