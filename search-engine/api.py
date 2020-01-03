from flask import Flask, jsonify
from flask import abort

import jwt
import json

app = Flask(__name__)

#API description
apiDescription = [
    {
        'title': u'Health Insights API',
        'description': u'An API to query the healthcare dataset insights', 
        'Author': u'DSC UMass'
    }
]

@app.route('/health-insights/api/v1.0/about', methods=['GET'])
def get_tasks():
    return jsonify({'description': apiDescription[0]})

@app.route('/health-insights/api/v1.0/<string:query>', methods=['GET'])
def get_query(query):

    with open('secret.json') as json_file:
        secret = json.load(json_file)['secret']
    
    query_test = "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJoZWxsbyI6IndlaXJkIn0.kjCG2vDIrrzFdF9HmGBJr8kFWl2p85xw2loFYZyyqa4'"
    decoded = jwt.decode(query_test, secret, algorithms=['HS256'])

    # except:
    #     return "error"
    
        
    return jsonify({'response': decoded})


# Helper Functions 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)