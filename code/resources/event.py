from flask_restful import Resource


class event(Resource):
    def get(self):
        return {"proba":"proba"}, 200


class eventList(Resource):
    def get(self):
        return {"proba":"proba"}, 200
