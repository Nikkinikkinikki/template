import random
import sql
import sqlite3
from bs4 import BeautifulSoup as soup
'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
import view
from operator import itemgetter

# Initialise our views, all arguments are defaults
curr_user = None
logged_in = False
page_view = view.View()
sql = sql.SQLDatabase()
sql.database_setup()
#-----------------------------------------------------------------------------
# Index
#-----------------------------------------------------------------------------

def index_page():
    return page_view("home")

#-----------------------------------------------------------------------------
# Login
#-----------------------------------------------------------------------------

def login_page():
    return page_view("login")

#-----------------------------------------------------------------------------

# Check the login credentials
def login_check(username, password):
    # By default assume bad creds
    err_str = "Incorrect Username or Password"

    logged_in = sql.check_credentials(username,password)
    print(logged_in)

    if logged_in:
        page_view.set_logged_state(True)
        #return page_view("home", name=username)
        global curr_user
        curr_user = username
        return page_view("validLog", name=username)
    else:
        return page_view("invalidLog", reason=err_str)


def logout():
    page_view.set_logged_state(False)
    return page_view("home")



#-----------------------------------------------------------------------------
#Signup
#-----------------------------------------------------------------------------

def signup_page():
    return page_view("signup")
#-----------------------------------------------------------------------------
def add_user(username, password):
    add_success = sql.add_user(username,password)
    if(add_success):
        return page_view("validSign", name=username)
    else:
        return page_view("invalidSign", reason="Username taken")

#-----------------------------------------------------------------------------
#Messages
#-----------------------------------------------------------------------------
def chat_page():
    return page_view("chat")

def send_message(receiver,msg):
    valid_user = sql.find_user(receiver)
    if(valid_user):
        sql.store_msg(curr_user,receiver, msg)
        return page_view("sent")
    else:
        return page_view("unsent", receiver=receiver)

def sent_page():
    return page_view("sent")

def unsent_page():
    return page_view("unsent")

def msg_page():
    return page_view("msg")

def messages_page():
    print("messages page")
    return page_view("messages")


def load_msg(u):
    msglist = []
    print(u)
    all_sent = sql.retrieve_msgs(curr_user,u)
    all_received = sql.retrieve_msgs(u, curr_user)
    if(all_sent!=None):
        for x in all_sent:
            msglist.append(x)
    if(all_received!=None):
        for x in all_received:
            msglist.append(x)
    msglist_s = sorted(msglist, key=itemgetter(0))
    print(msglist_s)
    strTable = "<div class='table table-hover'><table><tr><th>Sender</th><th>Message</th></tr>"
    for x in msglist_s:
        msg=x[1]
        sender=x[2]
        strRW = "<tr><td>" + sender + "</td><td>" + msg + "</td></tr>"
        strTable = strTable + strRW
    strTable = strTable + "</table></div>"
    hs = open("html/messages.html", 'w')
    back = "<a href='msg'><p><button class='w3-button w3-blue'>Back to view Messages</button></p></a>"
    hs.write(strTable)
    hs.write(back)
    hs.close()
    print(strTable)
    return page_view("messages")




#-----------------------------------------------------------------------------
# html Introduction
#html contents
#-----------------------------------------------------------------------------

def html_intro_page():
    return page_view("htmlintro")

def html_basic_page():
    return page_view("htmlbasic")

def html_heading_page():
    return page_view("htmlheading")

#css contents

def css_intro_page():
    return page_view("cssintro")

def css_syntax_page():
    return page_view("csssyntax")
def css_colour_page():
    return page_view("csscolour")

#Js contents
def js_intro_page():
    return page_view("javaintro")

def js_syntax_page():
    return page_view("javasyntax")

def js_variable_page():
    return page_view("javavariable")

#web server contents
def web_php_page():
    return page_view("php")

def web_sql_page():
    return page_view("sql")

def web_bottle_page():
    return page_view("bottle")


#-----------------------------------------------------------------------------

# About
#-----------------------------------------------------------------------------



def about_page():
    return page_view("about", garble=about_garble())


def help_page():
    return page_view("help")

# Returns a random string each time
def about_garble():
    garble = ["leverage agile frameworks to provide a robust synopsis for high level overviews.",
    "iterate approaches to corporate strategy and foster collaborative thinking to further the overall value proposition.",
    "organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment.",
    "bring to the table win-win survival strategies to ensure proactive domination.",
    "ensure the end of the day advancement, a new normal that has evolved from generation X and is on the runway heading towards a streamlined cloud solution.",
    "provide user generated content in real-time will have multiple touchpoints for offshoring."]
    return garble[random.randint(0, len(garble) - 1)]

#-----------------------------------------------------------------------------
