from flask import Flask, jsonify
from flask import abort

app = Flask(__name__)

#API description
apiDescription = [
    {
        'title': u'Health Insights API',
        'description': u'An API to query the healthcare dataset insights', 
        'Author': u'DSC UMass'
    }
]

@app.route('/show-tell/api/v1.0/about', methods=['GET'])
def get_tasks():
    return jsonify({'description': apiDescription[0]})

@app.route('/show-tell/api/v1.0/<string:query>', methods=['GET'])
def get_query(query):
    return jsonify({'response': query})


# Helper Functions 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)