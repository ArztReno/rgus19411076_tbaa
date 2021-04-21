# date : 27/12/2020
# Author : Renato Gusani
# Student no. : x19411076
# Question 1 – Design Patterns : a1, b1

# * * * * * * * * * * question a.1) * * * * * * * * * *

# these are the packages to establish the connection
from pymongo import Connection
import os

# this is the database connection class
class MongoDBConnection(object):
    __database = None

# This is the singleton Design Pattern
    @classmethod
    def get_connection(cls):
        if cls.__databbase is None:
            cls.__database = Connection()
        return cls.__database 

''' Advantage of Singleton Design Pattern;
To assure only one and same instance of object every time.

Take a scenario, say for a Company application, 
there is only one CEO. If I wanted to create or access CEO object, 
I should return the same CEO object every time. '''

# * * * * * * * * * * question b.1) * * * * * * * * * *

''' Here, I characterize the capacity, where the boundary is xyz, which is show
for the way that it wraps a capacity. At that point, I characterize the 
covering.

My wrapper here is basic, it just checks if the client has a "logged_in" 
in their meeting. If not, they get a glimmer message and a divert to the 
login page. 

Flask is the system here, Flask is the model used to make occurrences of
web application or web applications. Thus, when I import Flask, I need to
make an occurrence of the Flask class for my web application. '''

import flask

def login_required(xyz):
    @wraps(xyz)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return xyz(*args, **kwargs)
        else:
            flash("login first")
            return redirect(url_for('login_page'))

    return wrap

'''Since I have the wrapper capacity,  I now apply it to my 
logout page, this way: '''

@app.route("/logout/")
@login_required
def logout():
    session.clear()
    flash("You have been signed out!")
    gc.collect()
    return redirect(url_for('dashboard')

'''Adequately basic, under the app.route wrapper, I likewise added another
wrapper, which is the login_required wrapper.'''

'''Advantage of Decorator Design Pattern;
It is more flexible than inheritance because inheritance adds responsibility at compile time but
decorator pattern adds at run time. I can have any number of decorators and also
in any order. It extends functionality of object without affecting any other object.'''