# CNA 335 W21
# Instructor: Justin Ellis, jellis@rtc.edu
# T.J. Dewey, tjdewey@student.rtc.edu

# Restful interface that has search and update options for navigationg a zip code database on phpmyadmin

# Sources:
# https://pythonbasics.org/webserver/
#https://stackoverflow.com/questions/8211128/multiple-distinct-pages-in-one-html-file
#https://stackoverflow.com/questions/902408/how-to-use-variables-in-sql-statement-in-python
#https://stackoverflow.com/questions/1081750/python-update-multiple-columns-with-python-variables
#https://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for
#https://github.com/vimalloc/flask-jwt-extended/issues/175
#https://stackoverflow.com/questions/45017338/pycharm-cant-find-flask-template-that-exists

from mysql import connector
from flask import Flask, render_template, request, url_for, redirect
import mysql.connector

# saved unused imports:
# import condigparser, requests, time, json, urllib.request



app = Flask(__name__, static_url_path='')

##### Connect to Database #####

conn = mysql.connector.connect(user='root',
                               host='127.0.0.1',
                               password='',
                               database='zipcodes',
                               buffered=True)

cursor = conn.cursor()


##SQL functions #######################


# Query the database
@app.route('/searchZIP/<searchzip>')
def searchzip(searchzip):
    cursor.execute("SELECT * FROM `zipcodes` WHERE zip=%s", [searchzip])
    test = cursor.rowcount
    if test != 1:
        return searchzip + "was not found"
    else:
        searched = cursor.fetchall()
        return 'Success! Here you go: %s' % searched


# Update database zipcode population
@app.route('/updatezip_pop/<updateZIP>,<updatePOP>')
def updatezip_pop(updateZIP, updatePOP):
    cursor.execute("SELECT * FROM `zipcodes` WHERE zip=%s", [updateZIP])
    test = cursor.rowcount
    if test != 1:
        return updateZIP + "was not found"
    else:
        cursor.execute("UPDATE `zipcodes` SET Population=%s WHERE zip=%s;", [updatePOP, updateZIP])
        cursor.execute("SELECT * FROM `zipcodes` WHERE zip=%s and Population=%s", [updateZIP, updatePOP])
        test1 = cursor.rowcount
        if test1 != 1:
            return updateZIP + "failed to update"
        else:
            return 'Population has been updated successfully for zipcode: %s' % updateZIP


# Update webpage
@app.route('/update', methods=['POST'])
def update():
    user1 = request.form['uzip']
    user2 = request.form['upop']
    return redirect(url_for('updatezip_pop', updateZIP=user1, updatePOP=user2))


# search page
@app.route('/search', methods=['GET'])
def search():
    user = request.args.get('szip')
    return redirect(url_for('searchzip', searchzip=user))


# root of web server and gots to template (login.html)

@app.route('/')
def root():
    return render_template('login.html')


##Main Fucntion########################
if __name__ == '__main__':
    app.run(debug=True)

# REQUIREMENTS:
##hosts a webserver on port 5000
##Has 2 pages:
##          /search: queries SQL DB and prints out row data
##          /update: updates SQL DB row
