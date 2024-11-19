from flask_restful import Api
from constants import *
from api import *



USER_BASE_ROUTE = "/user"
USER_ID_ROUTE = f"{USER_BASE_ROUTE}/<string:user_id>"

USERS_ROUTE = "/users"
WORKOUTS_ROUTE = "/workouts/<string:user_id>"

ROUTES = {
    "RegisterUser": USER_BASE_ROUTE,
    "GetUser":USER_ID_ROUTE ,
    "RemoveUser": USER_ID_ROUTE,
    "ListUsers": USERS_ROUTE,
    "AddWorkout": WORKOUTS_ROUTE,
    "ListWorkouts": WORKOUTS_ROUTE,
}

METHODS = {
    "RegisterUser":"POST",
    "GetUser":"GET",
    "RemoveUser":"DELETE",
    "ListUsers":"GET",
    "AddWorkout":"PUT",
    "ListWorkouts":"GET"
    
}


RESOURCES = {
    "RegisterUser": RegisterUser,
    "GetUser": GetUser,
    "RemoveUser": RemoveUser,
    "ListUsers": ListUsers,
    "AddWorkout": AddWorkout,
    "ListWorkouts": ListWorkouts
}

def init_routes(api: Api) -> None:
    for api_name, resource in RESOURCES.items():
        api.add_resource(resource, ROUTES[api_name], methods=[METHODS[api_name]])

