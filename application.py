from flask import Flask
from flask import jsonify
from flask import request

from pprint import pprint
filename = 'ncaa.dat'


# print a nice greeting.
def say_hello():
    return '<p>Hello NCAA</p>\n'

# print a nice greeting.

def lookup(param, val):
    rows = []
    error = None
    query = "%s fields containing \"%s\"" % (param, val)
    for k in database.keys():
        if val in database[k][param]:
            rows.append(database[k])
    if not rows:
        error = 'no %s matches found for "%s"' % (param, val)


    response = jsonify({'result': rows, 'error': error, 'query': query})
    return response


# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p>This is a RESTful micro service returning information on NCAA Div I football teams</p>
    <UL>
        <LI><I>param</I>/<i>search string</i><br/>where <I>param</I> is school, conference, mascot, city or state and  
    </UL>\n''' 

home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

def teamdb():
    db = {}
    with open(filename) as f:
        for line in f.read().splitlines():
            cols = line.split("\t")
            db[cols[0]] = {'school': cols[0],
                           'mascot': cols[1],
                           'city': cols[2],
                           'state': cols[3],
                           'conference': cols[4]
                          }
    return db

# EB looks for an 'application' callable by default.
application = Flask(__name__)
database = teamdb()


# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + "example: %sschool/bama" % request.url_root + footer_text))

# # add a rule when the page is accessed with a name appended to the site URL.
# application.add_url_rule('/<username>', 'hello', (lambda username:
#     header_text + say_hello(username) + home_link + footer_text))

# add a rule when the page is accessed with a name appended to the site URL.
application.add_url_rule('/<param>/<school>', 'lookup', (lambda param, school:
    lookup(param, school)))

# run the app.
if __name__ == "__main__":

    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
