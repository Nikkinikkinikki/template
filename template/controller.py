from bottle import route, get, post, request, redirect, static_file

import model



#-----------------------------------------------------------------------------
'''
    This file will handle our typical Bottle requests and responses
    You should not have anything beyond basic page loads, handling forms and
    maybe some simple program logic
'''

#-----------------------------------------------------------------------------
# Static file paths
#-----------------------------------------------------------------------------

# Allow image loading
@route('/img/<picture:path>')
def serve_pictures(picture):
    return static_file(picture, root='img/')

#-----------------------------------------------------------------------------

# Allow CSS
@route('/css/<css:path>')
def serve_css(css):
    return static_file(css, root='css/')

#-----------------------------------------------------------------------------

# Allow javascript
@route('/js/<js:path>')
def serve_js(js):
    return static_file(js, root='js/')

#-----------------------------------------------------------------------------
# Pages
#-----------------------------------------------------------------------------

# Redirect to login
@get('/')
@get('/home')
def get_index():
    return model.index_page()

#-----------------------------------------------------------------------------

# Display the login page
@get('/login')
def get_login_controller():
    return model.login_page()

#-----------------------------------------------------------------------------

# Attempt the login
@post('/login')
def post_login():
    # Handle the form processing
    username = request.forms.get('username')
    password = request.forms.get('password')

    # Call the appropriate method
    return model.login_check(username, password)


#-----------------------------------------------------------------------------
#Sign up
#-----------------------------------------------------------------------------
@get('/signup')
def get_signup_controller():
    return model.signup_page()

# Attempt the login
@post('/signup')
def post_signup():
    # Handle the form processing
    username = request.forms.get('username')
    password = request.forms.get('password')

    # Call the appropriate method
    return model.add_user(username, password)

#-----------------------------------------------------------------------------
#Messages
#-----------------------------------------------------------------------------
@get('/chat')
def get_chat():
    return model.chat_page()

@post('/chat')
def post_chat():
    receiver = request.forms.get('receiver')
    msg = request.forms.get('message')

    return model.send_message(receiver,msg)

@get('/sent')
def get_sent():
    model.sent_page()
    redirect('/msg')

@get('/unsent')
def get_unsent():
    model.unsent_page()
    redirect('/chat')

@get('/msg')
def get_msg():
    return model.msg_page()

@post('/msg')
def post_msg():
    sender = request.forms.get('sender')
    return model.load_msg(sender)

@get('/messages')
def get_messages():
    model.messages_page()
#-----------------------------------------------------------------------------

@get('/logout')
def logout():
    return model.logout()

@get('/help')
def get_help():
    return model.help_page()

@get('/about')
def get_about():
    return model.about_page()

@get('/htmlintro')
def get_html_intro():
    return model.html_intro_page()

@get('/htmlbasic')
def get_html_basic():
    return model.html_basic_page()

@get('/htmlheading')
def get_html_basic():
    return model.html_heading_page()

# css
@get('/cssintro')
def get_html_intro():
    return model.css_intro_page()

@get('/csssyntax')
def get_html_intro():
    return model.css_syntax_page()

@get('/csscolour')
def get_html_intro():
    return model.css_colour_page()

#js
@get('/javaintro')
def get_html_intro():
    return model.js_intro_page()

@get('/javasyntax')
def get_html_intro():
    return model.js_syntax_page()

@get('/javavariable')
def get_html_intro():
    return model.js_variable_page()

#web Server

@get('/php')
def get_html_intro():
    return model.web_php_page()

@get('/sql')
def get_html_intro():
    return model.web_sql_page()

@get('/bottle')
def get_html_intro():
    return model.web_bottle_page()

