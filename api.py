from flask_restful import Resource, reqparse
from uuid import uuid4 as generateId  

users = {}
workouts={}
following={}

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
            
        }
        workouts[user_id] = []
        following[user_id] = set()
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
        return {"users": [user for user in users.values()]}, 200
        

    



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
            "distance": args["distance"],
            "time": args["time"]
            
        }
        workouts[user_id].append(workout)
        return workout, 200


class ListWorkouts(Resource):
    def get(self, user_id):
        user = users.get(user_id)
        if user is None:
            return {"message": "User not found"}, 404

        return {"workouts": workouts[user_id]}, 200
    


follow_friend_parser = reqparse.RequestParser()
follow_friend_parser.add_argument(
    "follow_id", type=str, required=True, help="follow_id is required"
)

class FollowFriend(Resource):
    def put(self, user_id):
        args = follow_friend_parser.parse_args()
        follow_id = args["follow_id"]
        
        if user_id not in users or follow_id not in users:
            return {"message": "User not found"}, 404

        following[user_id].add(follow_id)
        return {"following": list(following[user_id])}, 200

class ShowFriendWorkouts(Resource):
    def get(self, user_id, follow_id):
        
        if user_id not in users or follow_id not in users:
            return {"message": "User not found"}, 404

        
        if follow_id not in following[user_id]:
            return {"message": "You are not following this user"}, 403

        
        return {"workouts": workouts[follow_id]}, 200        