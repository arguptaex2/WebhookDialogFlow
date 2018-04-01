import os
from flask import Flask
from flask import request
from flask import make_response
import urllib
from api import fetchHomeDetails
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def webHoookResult(req):
    result = req.get("result")
    action = result.get('action')
    if action != 'home_search':
        return ([],None)
    params = result.get("parameters")
    if len(params) == 0:
        return ([],None)
    city = params.get('city')
    homes = params.get('home')
    community = params.get('community')
    zip = params.get('zip')
    #speech = 'You searched for {} in {} for the community {} and zipcode {}'.format(homes,city,community,zip)
    response = fetchHomeDetails(city)['Result']
    communities = []
    for result in response:
        communities.append(result.get('CommName'))

    respText = os.linesep.join(communities)
    print(respText)
    speech = "Here are the list of Communities to choose from:\n{}".format(respText)

    return {
        'speech':speech,
        'displayText':speech,
        'source':'dialogflow'
    }



@app.route('/webhook',methods=['POST'])
def webhook():
    req = request.get_json(silent=True,force=True)
    print(json.dumps(req,indent=4))
    res = webHoookResult(req)
    res = json.dumps(res,indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-type'] = 'application/json'
    return r


if __name__ == '__main__':
    app.run(debug=True)
