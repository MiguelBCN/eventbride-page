from flask_restful import Resource


class ticket(Resource):
    def get(self,id):

        return {"proba":id}, 200


class ticketList(Resource):
    def get(self):
        return {"proba":"proba"}, 200