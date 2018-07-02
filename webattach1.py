from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from searching import *
app = Flask(__name__)

@app.route('/results/<output>', methods=['GET'])
def res(output):

    render_template('results.html',out=1)

def get_results(query):
    sea = Simsearch(002, "bing", 1, 2,query)
    sea.start()
    # print sea.bing,sea.google
    print sea.run1(),sea.run2()
    redirect(url_for('/results'))

@app.route('/',methods=['GET'])
def index():
    text = request.args.get('search')
    print text
    get_results(text)
    return render_template("index.html")

if __name__ =='__main__':
    app.run()
