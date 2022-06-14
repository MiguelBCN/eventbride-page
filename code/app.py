from flask import Flask
from flask_restful import Api

from resources.event import event
from resources.event import eventList
from resources.ticket import ticket

app = Flask(__name__)
api = Api(app)




# Resources to get by Restfull
api.add_resource(event, '/event/<int:id>')
api.add_resource(eventList, '/eventList')

api.add_resource(ticket, '/event/<int:id>/ticket')

# Main Page
@app.route('/')
def hello_world():
    return 'Testing Backend!'

if __name__ == '__main__':
    app.run()
