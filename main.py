import os

from flask import Flask, jsonify, request, abort

from components import CardsView, Card, CardHeader

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
    # process payload from archy
    payload = request.json.get('payload', {})
    args = payload.get('args', {})
    links = [{
        'address': '/list'
    }]
    viewProps = {'links': links}

    view = CardsView(viewProps,
        Card({},
            CardHeader({
                'title': 'Card Title 1',
                'subtitle': 'card subtitle',
            })),
        Card({},
            CardHeader({
                'title': 'Card Title 2',
                'subtitle': 'card subtitle',
            })),
    )

    return jsonify(**view.to_dict())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
