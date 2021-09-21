from flask import Flask, jsonify, request, render_template, session, redirect, url_for
import requests
from bson.json_util import dumps
from bson.json_util import loads
from flask_bootstrap import Bootstrap
import os
import certifi

import pymongo
import datetime as dt
import safe_config

app = Flask(__name__)
ca = certifi.where()
on_heroku=False
if 'on_heroku' in os.environ:
    on_heroku = True
    cluster_uri = os.environ['cluster_uri']
    secret_key = os.environ['secret_key']
    cluster = pymongo.MongoClient(cluster_uri)
else:
    
    from config import cluster_uri
    cluster = pymongo.MongoClient(cluster_uri,tlsCAFile=ca)
    secret_key = config.secret_key
    
app.config['SECRET_KEY'] = secret_key
#app.config['DEBUG'] =True

bootstrap = Bootstrap(app)
db = cluster['bordercross']
def arg_getter(items):
    my_dict = {}
    for x in items:
        if x in request.args:
            my_dict.update({x:request.args[x]})
    return my_dict

def dict_cleaner(d):
    st=None
    et=None
    if 'id' in d:
        if d['id'] !='all':
            try:
                val =int(d.pop('id'))
            except:
                d.pop('id')
    if 'start_date' in d:
        st = dt.datetime.strptime(d['start_date'], "%Y-%m-%d")
        d.pop('start_date')

    if 'end_date' in d:
        et = dt.datetime.strptime(d['end_date'], "%Y-%m-%d")
        d.pop('end_date')
    if st != None and et != None:
        d.update({'utc':{'$gte':st,'$lte':et}})
    elif st != None and et == None:
        d.update({'utc':{'$gte':st}})
    elif et != None and st== None:
        d.update({'utc':{'$lte':et}})

    return d

@app.route('/', methods=['POST','GET'])
def index():
    #return "There is no main page, this is only the for API access" + 'date format: %Y-%m-%d --> YYYY-MM-DD'
    return safe_config.basic_html
#{'utc':{$gte:ISODate('2021-09-03')}}
@app.route('/request', methods=['GET'])
def query():
    items = ['id','start_date','end_date', 'region', 'district', 'name', ]
    # if 'id' in request.args and request.args['id'] != 'all':
    #     id = int(request.args['id'])
    # if 'start_date' in request.args:
    #     start_date = str(request.args['start_date'])
    #     start_date = dt.datetime.strptime(start_date,"%Y-%m-%d")
    # if 'end_date' in request.args:
    #     end_date = str(request.args['end_date'])
    #     end_date = dt.datetime.strptime(end_date,"%Y-%m-%d")
    coll = 'running_merge'
    if 'collection' in request.args:
        coll = request.args['collection']

    

    filter = arg_getter(items)
    filter = dict_cleaner(filter)
    
    print(filter)
    results = list(db[coll].find(filter))

    return dumps(results)







if __name__ == '__main__':
    app.run(port = 5000, debug=True)

