https://github.com/Saylee1998/FlaskProject

Name: **Saylee Mangesh Waje**

Email: **swaje@stevens.edu**

## **STRAVA LITE**

Strava Lite is a basic running tracker application similar to the popular Strava app. It's built using Flask, a Python web framework, and allows users to:

### 1.User Management:
Users can register with a unique ID, view their profile, and delete their account if necessary.

### 2.Tracking Workout:
Users can log new workout with specific details like date,distance and time,also view list of their past workouts.

### 3.Follow Friend:
Users can follow other runners to view their workout history.


### APIs:
1.**RegisterUser:** To add a new user by name.


2.**GetUser:** To retrieve a user's information by ID

3.**RemoveUser:** To delete a user having specific ID

4.**ListUsers:** To list all existing users

5.**AddWorkout:** To add a workout specific user's account.

6.**ListWorkouts:** To get all the workout of given user.

7.**FollowFriend:** Allows users to follow other runners

8.**ShowFriendWorkouts:** Allow users to view the workouts of the runners they follow

### Run the project:
Step1 :  pip install -r requirements.txt

Step2 : python app.py

### Bugs and issues faced:
The initial implementation of the workouts object as a local variable within the RegisterUser method limited its scope. By transforming it into a global dictionary and initializing an empty list for each new user, the system now maintains workout data across different API interactions.

