from flask_restful import Resource, reqparse
from uuid import uuid4 as generateId  

users = {}

register_user_parser = (reqparse.RequestParser()
    .add_argument("name", type=str, required=True,help="Name is required")
    .add_argument("age", type=int, required=True))

class RegisterUser(Resource):
    def post(self):
        name, age = register_user_parser.parse_args().values()
        user_id = str(generateId())
        users[user_id] = {
            "id": user_id,
            "name": name,
            "age": age,
            "workouts": []
        }
        return users[user_id], 200
    
class GetUser(Resource):
    def get(self, user_id):  
        user = users.get(user_id)
        if user is None:
            return {"message": "User not found"}, 404
        return user, 200


class RemoveUser(Resource):
    def delete(self,user_id):
        if user_id in users:
            del users[user_id]
            return {}, 200
        return {"message": "User not found"}, 404
    

class ListUsers(Resource):
    def get(self):
        return {"users": list(users.values())}, 200
    



add_workout_parser = (reqparse.RequestParser()
    .add_argument("date", type=str, required=True, help="Date is required")
    .add_argument("time", type=str, required=True, help="Time is required")
    .add_argument("distance", type=str, required=True, help="Distance is required"))



class AddWorkout(Resource):
    def put(self, user_id):
        args = add_workout_parser.parse_args()
        user = users.get(user_id)
        if user is None:
            return {"message": "User not found"}, 404

        workout = {
            "date": args["date"],
            "time": args["time"],
            "distance": args["distance"],
        }
        user["workouts"].append(workout)
        return workout, 200


class ListWorkouts(Resource):
    def get(self, user_id):
        user = users.get(user_id)
        if user is None:
            return {"message": "User not found"}, 404

        return {"workouts": user["workouts"]}, 200